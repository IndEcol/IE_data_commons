<%@ Page Language="C#"  MaintainScrollPositionOnPostback="true" AutoEventWireup="true" enableEventValidation ="false" CodeBehind="frmDatabaseHome.aspx.cs" Inherits="IEF_Database.frmDatabaseHome" %>

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
    <script src="scripts/lb/tag_app.js"></script>
    <link href="css/inputTags.css" rel="stylesheet" />
    <!-- css -->

    <!-- JavaScriptLibrary -->
        <script src="scripts/lib/jquery-1.12.4.js"></script>
    <script src="scripts/lib/jquery-ui.js"></script>
    
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
    <%--<asp:ScriptManager ID="ScriptManager1" runat="server">
        </asp:ScriptManager>
        <asp:UpdatePanel ID="UpdatePanel1" runat="server">
            <ContentTemplate>--%>
                 <%--<script type="text/javascript">
                     Sys.Application.add_load(tag);
     </script>--%>
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
          
        <asp:GridView ID="grdDataSet" Width="100%" AutoGenerateColumns="False" 
            CssClass="table table-striped table-bordered table-hover table-responsive"
   runat="server" PageSize="10"
   AllowPaging="true" OnPageIndexChanging="grdDataSet_PageIndexChanging" >
            <Columns>
                <asp:TemplateField HeaderText="">
                    <ItemTemplate>
                        <asp:Button ID="btnDatasetGridSelect" runat="server" Text="Select" OnClick="btnDatasetGridSelect_Click" />
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="SI" HeaderText="System ID" />
                <asp:BoundField DataField="SD" HeaderText="System Definition" />
                <asp:BoundField DataField="DN" HeaderText="Dataset Name" />
                <asp:BoundField DataField="RD" HeaderText="Reference Date" />
                <asp:BoundField DataField="MRU" HeaderText="Most Recent Update" />
                <asp:BoundField DataField="CAI" HeaderText="Corresponding Author" />
                <asp:BoundField DataField="OAI" HeaderText="Other Author" />
                <asp:BoundField DataField="DR" HeaderText="Document Reference" />
                <asp:BoundField DataField="R" HeaderText="Region" />
                <asp:BoundField DataField="TPA" HeaderText="Time Period of Analysis" />
                <asp:BoundField DataField="IE" HeaderText="Indicator Element" />
            </Columns>
            <EditRowStyle BackColor="#7C6F57" />
            
            <HeaderStyle BackColor="#E3EAEB" Font-Bold="True" />
            <PagerStyle HorizontalAlign="Center" />
            <RowStyle BackColor="#E3EAEB" />
            <SelectedRowStyle BackColor="#C5BBAF" Font-Bold="True" />
            <SortedAscendingCellStyle BackColor="#F8FAFA" />
            <SortedAscendingHeaderStyle BackColor="#246B61" />
            <SortedDescendingCellStyle BackColor="#D4DFE1" />
            <SortedDescendingHeaderStyle BackColor="#15524A" />
        </asp:GridView>

        <br />
        <br />

        <asp:GridView ID="grdProcessList" runat="server" Width="100%"  CssClass="table table-striped table-bordered table-hover"
    PageSize="500"
   AllowPaging="true" OnPageIndexChanging="grdProcessList_PageIndexChanging" >
            <Columns>
                <asp:TemplateField HeaderText="">
                    <ItemTemplate>
                        <asp:Button ID="btnProcessListGridSelect" runat="server" Text="Select" OnClick="btnProcessListGridSelect_Click"/>
                    </ItemTemplate>
                </asp:TemplateField>
            </Columns>
        </asp:GridView>

        <table class="table table-responsive">
   
    <tbody>
        <tr>
            <td style="width:40%">Choose Process Type</td>
            <td style="width:30%">
                <asp:RadioButtonList ID="rdoProcessType" runat="server" OnSelectedIndexChanged="rdoProcessType_SelectedIndexChanged" 
            RepeatDirection="Horizontal" AutoPostBack="true" >
            <asp:ListItem Text ="Stocks" Value="1" />
            <asp:ListItem Text ="Flows" Value="2" />
        </asp:RadioButtonList>
            </td>
            <td style="width:30%"></td>
        </tr>
      <tr>
          <td style="width:40%">Choose Stock Process</td>
        <td style="width:30%"> <asp:DropDownList ID="drdStocks" runat="server" OnSelectedIndexChanged="drdStocks_SelectedIndexChanged" 
            AutoPostBack="true" Enabled="False" CssClass="form-control" Width="80%"></asp:DropDownList></td>
     <td style="width:30%"></td>
        
      </tr>
         <tr>
       <td style="width:40%">Choose Source and Target Process</td>
        <td style="width:30%"> <asp:DropDownList ID="drdSourceFlows" runat="server" OnSelectedIndexChanged="drdSourceFlows_SelectedIndexChanged" 
            AutoPostBack="true" Enabled="False" CssClass="form-control" Width="80%"></asp:DropDownList></td>
         <td style="width:30%"> <asp:DropDownList ID="drdTargetFlows" runat="server" OnSelectedIndexChanged="drdTargetFlows_SelectedIndexChanged" 
            AutoPostBack="true" Enabled="False" CssClass="form-control" Width="80%"></asp:DropDownList>
