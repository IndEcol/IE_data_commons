<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="frmDB.aspx.cs" Inherits="IEF_Database.frmDB" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
   <title>IEF Database</title>

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

    <script src="scripts/js_dataset_grid.js"></script>


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
  $( function() {
      $("#Access_date").datepicker();
      $("#Submission_date").datepicker();
      $("#Review_date").datepicker();

      
      var aspect_list = ["Aspect_1", "Aspect_1", "Aspect_1", "Aspect_1", "Aspect_1", "Aspect_1"];
      var options = ["Model time",
    "age-cohorts",
      "chemical elements",
      "trivial classification, 1 entry only",
      "Region of process or stock",
      "Region of origin (flow)",
      "region of destination (flow)",
      "Process where stock is located",
      "Process of origin of flow",
      "Process of destination of flow",
      "Goods and products considered",
      "Engineering materials considered",
      "End-of-life products, buildings, and infrastructure",
      "waste and scrap types considered",
      "Energy consumed",
      "Scenerios considered (e.g., SSP)",
      "Costs, emissions factors, social impacts"]; 

      var select = document.getElementById("Aspect_1"); 
      var counter = 1;
      options.forEach(function(item) {
          var el = document.createElement("option");
          el.textContent = item;
          el.value = counter;
          select.appendChild(el);
          counter++;
      });


  });

  

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
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Dataset ID</td>
      <td> <input type="text" id="dataset_id" class="form-control" style="width:60%"/></td>

      <td>Dataset Name, serves as description</td>
      <td><input type="text" id="dataset_name" class="form-control" style="width:60%"/></td>

      <td>Dataset version</td>
      <td><input type="text" id="dataset_version" class="form-control" style="width:60%"/></td>

    </tr>
  </tbody>
  </table>
</div>
               
            </div>
         </div>

    <div class="row">
               <br />
 
         </div>

     
     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Data category</td>
      <td> 
                   <select name="dataset_category" id="dataset_category" style="width:60%"  class="form-control"  >
  <option value="1">Flow</option>
  <option value="2">Stock</option>
  <option value="3">Material/Product property</option>
</select>                                                          
</td>


      <td>Data type</td>
      <td><input type="text" id="dataset_type" class="form-control" /></td>


      <td>Layer</td>
      <td><input type="text" id="dataset_layer" class="form-control" /></td>

    </tr>
  </tbody>
  </table>
</div>
               
            </div>
         </div>


     <div class="row">
               <br />
 
         </div>

     
     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Process scope</td>
     <td><input type="text" id="Process_scope" class="form-control" /></td>
         <td>Process resolution</td>
      <td><input type="text" id="Process_resolution" class="form-control" /></td>
    
  

      <td>Product scope</td>
      <td><input type="text" id="Product_scope" class="form-control" /></td>
        </tr>
      <tr>
         <td>Product resolution</td>
      <td><input type="text" id="Product_resolution" class="form-control" /></td>
    

      

      <td>Material scope</td>
      <td><input type="text" id="Material_scope" class="form-control" /></td>

         <td>Material resolution</td>
      <td><input type="text" id="Material_resolution" class="form-control" /></td>
    

          </tr>
<tr>

      <td>Regional scope</td>
      <td><input type="text" id="Regional_scope" class="form-control" /></td>
       
         <td>Regional resolution</td>
      <td><input type="text" id="Regional_resolution" class="form-control" /></td>
  

       

      <td>Temporal scope</td>
      <td><input type="text" id="Temporal_scope" class="form-control" /></td>
    </tr>
        <tr>
         <td>Temporal resolution</td>
      <td><input type="text" id="Temporal_resolution" class="form-control" /></td>
    

      <td>Description Keywords</td>
      <td><input type="text" id="Description_Keywords" class="form-control" /></td>

         <td>Data provenance</td>
      <td>


            <select name="Data_provenance" id="Data_provenance" style="width:60%"  class="form-control"  >
  <option value="1">Expert estimates</option>
  <option value="2">Expert estimates, mass balance, product description</option>
  <option value="3">Aggregated data or estimates from industry association</option>
  <option value="4">Official data from government institution</option>
  <option value="5">Result of academic MFA work</option>
  <option value="6">Scenario models</option>
  <option value="7">Compiled from official and semi-official sources</option>
