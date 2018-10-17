<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="IEDC_Home.aspx.cs" Inherits="IEF_Database.IEDC_Home" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>IEDC Database</title>
    <link href="css/jquery-ui.css" rel="stylesheet" />
    
    <link href="css/bootstrap.css" rel="stylesheet" />
    <link href="css/footer-distributed-with-address-and-phones.css" rel="stylesheet" />
    <link href="css/body.css" rel="stylesheet" />

    <script src="scripts/lb/jquery-3.1.1.min.js"></script>

    <!-- css -->

    <!-- JavaScriptLibrary -->
        <script src="scripts/lib/jquery-1.12.4.js"></script>
    <script src="scripts/lib/jquery-ui.js"></script>


    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>

      <script type="text/javascript" src="js/jquery-1.6.2.js"></script>
      <script type="text/javascript" src="js/jquery-ui.js"></script>
      <link rel="stylesheet" type="text/css" media="screen" href="css/redmond/jquery-ui-1.7.2.custom.css" />
     <link rel="stylesheet" type="text/css" media="screen" href="css/ui.jqgrid.css" />
      <script type="text/javascript" src="js/grid.locale-en.js"></script>
      <script type="text/javascript" src="js/jquery.jqGrid.min.js"></script>
    <script src="scripts/json2-min.js" type="text/javascript"></script>

    <script src="scripts/js_iedc_dataset.js"></script>

    <!-- JavaScriptLibrary -->
   
    <!-- CustomJavaScript -->

        <style>

        .col-md-8 {
            text-align:left;

        }

        .col-md-4 {
            padding-left:0px;
            /*background-color:#229922;*/

        }
         .col-md-10 {
            text-align: right;
            padding-bottom: 20px;

        }

.col-md-12 {
    float: left;
    padding: 0;
    background-color:none;
    padding-bottom: 20px;
}
.col-md-12 p a, p a:hover {
    color: darkgreen;
    font-weight:bold;
    font-size:22px;
    text-decoration: none;
}
.col-md-12 p span {
    color: lightgreen;
}

        .table {
    margin-bottom: 20px;
}
        /*gridview*/
.table table  tbody  tr  td a ,
.table table  tbody  tr  td  span {
position: relative;
float: left;
padding: 6px 12px;
margin-left: -1px;
line-height: 1.42857143;
color: #337ab7;
text-decoration: none;
background-color: #fff;
border: 1px solid #ddd;
}

.table table > tbody > tr > td > span {
z-index: 3;
color: #fff;
cursor: default;
background-color: #337ab7;
border-color: #337ab7;
}

.table table > tbody > tr > td:first-child > a,
.table table > tbody > tr > td:first-child > span {
margin-left: 0;
border-top-left-radius: 4px;
border-bottom-left-radius: 4px;
}

.table table > tbody > tr > td:last-child > a,
.table table > tbody > tr > td:last-child > span {
border-top-right-radius: 4px;
border-bottom-right-radius: 4px;
}

.table table > tbody > tr > td > a:hover,
.table   table > tbody > tr > td > span:hover,
.table table > tbody > tr > td > a:focus,
.table table > tbody > tr > td > span:focus {
z-index: 2;
color: #23527c;
background-color: #eee;
border-color: #ddd;
}
/*end gridview */
    </style>

    <style>
        .styled-dropdown {
            border:2px solid green;
            
            padding:3px;
            -webkit-appearance: none;
           
            background-position:88px;
            background-repeat:no-repeat;
            text-indent: 0.01px;/*In Firefox*/
            text-overflow: '';/*In Firefox*/
   }
 

.myCheckBoxList label 
{  
    padding-right: 10px; 
}
    </style>



</head>

<body>
    <form id="form1" runat="server">
    <div class="jumbotron">
          <div class="container-fluid">
    
                    <div class="col-md-2">
                        <img src="resources/IEF_Logo.png" style="padding-left:10px;" width="150px" height="150px" />
                    </div>
                    <div class="col-md-8" style="padding-left:30px;">
                        <h2>Industrial Ecology Freiburg</h2>
                        <p style="font-size:16px;">Research group at the Faculty of Environment and Natural Resources</p>
                    </div>
                    <div class="col-md-2">
                        <img src="resources/uni_freiburg.png" width="120px" height="150px"/>
                    </div>
                
  </div>
</div>

<nav class="navbar navbar-default navbar-custom navbar">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
          
                   <li><a href="http://www.industrialecology.uni-freiburg.de" target="_blank">Home</a></li>

                    
      </ul>
     
    </div>
  </div>
