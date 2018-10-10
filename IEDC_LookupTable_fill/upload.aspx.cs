using IEF_Database.cls;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Common;
using System.Data.OleDb;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace IEF_Database
{
    public partial class upload : System.Web.UI.Page
    {
        clsDataHandling objDataHandling = new clsDataHandling();
        protected void Page_Load(object sender, EventArgs e)
        {
            if (!IsPostBack)
            {
                objDataHandling.listTables(drpTables);
            }
        }

        

        protected void btnCreateTable_Click(object sender, EventArgs e)
        {
            string ExcelContentType = "application/vnd.ms-excel";
            string Excel2010ContentType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

            if (FileUpload1.HasFile)
            {
                if (FileUpload1.PostedFile.ContentType == ExcelContentType || FileUpload1.PostedFile.ContentType == Excel2010ContentType)
                {
                    try
                    {
                        //Save file path 
                        string path = string.Concat(Server.MapPath(FileUpload1.FileName));
                        FileUpload1.SaveAs(path);

                        string excelConnectionString = string.Format("Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties=Excel 8.0", path);

                        // Create Connection to Excel Workbook 
                        using (OleDbConnection connection = new OleDbConnection(excelConnectionString))
                        {
                            OleDbCommand command = new OleDbCommand("Select * FROM [Sheet1$]", connection);

                            connection.Open();
                            OleDbDataAdapter da = new OleDbDataAdapter(command);

                            DataTable dt = new DataTable();
                            da.Fill(dt);

                            dbConnect cn = new dbConnect();

                            string database_name = "iedc";
                            string table_name = database_name + "." + txt_table.Text;
                            string Columns = "";
                            if (cn.open_connection() == true)
                            {
                                MySqlCommand cmd;
                                string[] columnNames = dt.Columns.Cast<DataColumn>()
                                 .Select(x => x.ColumnName)
                                 .ToArray();
                                foreach (DataRow row in dt.Rows)
                                {
                                    if (row[0].ToString().ToLower() == "id")
                                        Columns += row[0] + " " + row[2] + " " + row[3] + " AUTO_INCREMENT" + "," + "\r\n";
                                    else
                                        Columns += row[0] + " " + row[2] + " " + row[3] + "," + "\r\n";
                                    //cmd = new MySqlCommand(query, cn.connection);
                                    //cmd.ExecuteNonQuery();
                                    
                                }
                                string query = "CREATE TABLE " + table_name  + " (" + "\r\n" + Columns + "\r\n"+ "PRIMARY KEY (id)" + "\r\n"+ ");";
                                cmd = new MySqlCommand(query, cn.connection);
                                cmd.ExecuteNonQuery();

                                cn.close_connection();
                            }

                        }
                        File.Delete(path);
                    }

                    catch (Exception ex)
                    {
                        //Label1.Text = ex.Message;
                        
                    }
                }


            }


            
        }

        protected void btnDataUpload_Click(object sender, EventArgs e)
        {
            //fileUploader();
            string ExcelContentType = "application/vnd.ms-excel";
            string Excel2010ContentType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

            if (flUpload.HasFile)
            {
                if (flUpload.PostedFile.ContentType == ExcelContentType || flUpload.PostedFile.ContentType == Excel2010ContentType)
                {
                    try
                    {
                        //Save file path 
                        string path = string.Concat(Server.MapPath(flUpload.FileName));
                        flUpload.SaveAs(path);

                        //For Office Excel 2010   http://social.msdn.microsoft.com/Forums/en-US/exceldev/thread/0f03c2de-3ee2-475f-b6a2-f4efb97de302/#ae1e6748-297d-4c6e-8f1e-8108f438e62e 
                        string excelConnectionString = string.Format("Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties=Excel 8.0", path);

                        // Create Connection to Excel Workbook 
                        using (OleDbConnection connection = new OleDbConnection(excelConnectionString))
                        {
                            OleDbCommand command = new OleDbCommand("Select * FROM [Sheet1$]", connection);

                            connection.Open();
                            OleDbDataAdapter da = new OleDbDataAdapter(command);

                            DataTable dt = new DataTable();
                            da.Fill(dt);

                            dbConnect cn = new dbConnect();

                            string database_name = "iedc";
                            string table_name = database_name + "." + drpTables.SelectedValue.ToString();

                            if (cn.open_connection() == true)
                            {
                                MySqlCommand cmd, cmd1,cmd2;
                                string[] columnNames = dt.Columns.Cast<DataColumn>()
                                 .Select(x => x.ColumnName)
                                 .ToArray();
                                string columns = string.Join(", ", columnNames);
                                
                                //string query1 = "delete from " + table_name + "";
                                //string query2 = "ALTER TABLE " + table_name + " AUTO_INCREMENT = 1";
                                //cmd1 = new MySqlCommand(query1, cn.connection);
                                //cmd2 = new MySqlCommand(query2, cn.connection);
                                //cmd1.ExecuteNonQuery();
                                //cmd2.ExecuteNonQuery();
                                foreach (DataRow row in dt.Rows)
                                {
                                    string rows = "";
                                    foreach (DataColumn col in dt.Columns)
                                    {
                                        if (col.ToString().ToLower() != "id")
                                        {
                                            if (row[col].ToString().ToLower() == "true" || row[col].ToString().ToLower() == "false")
                                                rows += row[col] + ", ";
                                            else
                                            {

                                                if (row[col].ToString().Contains("'"))
                                                {
                                                    string formatedRow = row[col].ToString().Replace("'", "\\'");
                                                    rows += "'" + formatedRow + "'" + ", ";
                                                }
                                                else
                                                    rows += "'" + row[col] + "'" + ", ";
                                            }

                                        }

                                    }

                                    string query = "Insert INTO " + table_name + " (" + columns + ") values (" + "default, " + rows.Remove(rows.Length - 2) + ")";
                                    cmd = new MySqlCommand(query, cn.connection);
                                    cmd.ExecuteNonQuery();

                                }
                                cn.close_connection();
                            }

                        }
                    }

                    catch (Exception ex)
                    {
                        //Label1.Text = ex.Message;
                    }
                }


            }
        }

        public void fileUploader()
        {
            string[] Individal_Runs = Directory.GetFiles(@"C:\files");
            foreach (string s in Individal_Runs)
            {
                try
                {
                    //Save file path 
                    string path = string.Concat(Server.MapPath("aspects_data.xlsx"));
                    flUpload.SaveAs(path);

                    //For Office Excel 2010   http://social.msdn.microsoft.com/Forums/en-US/exceldev/thread/0f03c2de-3ee2-475f-b6a2-f4efb97de302/#ae1e6748-297d-4c6e-8f1e-8108f438e62e 
                    string excelConnectionString = string.Format("Provider=Microsoft.ACE.OLEDB.12.0;Data Source={0};Extended Properties=Excel 8.0", path);

                    // Create Connection to Excel Workbook 
                    using (OleDbConnection connection = new OleDbConnection(excelConnectionString))
                    {
                        OleDbCommand command = new OleDbCommand("Select * FROM [Sheet1$]", connection);

                        connection.Open();
                        OleDbDataAdapter da = new OleDbDataAdapter(command);

                        DataTable dt = new DataTable();
                        da.Fill(dt);

                        dbConnect cn = new dbConnect();

                        string database_name = "iedc";
                        string table_name = database_name + "." + drpTables.SelectedValue.ToString();
                        //classification_definition
                        //aspects
                        //string query = "Insert INTO "+ table_name + " (id,aspect,description,dimension,index_letter,index_letter_crib,reserve1,reserve2,reserve3) values (" + row[0] + ",'" + row[1] + "','" + row[2] + "','" + row[3] + "','" + row[4] + "','" + row[5] + "','" + row[6] + "','" + row[7] + "','" + row[8] + "')";


                        if (cn.open_connection() == true)
                        {
                            MySqlCommand cmd;
                            string[] columnNames = dt.Columns.Cast<DataColumn>()
                             .Select(x => x.ColumnName)
                             .ToArray();
                            string columns = string.Join(", ", columnNames);

                            foreach (DataRow row in dt.Rows)
                            {
                                string rows = "";
                                foreach (DataColumn col in dt.Columns)
                                {
                                    if (col.ToString().ToLower() != "id")
                                    {
                                        if (row[col].ToString().ToLower() == "true" || row[col].ToString().ToLower() == "false")
                                            rows += row[col] + ", ";
                                        else
                                        {

                                            if (row[col].ToString().Contains("'"))
                                            {
                                                string formatedRow = row[col].ToString().Replace("'", "\\'");
                                                rows += "'" + formatedRow + "'" + ", ";
                                            }
                                            else
                                                rows += "'" + row[col] + "'" + ", ";
                                        }

                                    }

                                }

                                string query = "Insert INTO " + table_name + " (" + columns + ") values (" + "default, " + rows.Remove(rows.Length - 2) + ")";
                                cmd = new MySqlCommand(query, cn.connection);
                                cmd.ExecuteNonQuery();

                            }
                            cn.close_connection();
                        }

                    }


                }
                catch (NullReferenceException ex)
                {
                    Console.Out.WriteLine("No run");
                }
            }
        }
    }
}