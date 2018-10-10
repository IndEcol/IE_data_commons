<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="units.aspx.cs" Inherits="IEF_Database.units" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>units</title>

    <link href="css/bootstrap.css" rel="stylesheet" />
    <link href="css/footer-distributed-with-address-and-phones.css" rel="stylesheet" />
    <link href="css/body.css" rel="stylesheet" />

    <!-- css -->

    <!-- JavaScriptLibrary -->



    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/>


      <link rel="stylesheet" type="text/css" media="screen" href="css/redmond/jquery-ui-1.7.2.custom.css" />
     <link rel="stylesheet" type="text/css" media="screen" href="css/ui.jqgrid.css" />
      <script type="text/javascript" src="js/grid.locale-en.js"></script>
      <script type="text/javascript" src="js/jquery.jqGrid.min.js"></script>
    <script src="scripts/json2-min.js" type="text/javascript"></script>



  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

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

.col-md-12 p span {
    color: lightgreen;
}

        .table {
    margin-bottom: 20px;
}
    
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
          
                   <li><a href="http://www.industrialecology.uni-freiburg.de" target="_blank">Home</a></li>

                    
      </ul>
     
    </div>
  </div>
</nav>

<div class="container-fluid" >

    <div class="row">
        <div class= "col-md-12">
           
            </div>


       </div>
     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
                <h4>Table contents of Units </h4>
              <asp:GridView ID="grdUnits" runat="server" CellPadding="10" ForeColor="#333333" BorderColor="#E3EAEB" BorderStyle="None" BorderWidth="1px" Width="100%" >
                  <HeaderStyle Height="40px" BackColor="#1C5E55" ForeColor="White" />
                                                <AlternatingRowStyle BackColor="White" />
                  <EditRowStyle BackColor="#7C6F57" />
                                                <FooterStyle BackColor="#1C5E55" Font-Bold="True" ForeColor="White" />
                                                <HeaderStyle BackColor="#1C5E55" Font-Bold="True" ForeColor="White" />
                                                <PagerStyle BackColor="#666666" ForeColor="White" HorizontalAlign="Center" />
                                                <RowStyle BackColor="#E3EAEB" />
                                                <SelectedRowStyle BackColor="#C5BBAF" ForeColor="#333333" Font-Bold="True" />
                                                <SortedAscendingCellStyle BackColor="#F8FAFA" />
                                                <SortedAscendingHeaderStyle BackColor="#246B61" />
                                                <SortedDescendingCellStyle BackColor="#D4DFE1" />
                                                <SortedDescendingHeaderStyle BackColor="#15524A" />
                                            </asp:GridView>
               
            </div>
         </div>

    <div class="row">
               <br />
 
         </div>

     

    
     <div class="row">
               <br />
 
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