</nav>
    
<div class="container-fluid" >

     <div class="row">
       <div class= "col-md-12"  style="background-color:#c6ecd9">

   <h3>Welcome to the Industrial Ecology Data Commons prototype!</h3>   <br />
           This database contains more than 100 IE-related datasets from the literature, including stocks, flows, process descriptions, IO tables, material composition of products, and many more. 
<br />All data are structured according to a newly developed general data model for socioeconomic metabolism.    <br />

           Our mission is to show how data storage and exchange in sustainability science could look like in the future and to develop some of the building blocks of the required infrastructure.
              <br /><br />
           The database is open and documented in a public <a href="https://github.com/IndEcol/IE_data_commons" target="_blank">GitHub repository</a>. There is a short <a href="https://youtu.be/mYh427O8toA" target="_blank">video tutorial</a> on how to use the download interface, a <a href="https://youtu.be/1aCynUvSVRY" target="_blank"> video lecture </a> on the data model, and <a href="http://www.database.industrialecology.uni-freiburg.de/resources/DataModel_SEM_IEDC_FAQ.pdf" target="_blank">a glossary and FAQ list</a>. A journal publication on the data model is in preparation. A <a href="http://www.blog.industrialecology.uni-freiburg.de/index.php/2018/10/17/launching-the-prototype-for-an-industrial-ecology-data-inventory/" target="_blank">blog entry</a> on the vision and background behind the project is also available.
<br /><br />
We are interested in your feedback, bug reports, and critisicm, and also offer direct reading access to the database via SQL. Please send us an email to <u>in4mation*at*indecol.uni-freiburg.de</u>!
              <br />
           The search interface below allows you to browse the catalogue of datasets and to download the available data as spreadsheet.
<br /><br /> The following links point to the different lookup tables:
              <br />
&nbsp;&nbsp;&nbsp;   <a href="http://www.database.industrialecology.uni-freiburg.de/resources/IEDC_DataTypes_Overview.pdf" target="_blank">List of all data types</a><br />
&nbsp;&nbsp;&nbsp;   <a href="aspects.aspx" target="_blank">aspect and dimension tables</a><br />
&nbsp;&nbsp;&nbsp;   <a href="datatypes.aspx" target="_blank">categories, types, and layers tables</a>  <br />
&nbsp;&nbsp;&nbsp;   <a href="units.aspx" target="_blank">units table</a>  <br />
&nbsp;&nbsp;&nbsp;   <a href="uncertainty.aspx" target="_blank">stats_array table</a>  <br />
&nbsp;&nbsp;&nbsp;   <a href="provenance.aspx" target="_blank">provencance, sources, and licenses tables</a>  <br />
&nbsp;&nbsp;&nbsp;   <a href="classifications.aspx" target="_blank">classifications definition table and display of selected classification</a>  <br />
            
        
           </div>
       </div>
      <div class="row">
           <div class= "col-md-12"  >
            
               
            </div>
         </div>

    <div class="row">
       <div class= "col-md-12"  style="background-color:#c6ecd9">
           <h2>Data search and download:</h2>
           + Searching for data? Use keywords! <br />
           + Searching for a specific data type? Use the data type key, such as '1_F' or '3_MC', cf. <a href="http://www.database.industrialecology.uni-freiburg.de/resources/IEDC_DataTypes_Overview.pdf" target="_blank">the list of all data types</a>! <br />
+ Searching for data from a specific publication? Use main author name or DOI! If data source does not have a DOI, use keywords from report title and publishing institution! <br />

+ Searching for a specific dataset from the catalogue? Use the dataset name! <br /><br />
             <table class="table-responsive">
                   <tr>
                       <td align="right">Search Keywords:&nbsp;&nbsp; </td>
                       <td>
                           <asp:TextBox ID="txtSearch1" runat="server" class="form-control"  onkeyup="getCheckboxValues();"></asp:TextBox></td>

                       <td>
                           <asp:TextBox ID="txtSearch2" runat="server" class="form-control"  onkeyup="getCheckboxValues();"></asp:TextBox></td>

                       <td>
                           <asp:TextBox ID="txtSearch3" runat="server" class="form-control"  onkeyup="getCheckboxValues();"></asp:TextBox></td>
                       <td align="right">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search Tags: &nbsp;&nbsp;&nbsp; </td>
                       <td> 
                            <asp:CheckBoxList ID="cbDatasets" runat="server" onclick="getCheckboxValues();" CssClass="myCheckBoxList" RepeatLayout="table" RepeatColumns="5" RepeatDirection="vertical">
                                <asp:ListItem Value="dataset_name" Selected="True"> Dataset Name </asp:ListItem>
    <asp:ListItem Value="description" Selected="True"> Description </asp:ListItem>
    <asp:ListItem Value="keywords" Selected="True"> Keywords </asp:ListItem>
    <asp:ListItem Value="main_author" Selected="True"> Main Author </asp:ListItem>
    <asp:ListItem Value="project_report" Selected="True"> Source </asp:ListItem>
    <asp:ListItem Value="suggested_citation" Selected="True"> DOI </asp:ListItem>