</select>                                                
      </td>
            </tr>
      <tr>
           <td>Comments</td>
      <td><input type="text" id="Comments" class="form-control" /></td>
               <td></td>
      <td>
                                         
      </td>
           <td></td>
            <td>
                
                                                 
      </td>
       </tr>
  </tbody>
 </table>
</div>
               
            </div>
         </div>


     <div class="row">
               <br />
 
         </div>

     
     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>

       <tr>
           <td>Aspect 1</td>
      <td>
          <select name="Aspect 1" id="Aspect_1" style="width:60%"  class="form-control"  >
 
</select>            
         </td>
               <td>Aspect 1 classification</td>
      <td>
          <input type="text" id="aspect_1_class" class="form-control" />                                       
      </td>
           <td>Aspect 2</td>
            <td>
                
            <select name="Aspect 2" id="Aspect_2" style="width:60%"  class="form-control"  >
 
</select>                                                
      </td>
             <td>Aspect 2 classification</td>
      <td>
          <input type="text" id="aspect_2_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Aspect 3</td>
      <td>
          <select name="Aspect 3" id="Aspect_3" style="width:60%"  class="form-control"  >
 
</select>            
         </td>
               <td>Aspect 3 classification</td>
      <td>
          <input type="text" id="aspect_3_class" class="form-control" />                                       
      </td>
           <td>Aspect 4</td>
            <td>
                
            <select name="Aspect 4" id="Aspect_4" style="width:60%"  class="form-control"  >
 
</select>                                                
      </td>
             <td>Aspect 4 classification</td>
      <td>
          <input type="text" id="aspect_4_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Aspect 5</td>
      <td>
          <select name="Aspect 5" id="Aspect_5" style="width:60%"  class="form-control"  >
 
</select>            
         </td>
               <td>Aspect 5 classification</td>
      <td>
          <input type="text" id="aspect_5_class" class="form-control" />                                       
      </td>
           <td>Aspect 6</td>
            <td>
                
            <select name="Aspect 6" id="Aspect_6" style="width:60%"  class="form-control"  >

</select>                                                
      </td>
             <td>Aspect 6 classification</td>
      <td>
          <input type="text" id="aspect_6_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Aspect 7</td>
      <td>
          <select name="Aspect 7" id="Aspect_7" style="width:60%"  class="form-control"  >

</select>            
         </td>
               <td>Aspect 7 classification</td>
      <td>
          <input type="text" id="aspect_7_class" class="form-control" />                                       
      </td>
           <td>Aspect 8</td>
            <td>
                
            <select name="Aspect 8" id="Aspect_8" style="width:60%"  class="form-control"  >

</select>                                                
      </td>
             <td>Aspect 8 classification</td>
      <td>
          <input type="text" id="aspect_8_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Aspect 9</td>
      <td>
          <select name="Aspect 9" id="Aspect_9" style="width:60%"  class="form-control"  >
 
</select>            
         </td>
               <td>Aspect 9 classification</td>
      <td>
          <input type="text" id="aspect_9_class" class="form-control" />                                       
      </td>
           <td>Aspect 10</td>
            <td>
                
            <select name="Aspect 10" id="Aspect_10" style="width:60%"  class="form-control"  >

</select>                                                
      </td>
             <td>Aspect 10 classification</td>
      <td>
          <input type="text" id="aspect_10_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Aspect 11</td>
      <td>
          <select name="Aspect 11" id="Aspect_11" style="width:60%"  class="form-control"  >

</select>            
         </td>
               <td>Aspect 11 classification</td>
      <td>
          <input type="text" id="aspect_11_class" class="form-control" />                                       
      </td>
           <td>Aspect 12</td>
            <td>
                
            <select name="Aspect 12" id="Aspect_12" style="width:60%"  class="form-control"  >
 
