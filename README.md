# IE_data_commons
Code and documentation for a general industrial ecology structured data commons

Here we document efforts to build a general data model and database for socioeconomic metabolism, boldly labelled as 'Industrial Ecology Data Commons' (IEDC). The data in the project include stocks and flows of all kind, composition data, prices, process inventories, lifetimes, etc. They have in common a data model based on multidimensional arrays and the representation of the location of the data in the different dimensions (time, region, process, commodity, material, scenario, ...) as tuples. A publication on the data model and its implementation in a database is underway ('A General Data Model for Socioeconomic Metabolism and its Implementation in an Industrial Ecology Data Commons Prototype'). 

The prototype is up and running under http://www.database.industrialecology.uni-freiburg.de/

The data that fit the general data model are structured and stored in a relational database, the structure of which is documented here.
The data are structured (they all fit a commmon data model and are organised in a single database) but not linked (different data come in different classifications, resolution and scope of the different datasets is not compatible with others). That means this database exhibits an intermediate step of data integration: more integrated than repositories like Figshare or Zenodo (Data are not structured or structured in custom formats and not linked) and less integrated than highly integrated databases like ecoinvent or EXIOBASE (data are structured and come in a project-wide classification)

This repository contains:
* mySQL code to create the (empty) database on any machine (folder mySQL_Create)
* csv templates to fill the lookup tables (licenses, etc.) (folder IEDC_LookupTable_fill)
* csv templates to fill the classfication table (folder IEDC_Classification_fill)
* Python scripts with mySQL code to write to and download from the database (folder IEDC_content_fill)
* C# code for the web interface (folder IEDC_webapp)
* Sample code for the pymysql interface (folder mySQL_Python_Examples)

Last change of this document: October 19th, 2018.


