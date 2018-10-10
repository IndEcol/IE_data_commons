<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="fromTagTest.aspx.cs" Inherits="IEF_Database.fromTagTest" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <script src="scripts/lb/jquery-3.1.1.min.js"></script>
    <script src="scripts/lb/inputTags.jquery.js"></script>
    <script src="scripts/lb/tag_app.js"></script>
    <link href="css/inputTags.css" rel="stylesheet" />
</head>
<body>
    <form id="form1" runat="server">

    <div class="container">
    <h1><span class="color">Filter With</span> Year</h1>
    <input type="text" id="year" value="" />
    <%--<p id="events">
      <strong>Event: </strong>
      <span></span>
    </p>
    <p id="autocomplete"> 
      <strong>Autocomplete: </strong>
      <span></span>
    </p>--%>
    
    <input type="text" id="country" value="" />
    <%--<p id="events">
      <strong>Event: </strong>
      <span></span>
    </p>
    <p id="autocomplete"> 
      <strong>Autocomplete: </strong>
      <span></span>
    </p>--%>
    </div>
<asp:HiddenField ID="hdnYear" runat="server" value="" />
        <asp:HiddenField ID="hdnCountry" runat="server" value="" />
    </form>
  
</body>
</html>