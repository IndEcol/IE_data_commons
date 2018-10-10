using IEF_Database.cls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class classifications : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                string classifications_query = "select id, classification_Name, dimension, description, reference, ";
                classifications_query += "meaning_attribute1, meaning_attribute2, meaning_attribute3, meaning_attribute4, meaning_attribute5 ";
                classifications_query += " ";
                classifications_query += " from iedc.classification_definition";
                objDataHandling.dataGrid(grdClassifications, classifications_query);

                string dropClassificaitonsQuery = "SELECT distinct id, classification_Name FROM iedc.classification_definition;";
                objDataHandling.dropdown(drpClassifications, dropClassificaitonsQuery);

            }

        }

        protected void drpClassifications_SelectedIndexChanged(object sender, EventArgs e)
        {
            string id = drpClassifications.SelectedValue;
            string classification_item_query = "select id, classification_id, parent_id, description, reference, attribute1_oto, attribute2_oto, attribute3_oto, attribute4_oto, attribute5_anc ";
            classification_item_query += " from iedc.classification_items where classification_id =" + id + "";
            objDataHandling.dataGrid(grdClassificationItems, classification_item_query);
        }

        protected void grdClassifications_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            string classifications_query = "select id, classification_Name, dimension, description, reference, ";
            classifications_query += "meaning_attribute1, meaning_attribute2, meaning_attribute3, meaning_attribute4, meaning_attribute5 ";
            classifications_query += " ";
            classifications_query += " from iedc.classification_definition";
            grdClassifications.PageIndex = e.NewPageIndex;
            objDataHandling.dataGrid(grdClassifications, classifications_query);
        }

        protected void grdClassificationItems_PageIndexChanging(object sender, GridViewPageEventArgs e)
        {
            string id = drpClassifications.SelectedValue;
            string classification_item_query = "select id, classification_id, parent_id, description, reference, attribute1_oto, attribute2_oto, attribute3_oto, attribute4_oto, attribute5_anc ";
            classification_item_query += " from iedc.classification_items where classification_id =" + id + "";
            grdClassificationItems.PageIndex = e.NewPageIndex;
            objDataHandling.dataGrid(grdClassificationItems, classification_item_query);
        }
    }
}