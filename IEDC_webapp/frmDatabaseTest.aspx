<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="frmDatabaseTest.aspx.cs" Inherits="IEF_Database.frmDatabaseTest" EnableEventValidation="false" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>IEF Database</title>
   <%-- <link href="css/jquery-ui.css" rel="stylesheet" />
    
    <link href="css/bootstrap.css" rel="stylesheet" />
    <link href="css/footer-distributed-with-address-and-phones.css" rel="stylesheet" />
    <link href="css/body.css" rel="stylesheet" />

    <script src="scripts/lb/jquery-3.1.1.min.js"></script>--%>

    <!-- css -->

    <!-- JavaScriptLibrary -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/free-jqgrid/4.14.1/css/ui.jqgrid.min.css"/>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/free-jqgrid/4.14.1/jquery.jqgrid.min.js"></script>

        <script src="scripts/lb/inputTags.jquery.js"></script>
    <script src="scripts/lb/tag_app.js"></script>
    <link href="css/inputTags.css" rel="stylesheet" />


    <script src="scripts/json2-min.js" type="text/javascript"></script>

    <script src="scripts/js_dataset_grid.js"></script>

    <script src="scripts/js_stocks_grid.js"></script>
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

.col-md-2 {
    float: left;
    padding: 0;
    background-color:none;
    padding-bottom: 20px;
}
.col-md-2 p a, p a:hover {
    color: darkgreen;
    font-weight:bold;
    font-size:22px;
    text-decoration: none;
}
.col-md-2 p span {
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

    <script>
        //jQuery(document).ready(function () {
        //    //alert();
        //    jQuery("#grid_dataset").jqGrid('setGridWidth', $myLayout.state.center.innerWidth - 2, 'true');
        //});
    </script>
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
          
                    <li><a href="frmHome.aspx">Home</a></li>
                        <li><a href="frmCircularSankeyLP.aspx">Sankey Diagram</a></li>
                        <li><a href="frmBuildMap.aspx">Map Maker</a></li>
                        <li><a href="frmBuildChart.aspx">Pie Chart</a></li>
                        <li><a href="frmUserProfile.aspx">Your History</a></li>
                        <li><a href="frmUserGuide.aspx">User Guide</a></li>
                        <li><a href="frmAboutUs.aspx">About Us</a></li>

                    
      </ul>
     
    </div>
  </div>
</nav>

<div class="container-fluid" style="background-color:white" >

                 <br />
    <div class="row">
        
        <div class= "col-md-2">
            <p><a href="#">IEF<span>Database</span></a></p>
            </div>
         <div class= "col-md-10">
            <strong style="color:green; font-size:14px;"> Hello,</strong>   <asp:Label ID="lblUser" CssClass="user-name-label" runat="server" Text="" ></asp:Label> 
                     &nbsp;&nbsp;&nbsp;&nbsp; 
                     <asp:Button ID="btnLogOut" runat="server" class="btn btn-success" Text="Log Out" OnClick="btnLoggOut_Click" />
        </div>

       </div>
      <div class="row">  
               
        
                      <div class= "col-md-12" >

        
                           <table id="grid_dataset" class="scroll">
        </table>
        <div id="pager_dataset" class="scroll" style="text-align:center;"></div> 
        

        <table class="table table-responsive">
   
    <tbody>
        <tr>
            <td style="width:40%">Choose Process Type</td>
            <td style="width:30%">
                <asp:RadioButtonList ID="rdoProcessType" runat="server" 
            RepeatDirection="Horizontal" AutoPostBack="true" >
            <asp:ListItem Text ="Stocks" Value="1" />
            <asp:ListItem Text ="Flows" Value="2" />
        </asp:RadioButtonList>
            </td>
            <td style="width:30%"></td>
        </tr>
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
    </tbody>
  </table>
        
                          <h3>Filter With <span class="color"> Year & Region </span></h3>
   
                          
                          <table class="table table-responsive">
   
    <tbody>
      <tr>

        <td> <input type="text" id="year" value="" />
            <%--<label id="lyear"></label>--%>
            <%--<asp:Label ID="lblYear"  Text=""></asp:Label>--%>
        </td>
     
        
      </tr>
         <tr>
      
        <td>
            <input type="text" id="country" value="" />
            <%--<label id="lcountry"></label>--%>
        </td>
        
      </tr>
    </tbody>
  </table>
                          <asp:Button ID="btnFilter" runat="server" Text="Apply Filter" CssClass=".btn-success" 
                              />

                           <table id="grid_stocks" class="scroll">
        </table>
        <div id="pager_stocks" class="scroll" style="text-align:center;"></div> 


                          <asp:HiddenField ID="hdnYear" runat="server" value="" />
        <asp:HiddenField ID="hdnCountry" runat="server" value="" />

                          <asp:HiddenField ID="hdnSelectedYear" runat="server" value="" />
        <asp:HiddenField ID="hdnSelectedCountry" runat="server" value="" />

        <br />
                          <asp:Button ID="btnExport" runat="server" Text="Export" />
        <br />

</div>

                    </div>

</div><br/>

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
            <a href="http://www.internal.industrialecology.uni-freiburg.de">Internal</a>
                    .
           <a href="http://www.teaching.industrialecology.uni-freiburg.de">Teaching</a>
				</p>
			
			</div>

			<div class="footer-center">
                    <h3>Industrial Ecology <span>Freiburg</span></h3>
					<p>  &copy; 2017 Stefan Pauliuk &amp; Mahadi Hasan<br/>
                        Nachhaltiges Energie- und Stoffstrommanagement <br/>
                        Fakultät für Umwelt und Natürliche Ressourcen <br/>
                       
					       Tennenbacher Straße 4 <br/>
                         D-79106 Freiburg <br/>
                        Germany</p>
			</div>

			

		</footer>
    </form>
</body>
</html>