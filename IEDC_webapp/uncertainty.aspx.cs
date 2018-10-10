using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class uncertainty : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string stats_array_query = "select id, name, description, loc, scale, shape from iedc.stats_array";
                objDataHandling.dataGrid(grdStatsArray, stats_array_query);
                
            }

        }
    }
}