</td>
      </tr>
    </tbody>
  </table>
        
                          <h3>Filter With <span class="color"> Year & Region </span></h3>
   
                          
                          <table class="table table-responsive">
   
    <tbody>
      <tr>

        <td> <input type="text" runat="server" id="year" value="All" />
            <asp:Label ID="lblYear" runat="server" Text=""></asp:Label>
        </td>
     
        
      </tr>
         <tr>
      
        <td>
            <input type="text" runat="server" id="country" value="All" />
            
        </td>
        
      </tr>
    </tbody>
  </table>
                          <asp:Button ID="btnFilter" runat="server" Text="Apply Filter" CssClass=".btn-success" 
                              OnClick="btnFilter_Click"/>

                          <asp:HiddenField ID="hdnYear" runat="server" value="" />
        <asp:HiddenField ID="hdnCountry" runat="server" value="" />

                          <asp:HiddenField ID="hdnSelectedYear" runat="server" value="" />
        <asp:HiddenField ID="hdnSelectedCountry" runat="server" value="" />

        <asp:GridView ID="grdStocks" runat="server" Width="100%" CssClass="table table-striped table-bordered table-hover"
   AllowPaging="True" OnPageIndexChanging="grdStocks_PageIndexChanging" AutoGenerateColumns="False" CellPadding="4"  GridLines="None" >
            <AlternatingRowStyle BackColor="White" />
            <Columns>
                <asp:TemplateField HeaderText="">
                    <ItemTemplate>
                        <asp:Button ID="btnStocksGridSelect" runat="server" Text="Select"/>
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="SI" HeaderText="System Id" />
                <asp:BoundField DataField="SDN" HeaderText="Stock Dataset Number" />
                <asp:BoundField DataField="PN" HeaderText="Process Name" />
                <asp:BoundField DataField="C" HeaderText="Country Name" />
                <asp:BoundField DataField="T" HeaderText="Time" />
                <asp:BoundField DataField="IE" HeaderText="Indicator Element" />
                <asp:BoundField DataField="AD" HeaderText="Aspect Of Dataset" />
                <asp:BoundField DataField="V" HeaderText="Value" />
                <asp:BoundField DataField="UID" HeaderText="Unit ID" />
            </Columns>
            <EditRowStyle BackColor="#7C6F57" />
            
            <HeaderStyle BackColor="#E3EAEB" Font-Bold="True" />
            <PagerStyle HorizontalAlign="Center" />
            <RowStyle BackColor="#E3EAEB" />
            <SelectedRowStyle BackColor="#C5BBAF" Font-Bold="True" />
            <SortedAscendingCellStyle BackColor="#F8FAFA" />
            <SortedAscendingHeaderStyle BackColor="#246B61" />
            <SortedDescendingCellStyle BackColor="#D4DFE1" />
            <SortedDescendingHeaderStyle BackColor="#15524A" />
        </asp:GridView>

        <br />
                          <asp:Button ID="btnExport" runat="server" Text="Export" OnClick="btnExport_Click" />
        <br />

        <asp:GridView ID="grdFlows" runat="server" CssClass="table table-striped table-bordered table-hover"
    PageSize="10"
   AllowPaging="true" OnPageIndexChanging="grdFlows_PageIndexChanging" >
            <Columns>
                <asp:TemplateField HeaderText="">
                    <ItemTemplate>
                        <asp:Button ID="btnStocksGridSelect" runat="server" Text="Select"/>
                    </ItemTemplate>
                </asp:TemplateField>
            </Columns>
        </asp:GridView>

</div>

                    </div>
               <%-- </ContentTemplate>
</asp:UpdatePanel>--%>
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