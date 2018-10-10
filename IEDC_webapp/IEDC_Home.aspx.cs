using ClosedXML.Excel;
using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class IEDC_Home : System.Web.UI.Page
    {
        clsDataHandling objDataClass = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {


        }

        protected void btnSave_Click(object sender, EventArgs e)
        {
            int download_format = drdDownload.SelectedIndex;
            if (download_format == 1)
            {
                download_as_xls();
            }
        }

        private void download_as_xls()
        {
            string dataset_id = hdnDatasetId.Value;
            DataSet ds = getDataSetExportToExcel(dataset_id);

            string dataset_name = objDataClass.DataSetName(dataset_id) + ".xlsx";
            //exportToExcel(ds);

            using (XLWorkbook wb = new XLWorkbook())
            {

                wb.Worksheets.Add(ds.Tables[0], "Dataset description");
                wb.Worksheets.Add(ds.Tables[1], "Data");
                //foreach (System.Data.DataTable dt in ds.Tables)
                //{
                //    wb.Worksheets.Add(dt, "");
                //    wb.Worksheets.Name = “NewTabName”;
                //}

                //Export the Excel file.
                Response.Clear();
                Response.Buffer = true;
                Response.Charset = "";
                Response.ContentType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";
                Response.AddHeader("content-disposition", "attachment;filename=" + dataset_name + "");
                using (MemoryStream MyMemoryStream = new MemoryStream())
                {
                    wb.SaveAs(MyMemoryStream);
                    MyMemoryStream.WriteTo(Response.OutputStream);
                    Response.Flush();
                    Response.End();
                }
            }
        }

        public DataSet getDataSetExportToExcel(string dataset_id)
        {
            DataSet ds = new DataSet();

            string[] colNamesFlow = { "Source", "Value", "Color", "Flow Style", "Target" };
            string[] colNamesNodes = { "Name", "Color", "Orientation", "Width", "Height", "X_position", "Y_position" };

            //string flow_data = Convert.ToString(input_flow_data.InnerText);
            //string node_data = Convert.ToString(input_node_data.InnerText);

            System.Data.DataTable DataSet = new System.Data.DataTable("Dataset description");
            System.Data.DataTable Data = new System.Data.DataTable("Data");

            //dt_s = sampleData(dt_s);

            DataSet = objDataClass.IEDC_DataSetView(dataset_id);
            Data = objDataClass.IEDC_DataTable(dataset_id);

            ds.Tables.Add(DataSet);
            ds.Tables.Add(Data);

            return ds;
        }

        public System.Data.DataTable parsedData(System.Data.DataTable dt, string node_data, string[] colNames)
        {
            //System.Data.DataTable dt = new System.Data.DataTable(tableName);
            string[] lineData = Regex.Split(node_data, "[\r\n]+");
            string pattern = @"\[([^\]]*)\]";

            for (int i = 0; i < colNames.Length; i++)
            {
                dt.Columns.Add(new DataColumn(colNames[i]));
            }

            for (var f = 0; f < lineData.Length; f++)
            {
                MatchCollection matches = Regex.Matches(lineData[f], pattern);
                var row = dt.Rows.Add();

                for (var c = 0; c < matches.Count; c++)
                {
                    row[colNames[c]] = matches[c].Groups[0].Value.Substring(1, matches[c].Groups[0].Value.Length - 2);

                }
            }

            return dt;
        }
    }
}