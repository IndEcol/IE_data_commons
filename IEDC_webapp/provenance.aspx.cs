using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class provenance : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string provenance_query = "select id, name, description, reserve1, reserve2 from iedc.provenance";
                objDataHandling.dataGrid(grdProvenance, provenance_query);
                string sources_query = "select id, name, description, reserve1, reserve2 from iedc.source_type";
                objDataHandling.dataGrid(grdSources, sources_query);
                string licences_query = "select id, name, description, link, reserve1, reserve2 from iedc.licences";
                objDataHandling.dataGrid(grdLicences, licences_query);
            }

        }
    }
}