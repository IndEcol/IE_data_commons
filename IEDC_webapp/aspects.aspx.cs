using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class aspects : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string aspects_query = "select id, aspect, description, dimension, index_letter, index_letter_crib, reserve1, reserve2, reserve3 from iedc.aspects";
                objDataHandling.dataGrid(grdAspect, aspects_query);
                string dimensions_query = "select id, name, description, reserve1, reserve2, reserve3, reserve4, reserve5 from iedc.dimensions";
                objDataHandling.dataGrid(grdDimensions, dimensions_query);

            }

        }
    }
}