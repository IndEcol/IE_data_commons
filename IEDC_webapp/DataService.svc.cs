using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Activation;
using System.ServiceModel.Web;
using System.Text;

namespace IEF_Database
{
    [ServiceContract(Namespace = "")]
    [AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
    public class DataService
    {
        // To use HTTP GET, add [WebGet] attribute. (Default ResponseFormat is WebMessageFormat.Json)
        // To create an operation that returns XML,
        //     add [WebGet(ResponseFormat=WebMessageFormat.Xml)],
        //     and include the following line in the operation body:
        //         WebOperationContext.Current.OutgoingResponse.ContentType = "text/xml";


        [OperationContract]
        [WebInvoke(Method = "POST",
            BodyStyle = WebMessageBodyStyle.WrappedRequest,
            ResponseFormat = WebMessageFormat.Json
            )]
        public string GetProducts()
        {
            //JavaScriptSerializer json = new JavaScriptSerializer();
            IList<Product> personList = ProductRepository.GetProducts();
            int total = 1, page = 10;
            ProductJqGridView productJqGridView = new ProductJqGridView(total, page, personList);
            return productJqGridView.ToJson();
        }



        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string DataSet(string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.DataSet();
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, strSort);
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][2] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][3] + "'" + ",");

                        stringBuilder.Append("'" + dtNew.Rows[i][4] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][5] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][6] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][7] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][8] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][9] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][10] + "'" + "");


                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string stockProcessList(string system_id)
        {
            clsDataHandling objDataClass = new clsDataHandling();
            DataTable dt = objDataClass.stockProcessList(system_id);
            StringBuilder str = new StringBuilder();

            str.Append("[");
            str.Append("{");
            str.Append("\"code\":\"0\" ,");
            str.Append("\"name\":\"--Select--\"");
            str.Append("},");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                str.Append("{");
                str.Append("\"code\":\"" + dt.Rows[i]["process_id"].ToString() + "\" ,");
                str.Append("\"name\":\"" + dt.Rows[i]["process_name"].ToString() + "\" ");
                str.Append("},");
            }
            str = str.Remove(str.Length - 1, 1);
            str.Append("]");
            return str.ToString();
        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string sourceFLowList(string system_id)
        {
            clsDataHandling objDataClass = new clsDataHandling();
            DataTable dt = objDataClass.sourceFLowList(system_id);
            StringBuilder str = new StringBuilder();

            str.Append("[");
            str.Append("{");
            str.Append("\"code\":\"0\" ,");
            str.Append("\"name\":\"--Select--\"");
            str.Append("},");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                str.Append("{");
                str.Append("\"code\":\"" + dt.Rows[i]["process_id"].ToString() + "\" ,");
                str.Append("\"name\":\"" + dt.Rows[i]["process_name"].ToString() + "\" ");
                str.Append("},");
            }
            str = str.Remove(str.Length - 1, 1);
            str.Append("]");
            return str.ToString();
        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string targetFLowList(string system_id, string source_flow)
        {
            clsDataHandling objDataClass = new clsDataHandling();
            DataTable dt = objDataClass.targetFLowList(system_id, source_flow);
            StringBuilder str = new StringBuilder();

            str.Append("[");
            str.Append("{");
            str.Append("\"code\":\"0\" ,");
            str.Append("\"name\":\"--Select--\"");
            str.Append("},");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                str.Append("{");
                str.Append("\"code\":\"" + dt.Rows[i]["process_id"].ToString() + "\" ,");
                str.Append("\"name\":\"" + dt.Rows[i]["process_name"].ToString() + "\" ");
                str.Append("},");
            }
            str = str.Remove(str.Length - 1, 1);
            str.Append("]");
            return str.ToString();
        }
        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string Stocks(string stock_id, string selectedYear, string selectedCountry, string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.stocksDataTable(stock_id, selectedYear, selectedCountry);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, strSort);
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][2] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][3] + "'" + ",");

                        stringBuilder.Append("'" + dtNew.Rows[i][4] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][5] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][6] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][7] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][8] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][9] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][10] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][11] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][12] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][13] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][14] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][15] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][16] + "'" + "");


                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }
        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string Flows(string source_flow_id, string target_flow_id, string selectedYear, string selectedCountry, string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.flowsDataTable(source_flow_id, target_flow_id, selectedYear, selectedCountry);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, strSort);
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][2] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][3] + "'" + ",");

                        stringBuilder.Append("'" + dtNew.Rows[i][4] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][5] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][6] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][7] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][8] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][9] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][10] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][11] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][12] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][13] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][14] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][15] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][16] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][17] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][18] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][19] + "'" + "");


                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }



        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string CycleYear(string system_id)
        {
            clsDataHandling objDataClass = new clsDataHandling();
            DataTable dt = objDataClass.CycleYear(system_id);
            StringBuilder str = new StringBuilder();

            str.Append("[");
            str.Append("{");
            str.Append("\"code\":\"0\" ,");
            str.Append("\"name\":\"--Select--\"");
            str.Append("},");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                str.Append("{");
                str.Append("\"code\":\"" + dt.Rows[i]["year"].ToString() + "\" ,");
                str.Append("\"name\":\"" + dt.Rows[i]["year"].ToString() + "\" ");
                str.Append("},");
            }
            str = str.Remove(str.Length - 1, 1);
            str.Append("]");
            return str.ToString();
        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string CycleCountry(string system_id, string selected_year)
        {
            clsDataHandling objDataClass = new clsDataHandling();
            DataTable dt = objDataClass.CycleCountry(system_id, selected_year);
            StringBuilder str = new StringBuilder();

            str.Append("[");
            str.Append("{");
            str.Append("\"code\":\"0\" ,");
            str.Append("\"name\":\"--Select--\"");
            str.Append("},");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                str.Append("{");
                str.Append("\"code\":\"" + dt.Rows[i]["ISO"].ToString() + "\" ,");
                str.Append("\"name\":\"" + dt.Rows[i]["COUNTRY"].ToString() + "\" ");
                str.Append("},");
            }
            str = str.Remove(str.Length - 1, 1);
            str.Append("]");
            return str.ToString();
        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string FlowCycle(string selectedYear, string selectedCountry, string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.flowCycleDataTable(selectedYear, selectedCountry);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, strSort);
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][2] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][3] + "'" + ",");

                        stringBuilder.Append("'" + dtNew.Rows[i][4] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][5] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][6] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][7] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][8] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][9] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][10] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][11] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][12] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][13] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][14] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][15] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][16] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][17] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][18] + "'" + ",");
                        stringBuilder.Append("'" + dtNew.Rows[i][19] + "'" + "");


                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string IEDC_DataSet(string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1, string selectedItems, string searchText)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.IEDC_DataSet(selectedItems, searchText);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, strSort);
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");
                        stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");
                        if (dtNew.Rows[i][1].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][1].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + ",");

                        if (dtNew.Rows[i][2].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][2].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][2] + "'" + ",");

                        if (dtNew.Rows[i][3].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][3].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][3] + "'" + ",");

                        if (dtNew.Rows[i][4].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][4].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][4] + "'" + ",");
                        if (dtNew.Rows[i][5].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][5].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][5] + "'" + ",");

                        if (dtNew.Rows[i][6].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][6].ToString().Replace("'", "\\'") + "'" + "");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][6] + "'" + "");

                      



                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string IEDC_DataSetView(string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1, string datasetId)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.IEDC_DataSetView(datasetId);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, "");
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        if (dtNew.Rows[i][0].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][0].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");

                        if (dtNew.Rows[i][1].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][1].ToString().Replace("'", "\\'") + "'" + "");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + "");



                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }

        [OperationContract]
        [WebInvoke(Method = "POST", BodyStyle = WebMessageBodyStyle.WrappedRequest, ResponseFormat = WebMessageFormat.Json)]
        public string IEDC_DataGroupView(string searchField1, string searchOper1, string searchString1, int page1, string pageSize1, string sortIndex1, string sord1, int totalrows1, string datasetId)
        {
            clsDataHandling objDataClass = new clsDataHandling();

            DataTable dt = null;

            dt = objDataClass.IEDC_DataGroupView(datasetId);
            int page = page1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["page"].ToString());

            string sidx = sortIndex1;// HttpContext.Current.Request.QueryString["sidx"].ToString();
            string sord = sord1;// HttpContext.Current.Request.QueryString["sord"].ToString();
            int totalRows = totalrows1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["totalrows"].ToString());


            string searchField = searchField1;// HttpContext.Current.Request.QueryString["SEARCHFIELD"];
            string searchString = searchString1;// HttpContext.Current.Request.QueryString["SEARCHSTRING"];
            string searchOper = searchOper1;// HttpContext.Current.Request.QueryString["SEARCHOPER"];
            if (page == 0) page = 1;
            string result = "";
            if (String.IsNullOrEmpty(sidx)) sidx = "1";
            int count;
            result = dt.Rows.Count.ToString();
            count = dt.Rows.Count;
            int totalpages;
            Int32 limit = 0;
            if (pageSize1 == "All")
            {
                limit = Convert.ToInt32(result);
            }
            else
            {
                limit = Convert.ToInt32(pageSize1);// pageSize1;// Convert.ToInt32(HttpContext.Current.Request.QueryString["rows"].ToString());
            }


            double hasilbagi = Convert.ToDouble(result) / Convert.ToDouble(limit);
            if (int.Parse(result) > 0) totalpages = Convert.ToInt32(Math.Ceiling(hasilbagi));
            else
                totalpages = 0;

            if (Convert.ToInt32(page) > totalpages) page = totalpages;
            int start = limit * page - limit;
            if (start < 0) start = 0;

            string strFilter = objDataClass.SetSearchStr(searchOper, searchField, searchString);
            string strSort = sidx + " " + sord;
            DataRow[] dr = dt.Select(strFilter, "");
            DataTable dtNew;

            StringBuilder stringBuilder = new StringBuilder("{");
            stringBuilder.Append("total: " + totalpages + ", ");
            stringBuilder.Append("page: " + page + ", ");
            stringBuilder.Append("records: " + count + ", ");
            stringBuilder.Append("  rows : [ ");
            if (dr.Length > 0)
            {
                dtNew = dr.CopyToDataTable<DataRow>();
                for (int i = start; i < dt.Rows.Count; i++)
                {
                    if (i < dtNew.Rows.Count)
                    {
                        stringBuilder.Append("{");

                        stringBuilder.Append("id:" + i + ", ");
                        stringBuilder.Append("cell:[ ");

                        if (dtNew.Rows[i][0].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][0].ToString().Replace("'", "\\'") + "'" + ",");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][0] + "'" + ",");

                        if (dtNew.Rows[i][1].ToString().Contains("'"))

                            stringBuilder.Append("'" + dtNew.Rows[i][1].ToString().Replace("'", "\\'") + "'" + "");

                        else
                            stringBuilder.Append("'" + dtNew.Rows[i][1] + "'" + "");



                        stringBuilder.Append(" ]");
                        if (i == dt.Rows.Count - 1)
                        {
                            stringBuilder.Append(" }");
                        }
                        else
                        {
                            stringBuilder.Append(" },");
                        }
                    }
                }
            }

            stringBuilder.Append(" ]");
            stringBuilder.Append(" }");
            return stringBuilder.ToString();

        }
        
    }
}
