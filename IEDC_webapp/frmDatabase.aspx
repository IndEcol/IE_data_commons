​
​​
​<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="frmDatabase.aspx.cs" Inherits="IEF_Database.frmDatabase" EnableEventValidation="false" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>IEF Database</title>
    <link href="css/jquery-ui.css" rel="stylesheet" />
    
    <link href="css/bootstrap.css" rel="stylesheet" />
    <link href="css/footer-distributed-with-address-and-phones.css" rel="stylesheet" />
    <link href="css/body.css" rel="stylesheet" />

    <script src="scripts/lb/jquery-3.1.1.min.js"></script>
    <script src="scripts/lb/inputTags.jquery.js"></script>
    <script src="scripts/tag_app.js"></script>
    <link href="css/inputTags.css" rel="stylesheet" />
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
    <%--<script src="scripts/js_DataSetJQGrid.js"></script>--%>
    <script src="scripts/js_dataset_grid.js"></script>
    <%--<script src="scripts/jsGrid.js"></script>--%>
    <script src="scripts/js_stocks_grid.js"></script>
    <script src="scripts/js_flows_grid.js"></script>
    <script src="scripts/js_flow_cycle_grid.js"></script>
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
 
    </style>

<style>

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
        <div class= "col-md-12">
            <p><a href="#">IEF Database</a></p>
            A short video tutorial is available on
            <a href="https://www.youtube.com/watch?v=TPJM1lHhrSQ" target="_blank">Youtube</a><br />
                        All data on this website are made available under a CC BY-NC 4.0 license.
            </div>


       </div>
      <div class="row">
             
                      <div class= "col-md-12"  style="background-color:#b3ffcc">

                           <h3>Catalogue of Data Sets</h3>
                           <table id="grid_dataset" class="scroll"></table>
        <div id="pager_dataset" class="scroll" style="text-align:center;"></div>
                          <br />
        </div>
               <br />
           <br />
          <h4>System definition of selected dataset</h4>
          <div class="col-md-12" id ="system_definition">
                  <br />     
                    </div>
           </div>
     <div class="row">
           <br />
                           <div class= "col-md-12" style="background-color:#ccffdd" >
                                <h3>Processes with stocks</h3>
        <table class="table table-responsive">
   
    <tbody>
       
      <tr>

          <td style="width:40%">Choose Stock Process</td>
        <td style="width:30%">
             <asp:DropDownList ID="drp_stock_process" runat="server" CssClass="form-control" Width="80%">
                                                                            </asp:DropDownList>
                                                                            <asp:RequiredFieldValidator ID="rfv_stock_process" runat="server"
                                                                                ControlToValidate="drp_stock_process" ErrorMessage="Please select Process Name"
                                                                                InitialValue="Process Name" SetFocusOnError="True" CssClass="form-control" Width="80%"></asp:RequiredFieldValidator>
        </td>
     <td style="width:30%"></td>
        
      </tr>
         
    </tbody>
  </table>
        
                          <h4>Filter by<span class="color"> Year and Region </span></h4>

                          <table class="table table-responsive">
   
    <tbody>
      <tr>

        <td> <input type="text" id="stock_year" value="" />
            <%--<label id="lyear"></label>--%>
            <%--<asp:Label ID="lblYear"  Text=""></asp:Label>--%>
        </td>
     
        
      </tr>
         <tr>
      
        <td>
            <input type="text" id="stock_country" value="" />
            <%--<label id="lcountry"></label>--%>
        </td>
        
      </tr>
       
    </tbody>
  </table>
                          <asp:Button ID="btnFilter" runat="server" Text="Apply Filter" CssClass=".btn-success" Visible="false"
                              />

                           <table id="grid_stocks" class="scroll"> </table>
        <div id="pager_stocks" class="scroll" style="text-align:center;"></div>

          <br />           

</div>
         </div>
     <div class="row">
               <br />
 
           <div class= "col-md-12" style="background-color:#b3ffcc" >
                <h3>Flows between processes</h3>
                <table class="table table-responsive">
   <tr>
       <td style="width:40%">Choose Source and Target Process</td>
        <td style="width:30%">
             <asp:DropDownList ID="drp_source_flows" runat="server" CssClass="form-control" Width="80%">
                                                                            </asp:DropDownList>
                                                                            <asp:RequiredFieldValidator ID="rfv_drp_source_flows" runat="server"
                                                                                ControlToValidate="drp_source_flows" ErrorMessage="Please select Process Name"
                                                                                InitialValue="Process Name" SetFocusOnError="True" CssClass="form-control" Width="80%"></asp:RequiredFieldValidator>
        </td>
         <td style="width:30%">
              <asp:DropDownList ID="drp_target_flows" runat="server" CssClass="form-control" Width="80%">
                                                                            </asp:DropDownList>
                                                                            <asp:RequiredFieldValidator ID="rfv_drp_target_flows" runat="server"
                                                                                ControlToValidate="drp_target_flows" ErrorMessage="Please select Process Name"
                                                                                InitialValue="Process Name" SetFocusOnError="True" CssClass="form-control" Width="80%"></asp:RequiredFieldValidator>
</td>
      </tr>
    <tbody>
        </tbody>
                   </table>

                 <h4>Filter by<span class="color"> Year and Region </span></h4>

                          <table class="table table-responsive">
   
    <tbody>
      <tr>

        <td> <input type="text" id="flow_year" value="" />

        </td>
     
        
      </tr>
         <tr>
      
        <td>
            <input type="text" id="flow_country" value="" />

        </td>
        
      </tr>
       
    </tbody>
  </table>


              

                <table id="grid_flows" class="scroll"></table>
        <div id="pager_flows" class="scroll" style="text-align:center;"></div>
               <br />
          </div>
         </div>
     <div class="row">
               <br />
               <div class= "col-md-12" style="background-color:#ccffdd" >
                   <br />
                    <h3>Material cycle for fixed year and region</h3>


                    <table class="table table-responsive">
   <tr>
       <td style="width:40%">Choose Year and Region</td>
        <td style="width:30%">
             <asp:DropDownList ID="drpCycleYear" runat="server" CssClass="form-control" Width="80%">
                                                                            </asp:DropDownList>
                                                                          
        </td>
         <td style="width:30%">
              <asp:DropDownList ID="drpCycleCountry" runat="server" CssClass="form-control" Width="80%">
                                                                            </asp:DropDownList>
                                                                          
</td>
      </tr>
    <tbody>
        </tbody>
                   </table>



                    <table id="grid_flow_cycle" class="scroll"> </table>
        <div id="pager_flow_cycle" class="scroll" style="text-align:center;"> <br /></div>
                   <br />
                  
<br />
          </div>
         </div>

     <div class="row">
           <div class= "col-md-12" style="text-align:center;" >
               <br />
           <input type="button" value="Go To Sankey Maker" class="btn btn-success" onclick="open_sankey();" />
          </div>
      </div>

     <div class="row">
           <div class= "col-md-12" >
                <asp:HiddenField ID="hdnYear" runat="server" value="" />
        <asp:HiddenField ID="hdnCountry" runat="server" value="" />

                          <asp:HiddenField ID="stock_hdnSelectedYear" runat="server" value="" />
        <asp:HiddenField ID="stock_hdnSelectedCountry" runat="server" value="" />

                                     <asp:HiddenField ID="flow_hdnSelectedYear" runat="server" value="" />
        <asp:HiddenField ID="flow_hdnSelectedCountry" runat="server" value="" />
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