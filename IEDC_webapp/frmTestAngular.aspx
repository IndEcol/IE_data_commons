<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="frmTestAngular.aspx.cs" Inherits="IEF_Database.frmTestAngular" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml" ng-app="dictModule">
<head runat="server">
     <title>AngularJS Plunker</title>
    <script>
        document.write('<base href="' + document.location + '" />');
    </script>
    <link href="css/styleAng.css" rel="stylesheet" />
  
    <link data-require="bootstrap-css" rel="stylesheet" href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap.min.css" />
    <script data-require="angular.js@1.2.x" src="http://code.angularjs.org/1.2.13/angular.js" data-semver="1.2.13"></script>
    <script src="scripts/app.js"></script>

    <script src="scripts/pagination.js"></script>
    <script src="scripts/xuiTable.js"></script>
</head>
<body ng-controller="dictController">
    <form id="form1" runat="server">
    <p>Hello {{name}}!</p>
    <input type="text" ng-model='PageSize' placeholder='page size'>
    <input type="text" ng-model="search.id" placeholder='id'>
    <input type="text" ng-model="search.description" placeholder='description'>
    <table xui-table="test" table-headers="TableHeader" table-data="List" items-per-page='10' page-window='PageSize' table-pager='true' table-filter='searchfn(input)' table-filter-factor='search'>
        <tbody>
            <tr>
                <td class="id" data-fileid="{{row.id}}">{{row.id}} </td>
                <td class="name">{{row.name }} </td>
                <td class="description">{{row.description}} </td>
                <td class="field3">{{row.field3}} </td>
                <td class="field4"><i ng-class="{'icon-ok-sign': !!row.field4 , 'icon-circle-blank': !row.field4}"></i> </td>
                <td class="Action">
                    <button ng-click='$parent.$parent.open(row.id)'>test</button>
                </td>
            </tr>
        </tbody>
    </table>
    </form>
</body>
</html>