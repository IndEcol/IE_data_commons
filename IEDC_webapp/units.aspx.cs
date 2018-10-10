using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class units : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                
                string units_query = "select id, refunit_id, unitcode, alt_unitcode, alt_unitcode2, unit_name, alt_unit_name, alt_unit_name2, factor from iedc.units";
                objDataHandling.dataGrid(grdUnits, units_query);
            }

        }
    }
}