</select>                                                
      </td>
             <td>Aspect 12 classification</td>
      <td>
          <input type="text" id="aspect_12_class" class="form-control" />                                       
      </td>
      </tr>

        <tr>
           <td>Tupel notation</td>
      <td>
         <input type="text" id="Tupel_notation" class="form-control" />  
        
         </td>
               <td>Semantic string example</td>
      <td>
          <input type="text" id="Semantic_string_example" class="form-control" />                                       
      </td>
           <td>Semantic string, general</td>
            <td>
                
                 <input type="text" id="Semantic_string" class="form-control" />                                    
      </td>
             <td></td>
      <td>
                                               
      </td>
      </tr>


  </tbody>
  </table>
</div>
               
            </div>
         </div>

      <div class="row">
               <br />
 
         </div>

     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Type of source</td>
     <td><input type="text" id="Type_of_source" class="form-control" /></td>
         <td>Dataset license</td>
      <td><input type="text" id="Dataset_license" class="form-control" /></td>
    
  

      <td>Main/first author or organisation</td>
      <td><input type="text" id="Main_author" class="form-control" /></td>
        </tr>
      <tr>
         <td>Link to dataset</td>
      <td><input type="text" id="Link_to_dataset" class="form-control" /></td>
    

      

      <td>Dataset format</td>
      <td><input type="text" id="Dataset_format" class="form-control" /></td>

         <td>Link to accompanying report/paper</td>
      <td><input type="text" id="Link_to_paper" class="form-control" /></td>
    

          </tr>
<tr>

      <td>Suggested citation</td>
      <td><input type="text" id="Suggested_citation" class="form-control" /></td>
       
         <td>Visible</td>
      <td><input type="text" id="Visible" class="form-control" /></td>
  

      </tr>
  </tbody>
 </table>
</div>
               
            </div>
         </div>

     <div class="row">
               <br />
 
         </div>

     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Access date</td>
     <td><input type="text" id="Access_date" class="form-control" /></td>
         <td>Submission date</td>
      <td><input type="text" id="Submission_date" class="form-control" /></td>
    
  

      <td>Submitting user</td>
      <td><input type="text" id="Submitting_user" class="form-control" /></td>
        </tr>
      <tr>
         <td>Dataset conversion info</td>
      <td><input type="text" id="Dataset_conversion_info" class="form-control" /></td>
    

      

      <td>Review date</td>
      <td><input type="text" id="Review_date" class="form-control" /></td>

         <td>Review user</td>
      <td><input type="text" id="Review_user" class="form-control" /></td>
    

          </tr>
<tr>

      <td>Review Comment</td>
      <td><input type="text" id="Review_Comment" class="form-control" /></td>
       
         <td></td>
      <td></td>
  

      </tr>
  </tbody>
 </table>
</div>
               
            </div>
         </div>

     <div class="row">
               <br />
 
         </div>

     <div class="row">
           <div class= "col-md-12"  style="background-color:#b3ffcc">
               <div class="table-responsive">
  <table class="table">
  <tbody>
    <tr>

      <td>Reserve1</td>
     <td><input type="text" id="Reserve1" class="form-control" /></td>
         <td>Reserve2</td>
      <td><input type="text" id="Reserve2" class="form-control" /></td>
    
  

      <td>Reserve3</td>
      <td><input type="text" id="Reserve3" class="form-control" /></td>
        </tr>
      <tr>
         <td>Reserve4</td>
      <td><input type="text" id="Reserve4" class="form-control" /></td>
    

      

      <td>Reserve5</td>
      <td><input type="text" id="Reserve5" class="form-control" /></td>

         <td></td>
      <td></td>
    

          </tr>
  </tbody>
 </table>
</div>
               
            </div>
         </div>

     <div class="row">
               <br />
                 
        
             <asp:Button ID="btnSave" runat="server" Text="Save Into Database" Enable="True" class="btn btn-success" style="display: block; margin: 0 auto;"></asp:Button>
                    
          <br />
         </div>

    <div class="row" style="align-items:center">
               <br />
          
         </div>
      <div class="row">
             
                      <div class= "col-md-12"  style="background-color:#b3ffcc">

                           <h5>DataSet</h5>
                           <table id="grid_data" class="scroll"></table>
        <div id="pager_data" class="scroll" style="text-align:center;"></div>
                          <br />
        </div>

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