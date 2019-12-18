# File changes & activity Niko

Documenting changes and progress Niko while developping [IEDC_tools](https://github.com/IndEcol/IEDC_tools). 
File changes refer to the folder `IE_Data_Commons_Prototype/Data_ODYM_Format`. 

## 18. Dec. 2019

- `3_MC_Buildings_Heeren_Fishman_ScientificData_2019_V1.1`
    - Changed value for `dataset_size` to 1.
    - Renamed sheet'comment' to 'Comment'
    - Added question in issue https://github.com/IndEcol/IE_data_commons/issues/21#issuecomment-567078634
    - Uploaded successfully
- `6_MIP_SI.POV.GINI_WorldBank_2019` deleted & uploaded successfully
- Moved LIST type files to ../NEW_LIST_2, i.e. 4_PY_YSTAFDB_EoL_RecoveryRate_v1.0.xlsx, 6_MIP_YSTAFDB_MetalUseShares_v1.0.xlsx, 6_URB_MetabolismOfCities_Jan2019_DOI_7326485.v1.xlsx
- `6_MIP_YSTAFDB_MetalUseShares_v1.0` 
    - has an issue: https://github.com/IndEcol/IE_data_commons/issues/24
    - *skipping for now*
- `6_CR_YSTAFDB_criticality_2019_v1.0`
    - Fixed classification names in Cover!F12:H14
    - 'Data layer' in Cover!D10 must be fixed
    - *skipping for now*
- `6_CR_YSTAFDB_criticality_ei_2019_v1.0.xlsx`
    - Fixed classification names in Cover!F12:H14
    - 'Data layer' in Cover!D10 must be fixed
    - *skipping for now*
- `1_F_Wood_Carbon_MFA_Indonesia_Aryapratama_2019` successfully uploaded
- `3_LT_Wood_Carbon_MFA_Indonesia_Aryapratama_2019` successfully uploaded
- `6_CR_YSTAFDB_criticality_sr_2019_v1.0`
    - classification names in Cover!F12:H14 need to be fixed
    - 'Data layer' in Cover!D10 must be fixed
    - *skipping for now*
- `6_CR_YSTAFDB_criticality_vsr_2019_v1.0` see above. *Skipping for now*.
-  `6_MIP_YSTAFDB_MetalUseShares_v1.0` see above. *Skipping for now*.

- `1_F_UN_Global_Material_Flows_Database`
- `2_IUS_Wood_Carbon_MFA_Indonesia_Aryapratama_2019` successfully uploaded


## 15. Dec. 2019

- `1_F_ElectricityGeneration_IEA_HeadlineEnergyData_2016` uploaded successfully
- `1_F_FinalEnergyConsumption_TFC_ByCountryAndSector_IEA_2018` uploaded successfully
- `3_MC_Buildings_Heeren_Fishman_ScientificData_2019_V1.1` not uploaded 
    - `dataset_size` and `comment` must have values
    - Waiting for [feedback](https://github.com/IndEcol/IE_data_commons/issues/21#issuecomment-565851165)
- `6_MIP_SI.POV.GINI_WorldBank_2019` not uploaded because there may be a [misunderstanding](https://github.com/IndEcol/IE_data_commons/issues/21#issuecomment-565851165) and I wait for feedback. Also this dataset will have to be removed from the DB again.

## 19. July 2019

- `1_F_ElectricityGeneration_IEA_HeadlineEnergyData_2016` could not be uploaded because it caused the following error: 

    > aspect_2 electricity generation from nuclear reactors 6 not in classification_items
    > aspect_2 electricity generation from renewable sources 6 not in classification_items
    > aspect_2 electricity generation, total 6 not in classification_items

    - Updated https://github.com/IndEcol/IE_data_commons/issues/23

- `6_MIP_SI.POV.GINI_WorldBank_2019` 

    - uploaded successfully
    - *Needs further attention:* https://github.com/IndEcol/IE_data_commons/issues/23#issuecomment-507737192

- `1_F_FinalEnergyConsumption_TFC_ByCountryAndSector_IEA_2018` not uploaded and caused the following error:

    > aspect_5 industry 6 not in classification_items
    > aspect_5 transport 6 not in classification_items
    > aspect_5 residential 6 not in classification_items
    > aspect_5 other (commercial and public services, agriculture/forestry, fishing and non-specified) 6 not in classification_items
    > aspect_5 non-energy use 6 not in classification_items

    - Updated https://github.com/IndEcol/IE_data_commons/issues/23

- `6_IMI_EU_Regional_Carbon_Footprint_Ivanova_2017` uploaded successfully

## 30. June 2019

### Done

- `2_P_SSP_Database_32R_Future.xlsx`
  - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
  - Uploaded.
- `3_MC_Buildings_China_Huang_2015.xlsx` uploaded.
- `1_F_PPPGDP_SSP_Database_32R_History`
    - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
    - Uploaded.
- `6_SHA_Urbanisation_SSP_Database_32R_History`
    - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
    - Uploaded.
- `6_SHA_Urbanisation_SSP_Database_32R_Future`
    - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
    - Uploaded.
- `2_P_SSP_Database_32R_History.xlsx`
    - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
    - Uploaded.
- `1_F_PPPGDP_SSP_Database_32R_Future.xlsx`
    - Changed the value for `dataset_version` from "*SSP Public Database (Version 1.1)*" to "*SSP Public Database (Ver 1.1)*". See also issue https://github.com/IndEcol/IE_data_commons/issues/22
    - Uploaded.
- `1_F_BuildingConstruction_HU_2010.xlsx` uploaded.
- `4_PE_EnergyIntensity_MaterialProduction_Hertwich_2015.xlsx`uploaded.
- `6_PCS_ResidentialBuildings_Canada.xlsx`uploaded.
- `6_IMI_Global_Household_EnvFootprints_Ivanova_2016.xlsx`
    - Renamed sheets "Unit_denom" to "Unit_denominator" and "Unit_nominator" to "Unit_nominator"
    - Uploaded.

### Pending

- `1_F_FinalEnergyConsumption_TFC_ByCountryAndSector_IEA_2018.xlsx` postponed until https://github.com/IndEcol/IE_data_commons/issues/23 is fixed
- `1_F_ElectricityGeneration_IEA_HeadlineEnergyData_2016.xlsx` cannot be included, because aspect 1 (energy does not exist).  https://github.com/IndEcol/IE_data_commons/issues/23
- `3_MC_Buildings_Heeren_Fishman_ScientificData_2019_V1` postponed until https://github.com/IndEcol/IE_data_commons/issues/21 is resolved.
- `6_MIP_SI.POV.GINI_WorldBank_2019.xlsx` postponed until https://github.com/IndEcol/IE_data_commons/issues/23 is fixed
- `6_IMI_EU_Regional_Carbon_Footprint_Ivanova_2017.xlsx`
    - Renamed sheets "Unit_denom" to "Unit_denominator" and "Unit_nominator" to "Unit_nominator"
    - Unit "cap" is not defined. 
    - Postponed until  https://github.com/IndEcol/IE_data_commons/issues/23 is resolved.


## 15. Feb 2019

- `1_F_steel_SankeyFlows_2008_Global`, `2_IUS_Buildings_Europe_2008_Enerdata`, `2_IUS_Wood_buildings_Pingoud_2000`, `3_LT_AluCycle_LIU_2012`, `3_LT_AluCycle_LIU_2013`, `3_LT_MetalDemand_DEETMAN_2018`, `3_LT_NonResBuildings_Minneapolis_2000`, `3_LT_ResBuildings_USA_1997_2009`, `3_LT_SteelCycle_PAULIUK_2013`, `3_MC_Buildings_Bergsdal_2007`, `3_MC_Buildings_Dodoo_2011`, `3_MC_Buildings_Gustavsson_2006`, `3_MC_Buildings_Gustavsson_2011`, `3_MC_Buildings_Kleemann_2014`, `3_MC_Buildings_Monahan_2010`, `3_MC_Buildings_Ortlepp_2016`, `3_MC_Buildings_Sinha_2016`, `3_MC_ConstructionImpact_Liu_2006`, `3_MC_MetalDemand_DEETMAN_2018`, `3_MC_Steel_DRCSCC_2005`, `3_MC_SteelDemand_HU_2010`, `3_MC_Vehicles_Hawkins_2012`, `3_MC_Vehicles_Modaresi_2014`, `3_SHA_EndUseShares_7Metals_Ciacci_2015`, `3_SHA_FabricationYield_CollectionRate_Alu_Liu_2012`, `4_PE_EnergyIntensity_AluminiumCycle_Liu_2012`, `4_PY_FabricationYield_Alu_Liu_2012`, `4_PY_FabricationYield_Cullen2012`, `4_PY_FabricationYield_Dahlstroem2004`, `4_PY_FabricationYield_Hatayama2010`, `4_PY_WorldSteel_EoL_RR_SteelScrap`, `5_CAP_PowerGenCapacity_Germany_2018`, `6_MSC_Wood_buildings_Höglmeier_2015`, `6_MSC_Wood_buildings_Pingoud_2000`, `6_PCS_Buildings_Europe_2008_Enerdata`, `6_PCS_Buildings_Indonesia_1985`, `6_PCS_Buildings_Indonesia_BPS_2008_2015`, `6_PCS_Buildings_Indonesia_Surahman_2014`, `6_PCS_Buildings_USA_MOURA_2015`, '1_F_IOT_UK_2010_pxp_Y', '1_F_IOT_UK_2010_pxp_Z', '1_F_IOT_UK_2010_pxp_e', '1_F_IOT_UK_2010_pxp_i', '1_F_IOT_UK_2010_pxp_v', '1_F_IOT_UK_2010_pxp_x', '1_F_WIO_Japan_Nakamura_Kondo_2002', '1_F_Waste_EXIOBASE2_Global_aggregated', '2_IUS_Vehicles_AllCountries_OICA_2017', '2_P_UN_WPP_Future_2100', '2_P_UN_WPP_Historic_2015', '3_IUP_Vehicles_9Countries_Dhaniati_2012', '3_LT_MaTraceGlobal_Pauliuk_2017', '3_MC_Buildings_Indonesia_Surahman_2014', '6_PCS_Vehicles_12Countries_Dhaniati_2012'
  - Cover sheet: Changed cell format to datetime for "access date"
  
- `1_UPI_USLCI_Aluminum_cold_rolling_at_plant`, `1_UPI_USLCI_Chainsawing_delimbing`, `1_UPI_USLCI_Limestone_at_mine`, `1_UPI_USLCI_Electricity_lignite_coal_at_power_plant`, `1_UPI_USLCI_steel_liquid_at_plant`, `2_IUS_Global_Materials_2050Scenario_Wiedenhofer_2019`, `1_F_WIO_Japan_Nakamura_Kondo_2002`
  - Cover sheet: Replaced "Flow" with 1 for data_category
  - Cover sheet: Added "0" for dataset_size 
    
  
## 14. Feb 2019

- `7_CT_EXIOBASEv3_200Products_To_163Products.xlsx`
  - Cover sheet, replaced "Correspondence Table" with "correspondence_table"

- `7_CT_EXIOBASEv3_163Products_To_163Industries.xlsx`:
  - Cover sheet, replaced "Correspondence Table" with "correspondence_table"
  
- Pushed latest version of IEDC_tools: https://github.com/IndEcol/IEDC_tools/commit/cf79057f6a026979414b34da1e99f9b0c140e160
  - Finished function to create dataset entries
  - All current files are being successfully processed
  - Smaller issues remain (e.g. need to implement checks vor dataset version number)
  - Function to update existing dataset entries not yet implemented


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