</asp:CheckBoxList>
                       </td>
                   </tr>
         
               </table>

       
           </div>
       </div>
   
     <br />
      <div class="row">
             
                      <div class= "col-md-12"  style="background-color:#c6ecd9">

                           <h4>Catalogue of Data Sets</h4>
                           <table id="grid_iedc_dataset" class="scroll"></table>
        <div id="pager_iedc_dataset" class="scroll" style="text-align:center;"></div>
                         
        </div>
           </div>
      
           <div class="row" style="background-color:#c6ecd9">

          <div class= "col-md-6"  >

                           <h4>Description of the selected dataset: </h4>
                           <table id="grid_iedc_dataset_view" class="scroll"></table>
       
        </div>

           <div class= "col-md-6" >
               <h4>Description of the corresponding datagroup (if applicable): </h4>
                <table id="grid_iedc_datagroup" class="scroll"></table>
                 
        </div>
            <br /> <br /> 
                <h4>System definition of corresponding datagroup (if applicable):</h4>
          <div class="col-md-12" id ="system_definition">
                  <br />     
                   
        </div>

           <div class= "col-md-5"  style="background-color:#c6ecd9">
                <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td><h4>Download dataset in selected format</h4></td>
        

     <td>    <asp:DropDownList ID="drdDownload" runat="server"  class="form-control">
            <asp:ListItem Value="0">--SELECT--</asp:ListItem>
            <asp:ListItem Value="1">XLS</asp:ListItem>
            <asp:ListItem Value="1" Enabled="false">JSON</asp:ListItem>
            <asp:ListItem Value="1" Enabled="false">CSV</asp:ListItem>
            <asp:ListItem Value="1" Enabled="false">PY</asp:ListItem>
        </asp:DropDownList>     </td>
         <td> <asp:Button ID="btnSave" runat="server" Text="Download" Enable="True" class="btn btn-success" style="display: block; margin: 0 auto;" OnClick="btnSave_Click"></asp:Button></td>
     <td>&nbsp;</td>
        </tr>
 


  </tbody>
 </table>
                           
                           
       </div>
                          <br />
        </div>

               <div class= "col-md-7"  style="background-color:#c6ecd9">

                   </div>
     <div class="row">
           <div class= "col-md-12" >
               <asp:HiddenField ID="hdnDatasetId" runat="server" value="" />
                
          </div>
      </div>
</div>
<br/>
    <br /><br />

    </div>
        <footer class="footer-distributed">

            <div class="footer-left">

                <p class="footer-links">
                    <a href="http://www.blog.industrialecology.uni-freiburg.de">Blog</a>
                    .
                    <a href="http://www.blog.industrialecology.uni-freiburg.de">Research</a>
                    .
                    <a href="http://www.database.industrialecology.uni-freiburg.de">Database</a>
                    .
           <a href="http://www.visualisation.industrialecology.uni-freiburg.de">Visualisation</a>
                    .
                    <a href="http://www.teaching.industrialecology.uni-freiburg.de">Teaching</a>
                    .
            <a href="http://www.internal.industrialecology.uni-freiburg.de">Internal</a>

                </p>
            
            </div>
            
            <div class="footer-center">
                <div>

                    <h3>Industrial Ecology <span>Freiburg</span></h3>
                    <p>  &copy; 2017 Stefan Pauliuk &amp; Mahadi Hasan<br>
                        Sustainable Energy and Material Flow Management (Industrial Ecology) <br>
                        Faculty of Environment and Natural Resources <br>
                       
                           Tennenbacher Straße 4 <br>
                         D-79106 Freiburg <br>
                        Germany <br>
                        email: in4mation@indecol-freiburg.de <br>
                        </p>
                </div>

            </div>

            

        </footer>
    </form>
</body>
</html>