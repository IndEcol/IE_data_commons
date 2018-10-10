using System;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using System.Linq;
using System.Web;
using System.Web.UI.WebControls;
using System.Data;
using System.Collections;

namespace IEF_Database.cls
{

    public class clsDataHandling
    {
        dbConnect cn = new dbConnect();

        //string time = DateTime.Now.ToString("dd/MM/yyyy hh:mm:ss tt");
        string time = DateTime.Now.Year + "." + DateTime.Now.Month + "." + DateTime.Now.Day +
               " " + DateTime.Now.Hour + (":") + DateTime.Now.Minute + (":") + DateTime.Now.Second;

      

        public string createJobID(string user_name)
        {
            string job_id = "";
            string query = "select max(id)+1 as id from data_master";


            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();
                while (reader.Read())
                {
                    job_id = user_name + Convert.ToString(reader["id"]);
                }

                reader.Close();
                cn.close_connection();
            }

            return job_id;
        }

        public string DataSetName(string dataset_id)
        {
            string dataset_name = "";
            string query = "select distinct dataset_name from iedc.datasets where id = " + dataset_id + "";


            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();
                while (reader.Read())
                {
                    dataset_name = Convert.ToString(reader["dataset_name"]);
                }

                reader.Close();
                cn.close_connection();
            }

