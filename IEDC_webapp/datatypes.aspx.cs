using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class datatypes : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string categories_query = "select id, name, description, reserve1, reserve2 from iedc.categories";
                objDataHandling.dataGrid(grdCategories, categories_query);
                string types_query = "select id, name, description, reference_data_category, symbol, reserve1, reserve2, reserve3 from iedc.types";
                objDataHandling.dataGrid(grdTypes, types_query);
                string layers_query = "select id, name, description, reserve1, reserve2 from iedc.layers";
                objDataHandling.dataGrid(grdLayers, layers_query);
            }

        }
        
    }
}