using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class frmDatabase : System.Web.UI.Page
    {
        clsDataHandling clsD = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {


            if (!Page.IsPostBack)
            {
                //clsD.datasetDropDown(drdDataSet);
                clsD.getYear(hdnYear);
                clsD.getCountry(hdnCountry);
                //clsD.datasetGridView(grdDataSet);

            }

        }

        protected void btnDatasetGridSelect_Click(object sender, EventArgs e)
        {
            //rdoProcessType.Enabled = true;
            //System.Web.UI.WebControls.Button btn = (System.Web.UI.WebControls.Button)sender;
            //GridViewRow gvr = (GridViewRow)btn.NamingContainer;
            //string datasetId = gvr.Cells[1].Text;
            ////clsD.processListGridView(grdProcessList, datasetId);

            //clsD.processListDropDown(drdStocks, datasetId);
            //clsD.processListDropDown(drdSourceFlows, datasetId);
            //clsD.processListDropDown(drdTargetFlows, datasetId);
        }

        protected void btnProcessListGridSelect_Click(object sender, EventArgs e)
        {
            System.Web.UI.WebControls.Button btn = (System.Web.UI.WebControls.Button)sender;
            GridViewRow gvr = (GridViewRow)btn.NamingContainer;
            string processId = gvr.Cells[2].Text;

            bindGrid(processId);


            //clsD.processListGridView(grdProcessList, datasetId);
        }

        protected void bindGrid(string processId)
        {
            //string type = rdoProcessType.SelectedValue;

            //if (type == "1")
            //{
            //    //clsD.stocksGridView(grdStocks, processId);
            //}

            //else if (type == "2")
            //{
            //    //clsD.flowsGridView(grdFlows, processId);
            //}
        }

        protected void rdoProcessType_SelectedIndexChanged(object sender, EventArgs e)
        {
            //string type = rdoProcessType.SelectedValue;

            //if (type == "1")
            //{
            //    drdStocks.Enabled = true;
            //    drdSourceFlows.Enabled = false;
            //    drdTargetFlows.Enabled = false;
            //}

            //else if (type == "2")
            //{
            //    drdSourceFlows.Enabled = true;
            //    drdTargetFlows.Enabled = true;
            //    drdStocks.Enabled = false;
            //}
        }

        protected void drdStocks_SelectedIndexChanged(object sender, EventArgs e)
        {
            //string param = "stocks.time in (" + hdnYear.Value + ")";
            //clsD.stocksGridView(grdStocks, Convert.ToString(drdStocks.SelectedValue), param);
        }

        protected void drdSourceFlows_SelectedIndexChanged(object sender, EventArgs e)
        {
            //clsD.flowsGridView(grdFlows, Convert.ToString(drdSourceFlows.SelectedValue), Convert.ToString(drdTargetFlows.SelectedValue));
        }

        protected void drdTargetFlows_SelectedIndexChanged(object sender, EventArgs e)
        {
            //clsD.flowsGridView(grdFlows, Convert.ToString(drdSourceFlows.SelectedValue), Convert.ToString(drdTargetFlows.SelectedValue));
        }

        protected void btnLoggOut_Click(object sender, EventArgs e)
        {

        }

        protected void grdDataSet_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            //grdDataSet.PageIndex = e.NewPageIndex;
            //clsD.datasetGridView(grdDataSet);
        }

        protected void grdProcessList_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {

        }

        protected void grdStocks_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            //string param = "stocks.time in (" + hdnYear.Value + ")";
            //grdStocks.PageIndex = e.NewPageIndex;
            //clsD.stocksGridView(grdStocks, Convert.ToString(drdStocks.SelectedValue), param);
        }

        protected void grdFlows_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            //grdFlows.PageIndex = e.NewPageIndex;
            //clsD.flowsGridView(grdFlows, Convert.ToString(drdSourceFlows.SelectedValue), Convert.ToString(drdTargetFlows.SelectedValue));
        }

        protected void btnFilter_Click(object sender, EventArgs e)
        {
            //string type = rdoProcessType.SelectedValue;

            //if (type == "1")
            //{

            //    string param = "stocks.time in (" + hdnSelectedYear.Value + ")";
            //    string paramss = "stocks.time in (" + hdnSelectedCountry.Value + ")";

            //    //clsD.stocksGridView(grdStocks, Convert.ToString(drdStocks.SelectedValue), param);
            //}

            //else if (type == "2")
            //{
            //    drdSourceFlows.Enabled = true;
            //    drdTargetFlows.Enabled = true;
            //    drdStocks.Enabled = false;
            //}
        }

     

    }
}