            return dataset_name;
        }

        


        public void datasetGridView(GridView gv)
        {
            //string query = "select * from sankey.dataset";
            string query = "SELECT System_ID SI, System_definition SD, Dataset_name DN, Reference_date RD, ";
            query += "Most_recent_update MRU, Corresponding_author_info CAI, Other_author_info OAI, ";
            query += "Document_reference DR, region R, Time_period_of_analysis TPA, Indicator_element IE  ";
            query += "FROM sankey.dataset";
             
            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }
        }

        public DataTable DataSet()
        {
            DataTable table = new DataTable();
            string query = "SELECT System_ID SI, System_definition SD, Dataset_name DN, Reference_date RD, ";
            query += "Most_recent_update MRU, Corresponding_author_info CAI, Other_author_info OAI, ";
            query += "Document_reference DR, region R, Time_period_of_analysis TPA, Indicator_element IE  ";
            query += "FROM sankey.dataset";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }



        public void processListGridView(GridView gv, string datasetId)
        {
            string query = "select * from sankey.process_list where system_id = "+ datasetId + "";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }
        }
        public DataTable stocksDataTable(string stock_id, string selectedYear, string selectedCountry)
        {
            DataTable table = new DataTable();
            string filter = "";

            string[] modifiedSelectedCountry = selectedCountry.Split(',');
            string mselectedCountry= "'" + string.Join("','", modifiedSelectedCountry) + "'";

            if (selectedYear == "" && selectedCountry=="")
            {
                filter = " ";
            }
            else if(selectedYear == "" && selectedCountry != "")
            {
                filter = "and countries.country_name in (" + mselectedCountry + ") ";
            }
            else if (selectedYear != "" && selectedCountry == "")
            {
                filter = "and stocks.year in(" + selectedYear + ") ";
            }
            else
            {
                filter = "and stocks.year in(" + selectedYear + ") and countries.country_name in (" + mselectedCountry + ") ";
            }

            string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN, stocks.process_id PID, proc.process_name PN, stocks.country_iso_code CIC, ";
            query += "countries.country_name C, stocks.year T, stocks.age_cohort AC, stocks.indicator_element IE,  stocks.aspect_of_dataset AD, stocks.value V, ";
            query += "stocks.error_type ET, stocks.error_value_1 EV1, stocks.error_value_2 EV2, stocks.data_quality DQ, stocks.unit_id UID, stocks.comment CM  ";
            query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            query += "where stocks.process_id = " + stock_id + " " + filter + " ";

            //string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN ";
            //query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            //query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            //query += "where stocks.process_id = 12 limit 5 ";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }

        public DataTable flowsDataTable(string source_flow_id, string target_flow_id, string selectedYear, string selectedCountry)
        {
            DataTable table = new DataTable();

            if (target_flow_id == null || target_flow_id == "")
                target_flow_id = "0";
            if (source_flow_id == null || source_flow_id == "")
                source_flow_id = "0";

            string filter = "";

            string[] modifiedSelectedCountry = selectedCountry.Split(',');
            string mselectedCountry = "'" + string.Join("','", modifiedSelectedCountry) + "'";
            string mselectedCountryISO = "";
            string query = "select c.ISO_code as ISO_code from sankey.countries c where c.country_name in ("+ mselectedCountry + ") ";
            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();
                int counter = 0;
                while (reader.Read())
                {
                    if (counter == 0)
                        mselectedCountryISO += Convert.ToString(reader["ISO_code"]);
                    else
                        mselectedCountryISO += "," + Convert.ToString(reader["ISO_code"]);

                    counter++;
                    //countries.Add(Convert.ToString(reader["ISO"]));
                    //countries.Add(Convert.ToString(reader["COUNTRY"]));
                    //countries.Add(new string[2] { Convert.ToString(reader["ISO"]), Convert.ToString(reader["COUNTRY"]) });
                }
                while (reader.Read())
                {
                    
                }

                reader.Close();
                cn.close_connection();
            }


            if (selectedYear == "" && mselectedCountryISO == "")
            {
                filter = " ";
            }
            else if (selectedYear == "" && mselectedCountryISO != "")
            {
                filter = "and (f.region_source in (" + mselectedCountryISO + ") or f.region_target in (" + mselectedCountryISO + "))";
            }
            else if (selectedYear != "" && mselectedCountryISO == "")
            {
                filter = "and f.year in(" + selectedYear + ") ";
            }
            else
            {
                filter = "and f.year in(" + selectedYear + ") and (f.region_source in (" + mselectedCountryISO + ") or f.region_target in (" + mselectedCountryISO + ")) ";
            }

            //string query = "select distinct f.system_id SI, f.flow_dataset_number FDN, f.process_id_source PIDS, p.process_name PNS, f.process_id_target PIDT, p.process_name PNT, ";
            //query += "f.region_source CICS, c.country_name CS, f.region_target CICT, c.country_name CT, f.year T, f.age_cohort AC, f.material IE, f.value V, ";
            //query += "f.error_type ET, f.error_value_1 EV1, f.error_value_2 EV2, f.data_quality DQ, f.unit UID, f.comment CM  ";
            //query += "from sankey.flows f inner join sankey.process_list p on f.process_id_source = p.process_id inner join sankey.countries c ";
            //query += "on f.region_source = c.ISO_code where f.process_id_source = " + source_flow_id + " and f.process_id_target = " + target_flow_id + " ";
            //query += " order by f.flow_dataset_number ";

            string query2 = "SELECT distinct f.system_id SI, f.flow_dataset_number FDN, f.process_id_source PIDS, (select p.process_name from sankey.process_list p where p.process_id = "+ source_flow_id + ") as PNS, ";
            query2 += "f.process_id_target PIDT, (select p.process_name from sankey.process_list p where p.process_id = " + target_flow_id + ") as PNT, f.region_source CICS, c.country_name CS, f.region_target CICT, ";
            query2 += "c.country_name CT, f.year T, f.age_cohort AC, f.material IE, f.value V, f.error_type ET, f.error_value_1 EV1, f.error_value_2 EV2, f.data_quality DQ, f.unit UID, f.comment CM ";
            query2 += "FROM sankey.flows f inner join sankey.countries c on (f.region_source = c.ISO_code or f.region_target = c.ISO_code) ";
            query2 += "where f.process_id_source = " + source_flow_id + " and f.process_id_target = " + target_flow_id + " "+ filter + " ";

           

  



            //string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN ";
            //query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            //query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            //query += "where stocks.process_id = 12 limit 5 ";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query2, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query2, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }

        public DataTable flowCycleDataTable(string selectedYear, string selectedCountry)
        {
            DataTable table = new DataTable();
            string filter = "";

            //string[] modifiedSelectedCountry = selectedCountry.Split(',');
            //string mselectedCountry = "'" + string.Join("','", modifiedSelectedCountry) + "'";
            //string mselectedCountryISO = "";
            //string query = "select GROUP_CONCAT(c.ISO_code) as ISO_code from sankey.countries c where c.country_name in (" + mselectedCountry + ") ";
            //if (cn.open_connection() == true)
            //{
            //    MySqlCommand cmd = new MySqlCommand(query, cn.connection);
            //    MySqlDataReader reader = cmd.ExecuteReader();
            //    while (reader.Read())
            //    {
            //        mselectedCountryISO = Convert.ToString(reader["ISO_code"]);
            //    }

            //    reader.Close();
            //    cn.close_connection();
            //}


            if (selectedYear == "" && selectedCountry == "")
            {
                filter = " ";
            }
            else if (selectedYear == "" && selectedCountry != "")
            {
                filter = "where (f.region_source in (" + selectedCountry + ") or f.region_target in (" + selectedCountry + "))";
            }
            else if (selectedYear != "" && selectedCountry == "")
            {
                filter = "where f.year in(" + selectedYear + ") ";
            }
            else
            {
                filter = "where f.year in(" + selectedYear + ") and (f.region_source in (" + selectedCountry + ") or f.region_target in (" + selectedCountry + ")) ";
            }

            string query2 = "SELECT distinct f.system_id SI, f.flow_dataset_number FDN, f.process_id_source PIDS, (select p.process_name from sankey.process_list p where p.process_id = PIDS) as PNS, ";
            query2 += "f.process_id_target PIDT, (select p.process_name from sankey.process_list p where p.process_id = PIDT) as PNT, f.region_source CICS, c.country_name CS, f.region_target CICT, ";
            query2 += "c.country_name CT, f.year T, f.age_cohort AC, f.material IE, f.value V, f.error_type ET, f.error_value_1 EV1, f.error_value_2 EV2, f.data_quality DQ, f.unit UID, f.comment CM ";
            query2 += "FROM sankey.flows f inner join sankey.countries c on(f.region_source = c.ISO_code or f.region_target = c.ISO_code) ";
            query2 += "  " + filter + " ";







            //string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN ";
            //query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            //query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            //query += "where stocks.process_id = 12 limit 5 ";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query2, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query2, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }

        public DataTable stockProcessList(string datasetId)
        {
            DataTable table = new DataTable();
            string query = "select distinct p.process_id, p.process_name from sankey.process_list p inner join sankey.stocks s where p.process_id=s.process_id and p.system_id = " + datasetId + "";

            //string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN ";
            //query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            //query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            //query += "where stocks.process_id = 12 limit 5 ";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }
        
        public DataTable sourceFLowList(string datasetId)
        {
            DataTable table = new DataTable();
            //string query = "select process_id, process_name from sankey.process_list where system_id = " + datasetId + "";
             ;
            string query = "select distinct p.process_id, p.process_name from sankey.process_list p inner join sankey.flows f ";
            query += "where p.process_id = f.process_id_source and p.system_id = " + datasetId + "";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }
        public DataTable targetFLowList(string datasetId, string source_flow)
        {
            DataTable table = new DataTable();

            string query = "select distinct p.process_id, p.process_name from sankey.flows f, sankey.process_list p ";
            query += "where p.process_id = f.process_id_target and process_id_source = " + source_flow + " and p.system_id = " + datasetId + "";


            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }
        public void processListDropDown(DropDownList dp, string datasetId)
        {
            string query = "select * from sankey.process_list where system_id = " + datasetId + "";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);

                dp.DataSource = ds;
                dp.DataTextField = "process_name";
                dp.DataValueField = "process_id";
                dp.DataBind();

                cn.close_connection();
            }
        }

        public void stocksGridView(GridView gv, string processId, string param)
        {
            //string query = "select * from sankey.stocks where process_id = " + processId + "";
                                                 
            string query = "select stocks.system_id SI, stocks.stock_dataset_number SDN, proc.process_name PN, ";
            query += "countries.country_name C, stocks.year T, stocks.indicator_element IE, ";
            query += "stocks.aspect_of_dataset AD, stocks.value V, stocks.unit_id UID  ";
            query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
            query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
            query += "where stocks.process_id = " + processId + " and " + param + "";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }
        }


        public DataSet stocksDataSet(string processId, string param)
        {
            //string query = "select * from sankey.stocks where process_id = " + processId + "";
            string query = "";
            if (param == "")
            {
                query = "select stocks.system_id SI, stocks.stock_dataset_number SDN, proc.process_name PN, ";
                query += "countries.country_name C, stocks.year T, stocks.indicator_element IE, ";
                query += "stocks.aspect_of_dataset AD, stocks.value V, stocks.unit_id UID  ";
                query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
                query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
                query += "where stocks.process_id = " + processId + "";
            }
            else
            {
                query = "select stocks.system_id SI, stocks.stock_dataset_number SDN, proc.process_name PN, ";
                query += "countries.country_name C, stocks.year T, stocks.indicator_element IE, ";
                query += "stocks.aspect_of_dataset AD, stocks.value V, stocks.unit_id UID  ";
                query += "from sankey.stocks stocks  inner join sankey.process_list proc ";
                query += "on stocks.process_id = proc.process_id inner join sankey.countries on stocks.country_iso_code = countries.ISO_code ";
                query += "where stocks.process_id = " + processId + " and " + param + "";
            }

            DataSet ds = new DataSet();
           

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);
           
                adapter.Fill(ds);

                cn.close_connection();
            }

            return ds;
        }

        public void flowsGridView(GridView gv, string processSourceId, string processTargetId)
        {
            string query = "select * from sankey.flows_base where process_id_origin = " + processSourceId + " and process_id_destination = " + processTargetId + " ";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }
        }

        public void getYear(HiddenField hdn)
        {
            string query = "select distinct stocks.year YEAR ";
            query += "from sankey.stocks stocks ";
            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();
                string years = "";
                int counter = 0;
                while (reader.Read())
                {
                    if (counter == 0)
                        years += Convert.ToString(reader["YEAR"]);
                    else
                        years += "|||" + Convert.ToString(reader["YEAR"]);

                    counter++;
                    //countries.Add(Convert.ToString(reader["ISO"]));
                    //countries.Add(Convert.ToString(reader["COUNTRY"]));
                    //countries.Add(new string[2] { Convert.ToString(reader["ISO"]), Convert.ToString(reader["COUNTRY"]) });
                }
                hdn.Value =years;

                reader.Close();
                cn.close_connection();
            }
        }


        public DataTable CycleYear(string datasetId)
        {
            DataTable table = new DataTable();

            string query = "select distinct f.year as year, f.year as year from sankey.flows f where f.system_id= "+ datasetId + "";


            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }

        public DataTable CycleCountry(string datasetId, string selected_year)
        {
            DataTable table = new DataTable();

            string query = "select distinct c.ISO_code ISO, c.country_name COUNTRY from sankey.flows f, sankey.countries c ";
            query += "where (f.region_source = c.ISO_code or f.region_target = c.ISO_code) and f.year = " + selected_year + " and f.system_id = " + datasetId + "";


            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            return table;
        }

        public void getCountry(HiddenField hdn)
        {
            //string query = "select GROUP_CONCAT(distinct countries.country_name) COUNTRY ";
            //query += "from sankey.stocks stocks ";
            //query += "inner join sankey.process_list proc on stocks.process_id = proc.process_id inner join sankey.countries countries on stocks.country_iso_code= countries.ISO_code ";
            //query += "where stocks.process_id = 12 ";
            
                                                                
            string query = "select distinct c.ISO_code ISO, c.country_name COUNTRY from sankey.countries c inner ";
            query += "join sankey.stocks s on c.ISO_code = s.country_iso_code ";
            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();

                //List<string[]> countries = new List<string[]>();
                //ArrayList countries = new ArrayList();
                string countries = "";
                while (reader.Read())
                {
                    countries += Convert.ToString(reader["ISO"]) + "::" + Convert.ToString(reader["COUNTRY"]) + "|||";
                    //countries.Add(Convert.ToString(reader["ISO"]));
                    //countries.Add(Convert.ToString(reader["COUNTRY"]));
                    //countries.Add(new string[2] { Convert.ToString(reader["ISO"]), Convert.ToString(reader["COUNTRY"]) });
                }

                hdn.Value = countries;

                reader.Close();
                cn.close_connection();
            }
        }
        public DataTable getData()
        {
            //string connection_string = cn.connection_string;
            //string query = "select Id, UnitCode, UnitName from unit ;";
            //SqlDataAdapter adapter = new SqlDataAdapter(query, cn.sqlCn);
            //DataTable dt = new DataTable();
            //adapter.Fill(dt);
            DataTable dt = new DataTable();
            dt.Columns.Add("id", typeof(int));
            dt.Columns.Add("UnitCode", typeof(string));
            dt.Columns.Add("UnitName", typeof(string));

            // Here we add five DataRows.
            dt.Rows.Add(1, "kg", "David");
            dt.Rows.Add(2, "m", "Sam");
            dt.Rows.Add(3, "cm", "Christoff");
            dt.Rows.Add(4, "km", "Janet");
            dt.Rows.Add(5, "p", "Melanie");

            return dt;
        }

        public string SetSearchStr(string oper, string fld, string search)
        {
            string str = "";
            switch (oper)
            {
                case "eq":
                    str = fld + "='" + search + "'";
                    break;
                case "ne":
                    str = fld + "<>'" + search + "'";
                    break;
                case "bw":
                    str = fld + " like '" + search + "%'";
                    break;
                case "bn":
                    str = fld + " NOT like '" + search + "%'";
                    break;
                case "ew":
                    str = fld + " like '%" + search + "'";
                    break;
                case "en":
                    str = fld + " NOT like '%" + search + "'";
                    break;
                case "cn":
                    str = fld + " like '%" + search + "%'";
                    break;
                case "nc":
                    str = fld + " NOT like '%" + search + "%'";
                    break;
                default:
                    str = "";
                    break;
            }
            return str;
        }


        public void showClassificationGrid(GridView gv)
        {
            string query = "SELECT * FROM iedc.classification_definition";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }

        }

        public void showAspectsGrid(GridView gv)
        {
            string query = "SELECT * FROM iedc.aspects";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }

        }

        public void listTables(DropDownList dp)
        {
            string query = "SELECT table_name FROM information_schema.tables where table_schema='iedc';";

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);

                dp.DataSource = ds;
                dp.DataTextField = "table_name";
                dp.DataValueField = "table_name";
                dp.DataBind();

                cn.close_connection();
            }
        }

        public void dataGrid(GridView gv, string query)
        {

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);
                gv.DataSource = ds;
                gv.DataBind();

                cn.close_connection();
            }

        }

        //SELECT id, dataset_name, dataset_version, datagroup_id, data_category, data_type, data_layer, process_scope, process_resolution, product_scope, product_resolution, material_scope,
        //material_resolution, regional_scope, regional_resolution, temporal_scope, temporal_resolution, description, keywords, data_provenance, dataset_size, comment, aspect_1, aspect_1_classification,
        //aspect_2, aspect_2_classification, aspect_3, aspect_3_classification, aspect_4, aspect_4_classification, aspect_5, aspect_5_classification, aspect_6, aspect_6_classification, aspect_7,
        //aspect_7_classification, aspect_8, aspect_8_classification, aspect_9, aspect_9_classification, aspect_10, aspect_10_classification, aspect_11, aspect_11_classification, aspect_12,
        //aspect_12_classification, tupel_notation, semantic_string_example, semantic_string_general, type_of_source, project_license, main_author, dataset_link, dataset_format, project_report,
        //suggested_citation, visible, access_date, submission_date, submitting_user, dataset_conversion_info, review_date, review_user, review_comment, reserve1, reserve2, reserve3, reserve4, reserve5
        // FROM iedc.datasets;

        public DataTable IEDC_DataSet(string selectedItems, string searchText)
        {
            string[] selectedItemsList = new string[6];
            string filter = "";
            string query = "";
            
            if (selectedItems == "")
            {
                selectedItemsList[0] = "dataset_name";
                selectedItemsList[1] = "keywords";
                selectedItemsList[2] = "main_author";
                selectedItemsList[3] = "project_report";
                selectedItemsList[4] = "suggested_citation";
                selectedItemsList[5] = "description";
            }
            else
                selectedItemsList = selectedItems.Split(',');

            if (searchText == "")
            {
                query = "SELECT id, dataset_name DN,  ";
                query += "description DS, keywords KW, ";
                query += "main_author MA, datagroup_id DG, suggested_citation SC  ";
                query += "FROM iedc.datasets";
            }
            else
            {
                for (int i = 0; i < selectedItemsList.Length; i++)
                {
                    //filter += "" + selectedItemsList[i] + " like '%" + searchText + "%' || ";
                    filter += "" + selectedItemsList[i] + " REGEXP '" + searchText + "' || ";
                }
                string mod_filter = filter.Remove(filter.Length - 4);

                query = "SELECT id, dataset_name DN,  ";
                query += "description DS, keywords KW, ";
                query += "main_author MA, datagroup_id DG, suggested_citation SC  ";
                query += "FROM iedc.datasets where " + mod_filter + "";
            }
            DataTable table = new DataTable();          

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }
            //DataTable transposedTable = GenerateTransposedTable(table);
            return table;
        }


        public DataTable IEDC_DataGroupView(string datasetId)
        {
            //string query = "select * from iedc.datasets where id = '" + datasetId + "'";

            //string query = "SELECT distinct dg.* FROM iedc.datagroups dg inner join iedc.datasets ds where ds.datagroup_id=dg.id and ds.id = '" + datasetId + "' ";

            string query = "SELECT distinct dg.id, dg.datagroup_name, dg.datagroup_version, dg.project_id, dg.data_categories, dg.data_types, dg.data_layers, ";
            query += "dg.process_scope, dg.process_resolution, dg.product_scope, dg.product_resolution, dg.material_scope, dg.material_resolution, dg.regional_scope, ";
            query += "dg.regional_resolution, dg.temporal_scope, dg.temporal_resolution, dg.description, dg.keywords, dg.system_definition_picture, dg.comment, st.name as source_name, l.name ";

            query += "as license_name, dg.main_author, dg.project_link, dg.project_report, dg.suggested_citation, dg.submission_date, u.name as submitting_user, dg.reserve1, dg.reserve2, dg.reserve3 ";

            query += "FROM iedc.datagroups dg inner join iedc.datasets ds on dg.id = ds.datagroup_id left join iedc.users u on dg.submitting_user = u.id ";
            query += "left join iedc.source_type st on dg.type_of_source = st.id left join iedc.licences l on dg.project_license = l.id where ds.id = '" + datasetId + "' ";

            DataTable table = new DataTable();

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }
            if ((table == null) || (table.Rows.Count == 0))
            {
                DataRow newBlankRow1 = table.NewRow();
                table.Rows.Add(newBlankRow1);
                return table;
            }
            else
            {
                DataTable transposedTable = GenerateTransposedTable(table);
                return transposedTable;              
            }
               
        }
        public DataTable IEDC_DataSetView(string datasetId)
        {
            //string query = "select * from iedc.datasets where id = '" + datasetId + "'";

            //  string query = "select distinct datasets.id, datasets.dataset_name, datasets.dataset_version, datasets.datagroup_id, categories.name as category, types.name type, layers.name layer, ";
            //query += "datasets.process_scope, datasets.process_resolution, datasets.product_scope, datasets.product_resolution, datasets.material_scope, datasets.material_resolution, ";
            //query += "datasets.regional_scope, datasets.regional_resolution, datasets.temporal_scope, datasets.temporal_resolution, datasets.description, datasets.keywords, provenance.name as provenance, ";
            //query += "datasets.dataset_size, datasets.comment, aspects.aspect as aspect1_name, datasets.aspect_1_classification, datasets.aspect_2, datasets.aspect_2_classification, ";
            //query += "datasets.aspect_3, datasets.aspect_3_classification, datasets.aspect_4, datasets.aspect_4_classification, datasets.aspect_5, datasets.aspect_5_classification, ";
            //query += "datasets.aspect_6, datasets.aspect_6_classification, datasets.aspect_7, datasets.aspect_7_classification, datasets.aspect_8, datasets.aspect_8_classification, ";
            //query += "datasets.aspect_9, datasets.aspect_9_classification,datasets.aspect_10, datasets.aspect_10_classification, datasets.aspect_11, datasets.aspect_11_classification, ";
            //query += "datasets.aspect_12, datasets.aspect_12_classification, datasets.tupel_notation, datasets.semantic_string_example, datasets.semantic_string_general, source_type.name source, ";
            //query += "licences.name license, datasets.main_author, datasets.dataset_link, datasets.dataset_format, datasets.project_report, datasets.suggested_citation, datasets.visible, datasets.access_date, ";
            //query += "datasets.submission_date, users.name as Submitting_User, datasets.dataset_conversion_info, datasets.review_date, users.name as Review_User, datasets.review_comment, ";
            //query += "datasets.reserve1, datasets.reserve2, datasets.reserve3, datasets.reserve4, datasets.reserve5 from datasets inner join categories on datasets.data_category = categories.id ";
            //query += "inner join types on datasets.data_type = types.id inner join layers on datasets.data_layer = layers.id inner join provenance on datasets.data_provenance = provenance.id inner join ";
            //query += "source_type on datasets.type_of_source = source_type.id inner join licences on datasets.project_license = licences.id inner join users on datasets.submitting_user = users.id ";
            //query += "inner join aspects on datasets.aspect_1 = aspects.id ";
            //query += "where datasets.id = '" + datasetId + "'";


            string query = "select distinct d.id, d.dataset_name, d.dataset_version, d.datagroup_id, c.name as category, t.name as type, l.name as layer, d.process_scope, d.process_resolution, ";
            query += "d.product_scope, d.product_resolution, d.material_scope, d.material_resolution, d.regional_scope, d.regional_resolution, d.temporal_scope, d.temporal_resolution, d.description, ";
            query += "d.keywords, p.name as provenance, d.dataset_size, d.comment, a1.aspect as aspect1_name, cd1.classification_name as classification_name1, a2.aspect as aspect2_name, ";
            query += "cd2.classification_name as classification_name2, a3.aspect as aspect3_name, cd3.classification_name as classification_name3, a4.aspect as aspect4_name, ";
            query += "cd4.classification_name as classification_name4, a5.aspect as aspect5_name, cd5.classification_name as classification_name5, a6.aspect as aspect6_name, ";
            query += "cd6.classification_name as classification_name6, a7.aspect as aspect7_name, cd7.classification_name as classification_name7, a8.aspect as aspect8_name, cd8.classification_name ";
            query += "as classification_name8, a9.aspect as aspect9_name, cd9.classification_name as classification_name9, a10.aspect as aspect10_name, cd10.classification_name as classification_name10, ";
            query += "a11.aspect as aspect11_name, cd11.classification_name as classification_name11, a12.aspect as aspect12_name, cd12.classification_name as classification_name12, d.tupel_notation, ";     
            query += "d.semantic_string_example, d.semantic_string_general, st.name source, licences.name license, d.main_author, d.dataset_link, d.dataset_format, d.project_report, d.suggested_citation, ";
            query += "d.visible, d.access_date, d.submission_date, u1.name as Submitting_User, d.dataset_conversion_info, d.review_date, u2.name as Review_User, d.review_comment, d.reserve1, ";
            query += "d.reserve2, d.reserve3, d.reserve4, d.reserve5 from iedc.datasets d left join iedc.categories c on d.data_category = c.id left join iedc.types t on d.data_type = t.id left join ";
            query += "iedc.layers l on d.data_layer = l.id left join iedc.provenance p on d.data_provenance = p.id left join iedc.source_type st on d.type_of_source = st.id left join iedc.licences on ";
            query += "d.project_license = licences.id left join iedc.users u1 on d.submitting_user = u1.id left join iedc.users u2 on d.review_user = u2.id left join iedc.aspects a1 on d.aspect_1 = a1.id ";
            query += "left join iedc.aspects a2 on d.aspect_2 = a2.id left join iedc.aspects a3 on d.aspect_3 = a3.id left join iedc.aspects a4 on d.aspect_4 = a4.id ";
            query += "left join iedc.aspects a5 on d.aspect_5 = a5.id left join iedc.aspects a6 on d.aspect_6 = a6.id left join iedc.aspects a7 on d.aspect_7 = a7.id ";
            query += "left join iedc.aspects a8 on d.aspect_8 = a8.id left join iedc.aspects a9 on d.aspect_9 = a9.id left join iedc.aspects a10 on d.aspect_10 = a10.id ";
            query += "left join iedc.aspects a11 on d.aspect_11 = a11.id left join iedc.aspects a12 on d.aspect_12 = a12.id left join iedc.classification_definition cd1 on d.aspect_1_classification = cd1.id ";
            query += "left join iedc.classification_definition cd2 on d.aspect_2_classification = cd2.id left join iedc.classification_definition cd3 on d.aspect_3_classification = cd3.id ";
            query += "left join iedc.classification_definition cd4 on d.aspect_4_classification = cd4.id left join iedc.classification_definition cd5 on d.aspect_5_classification = cd5.id ";
            query += "left join iedc.classification_definition cd6 on d.aspect_6_classification = cd6.id left join iedc.classification_definition cd7 on d.aspect_7_classification = cd7.id ";
            query += "left join iedc.classification_definition cd8 on d.aspect_8_classification = cd8.id left join iedc.classification_definition cd9 on d.aspect_9_classification = cd9.id ";
            query += "left join iedc.classification_definition cd10 on d.aspect_10_classification = cd10.id left join iedc.classification_definition cd11 on d.aspect_11_classification = cd11.id ";
            query += "left join iedc.classification_definition cd12 on d.aspect_12_classification = cd12.id where d.id = '" + datasetId + "'";


            DataTable table = new DataTable();

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }
            DataTable transposedTable = GenerateTransposedTable(table);
            return transposedTable;
        }
        
        private DataTable GenerateTransposedTable(DataTable inputTable)
        {
            DataTable outputTable = new DataTable();

            // Add columns by looping rows

            // Header row's first column is same as in inputTable
            outputTable.Columns.Add(inputTable.Columns[0].ColumnName.ToString());

            // Header row's second column onwards, 'inputTable's first column taken
            foreach (DataRow inRow in inputTable.Rows)
            {
                string newColName = inRow[0].ToString();
                outputTable.Columns.Add(newColName);
            }

            // Add rows by looping columns        
            for (int rCount = 1; rCount <= inputTable.Columns.Count - 1; rCount++)
            {
                DataRow newRow = outputTable.NewRow();

                // First column is inputTable's Header row's second column
                newRow[0] = inputTable.Columns[rCount].ColumnName.ToString();
                for (int cCount = 0; cCount <= inputTable.Rows.Count - 1; cCount++)
                {
                    string colValue = inputTable.Rows[cCount][rCount].ToString();
                    newRow[cCount + 1] = colValue;
                }
                outputTable.Rows.Add(newRow);
            }

            return outputTable;
        }

        public DataTable IEDC_DataTable(string datasetId)
        {

            //string query = "select * from iedc.data where dataset_id = '" + datasetId + "'";

            ArrayList colNames = AspectNames(datasetId);

            string query = "select d.id, ds.dataset_name, ci1.attribute1_oto as aspect_1, ci2.attribute1_oto as aspect_2, ci3.attribute1_oto as aspect_3, ci4.attribute1_oto as aspect_4, ";
            query += "ci5.attribute1_oto as aspect_5, ci6.attribute1_oto as aspect_6, ci7.attribute1_oto as aspect_7, ci8.attribute1_oto as aspect_8, ci9.attribute1_oto as aspect_9, ci10.attribute1_oto as aspect_10, ";
            query += "ci11.attribute1_oto as aspect_11, ci12.attribute1_oto as aspect_12, d.value, u1.unitcode, u2.unitcode, sa1.name as stats_array_1, sa2.name as stats_array_2, sa3.name as stats_array_3, ";

            query += "sa4.name as stats_array_4, d.comment, d.reserve1, d.reserve2, d.reserve3 from iedc.data d ";
            query += "left join iedc.stats_array sa1 on d.stats_array_1 = sa1.id left join iedc.stats_array sa2 on d.stats_array_2 = sa2.id ";
            query += "left join iedc.stats_array sa3 on d.stats_array_3 = sa3.id left join iedc.stats_array sa4 on d.stats_array_4 = sa4.id ";
            query += "left join iedc.units u1 on d.unit_nominator = u1.id left join iedc.units u2 on d.unit_denominator = u2.id ";

            query += "left join iedc.classification_items ci1 on d.aspect1 = ci1.id left join iedc.classification_items ci2 on d.aspect2 = ci2.id left join iedc.classification_items ci3 on d.aspect3 = ci3.id ";
            query += "left join iedc.classification_items ci4 on d.aspect4 = ci4.id left join iedc.classification_items ci5 on d.aspect5 = ci5.id left join iedc.classification_items ci6 on d.aspect6 = ci6.id ";
            query += "left join iedc.classification_items ci7 on d.aspect7 = ci7.id left join iedc.classification_items ci8 on d.aspect8 = ci8.id left join iedc.classification_items ci9 on d.aspect9 = ci9.id ";
            query += "left join iedc.classification_items ci10 on d.aspect10 = ci10.id left join iedc.classification_items ci11 on d.aspect11 = ci11.id left join iedc.classification_items ci12 on d.aspect12 = ci12.id ";

            query += " inner join iedc.datasets ds on d.dataset_id = ds.id where d.dataset_id = '" + datasetId + "'";



            DataTable table = new DataTable();

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(table);
                cn.close_connection();
            }

            for (int i = 0; i < colNames.Count; i++)
            {
                table.Columns["aspect_" + (i + 1) + ""].ColumnName = colNames[i].ToString();
            }

            //table.Columns["aspect_1"].ColumnName = colNames[0].ToString();
            //table.Columns["aspect_2"].ColumnName = colNames[1].ToString();
            //table.Columns["aspect_3"].ColumnName = colNames[2].ToString();
            //table.Columns["aspect_4"].ColumnName = colNames[3].ToString();
            //table.Columns["aspect_5"].ColumnName = colNames[4].ToString();
            //table.Columns["aspect_6"].ColumnName = colNames[5].ToString();
            //table.Columns["aspect_7"].ColumnName = colNames[6].ToString();
            //table.Columns["aspect_8"].ColumnName = colNames[7].ToString();
            //table.Columns["aspect_9"].ColumnName = colNames[8].ToString();
            //table.Columns["aspect_10"].ColumnName = colNames[9].ToString();
            //table.Columns["aspect_11"].ColumnName = colNames[10].ToString();
            //table.Columns["aspect_12"].ColumnName = colNames[11].ToString();

            return table;
        }


        public ArrayList AspectNames(string datasetId)
        {

            //string query = "select * from iedc.data where dataset_id = '" + datasetId + "'";

            string query = "SELECT CONCAT('aspect 1 : ', a1.aspect) AS aspect1, CONCAT('aspect 2 : ', a2.aspect) AS aspect2, CONCAT('aspect 3 : ', a3.aspect) AS aspect3, CONCAT('aspect 4 : ', a4.aspect) AS aspect4, ";
            query += "CONCAT('aspect 5 : ', a5.aspect) AS aspect5, CONCAT('aspect 6 : ', a6.aspect) AS aspect6, CONCAT('aspect 7 : ', a7.aspect) AS aspect7, CONCAT('aspect 8 : ', a8.aspect) AS aspect8, ";
            query += "CONCAT('aspect 9 : ', a9.aspect) AS aspect9, CONCAT('aspect 10 : ', a10.aspect) AS aspect10, CONCAT('aspect 11 : ', a11.aspect) AS aspect11, CONCAT('aspect 12 : ', a12.aspect) AS aspect12 ";
            query += "FROM iedc.datasets ds left join iedc.aspects a1 on ds.aspect_1= a1.id left join iedc.aspects a2 on ds.aspect_2= a2.id left join iedc.aspects a3 on ds.aspect_3= a3.id ";
            query += "left join iedc.aspects a4 on ds.aspect_4= a4.id left join iedc.aspects a5 on ds.aspect_5= a5.id left join iedc.aspects a6 on ds.aspect_6= a6.id left join iedc.aspects a7 on ds.aspect_7= a7.id ";
            query += "left join iedc.aspects a8 on ds.aspect_8= a8.id left join iedc.aspects a9 on ds.aspect_9= a9.id left join iedc.aspects a10 on ds.aspect_10= a10.id left join iedc.aspects a11 on ds.aspect_11= a11.id ";
            query += "left join iedc.aspects a12 on ds.aspect_12= a12.id where ds.id = '" + datasetId + "'";

            ArrayList aspectNames = new ArrayList();

            DataTable table = new DataTable();

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataReader reader = cmd.ExecuteReader();
                while (reader.Read())
                {
                    for (int i =0; i<reader.FieldCount;i++)
                    {
                        if (Convert.ToString(reader[i]) == "")
                            aspectNames.Add(Convert.ToString("aspect " + (i+1) + " : "));
                        else
                            aspectNames.Add(Convert.ToString(reader[i]));
                    }                  
                }

                reader.Close();
                cn.close_connection();
            }

            return aspectNames;
        }
        

        public void dropdown(DropDownList dp, string query)
        {

            if (cn.open_connection() == true)
            {
                MySqlCommand cmd = new MySqlCommand(query, cn.connection);
                MySqlDataAdapter adapter = new MySqlDataAdapter(query, cn.connection);

                DataSet ds = new DataSet();
                adapter.Fill(ds);

                dp.DataSource = ds;
                dp.DataTextField = "classification_Name";
                dp.DataValueField = "id";
                dp.DataBind();

                cn.close_connection();
            }
        }
    }
}