# File changes & activity Niko

Documenting changes and progress Niko while developping [IEDC_tools](https://github.com/IndEcol/IEDC_tools). 
File changes refer to the folder `IE_Data_Commons_Prototype/Data_ODYM_Format`. 

## 11. Feb 2019

- updated https://github.com/IndEcol/IE_data_commons/issues/20
- `1_F_NewPassengerVehicleRegistration_AllCountries_OICA_2017.xlsx`
  - renamed "Use phase" to "use phase" in Data sheet
- `3_IUP_Vehicles_9Countries_Dhaniati_2012.xlsx` contains different values to encode `NULL`. *We seriously need a definition.*
- All LIST and TABLE type files work now, *except* the ones without a 'dataset' entry

## 7. Feb 2019

- Updated https://github.com/IndEcol/IE_data_commons/issues/20#issuecomment-461464876

- `1_UPI_USLCI_Aluminum_cold_rolling_at_plant.xlsx`
  - Changed sheetname "Value_master" or "Values_Master" to "Data"
  
- `1_UPI_USLCI_Limestone_at_mine.xlsx`
  - Data sheet changed "None" to "unspecified" for "destination_region" column

- `3_LT_SteelCycle_PAULIUK_2013.xlsx`
  - Changed sheetname "Value_master" or "Values_Master" to "Data"
  - Replaced "Latin America (the entire Americas without the US and Canada" with "Latin America (the entire Americas without the US and Canada)"
  - Removed trailing ";" from column "stats_array string"
  - Fixed error with Stefan (see https://github.com/IndEcol/IE_data_commons/issues/20#issuecomment-461424064)

- `3_MC_SteelDemand_HU_2010.xlsx`
  - Removed trailing ";" from column "stats_array string"


## 5. Feb 2019

Redoing iedc_review database

- Working on subfolder `LIST` 

- Created issue on input file errors: https://github.com/IndEcol/IE_data_commons/issues/20

- `LIST/*.xlsx`
  - Changed sheetname "Value_master" or "Values_Master" to "Data"
  
- `LIST/1_F_Primary_material_input_Global_Krausmann_2017.xlsx`
  - Rename sheet "Data" to "xData"
  - Rename sheet "Data1" to "Data" 
  
- `LIST/3_LT_AluCycle_LIU_2012.xlsx`
  - Removed trailing ";" from column "stats_array string"

- `LIST/3_LT_AluCycle_LIU_2013.xlsx`
  - Removed trailing ";" from column "stats_array string"
  
- `LIST/3_LT_IAI_GARC_2011.xlsx`
  - Removed trailing ";" from column "stats_array string"


