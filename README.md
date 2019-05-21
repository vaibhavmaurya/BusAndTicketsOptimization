
# Tickets Issued Dataset

## Table of contents
1. [About Tickets Issued Dataset](#AboutTicketData)
    1. [BackGround of Organization](#OrgBackground)
    2. [Services Provided by Organization](#OrgServices)
    3. [Dataset Info.](#DatasetInfo)
    4. [Structure of Dataset](#DataSetStructure)
2. [Data Wrangling](#datawrangling)
    1. [Gathering Data](#gatherdata)
3. [How to run this project](#run)

## About Tickets Issued Dataset <a name="AboutTicketData"></a>

This dataset is issued by organization KSRTC. It is a State Road Transport Corporation.

### BackGround of Organization <a name="OrgBackground"></a>

The Karnataka State Road Transport Corporation (KSRTC) is a state-owned road
transportation company catering to the different cities, towns and villages within and outside Karnataka. The corporation has the largest fleet of Volvo buses among the different state-owned transport companies in India. It is wholly owned by the Government of Karnataka.

### Services Provided by Organization <a name="OrgServices"></a>
Services covers 92% villages in Karnataka. KSRTC operates with a total fleet of 23829 buses (KSRTC-8348, NEKRTC-4343, NWKRTC-4716, and BMTC–6422). It transports, on an average, 74.57 lakh passengers per day. It also operates to the neighbouring states of Maharashtra, Andhra Pradesh, Telangana, Tamil Nadu, Puducherry, Goa and Kerala. KSRTC was the first state transport corporation to introduce Volvo B7RLE low floor city buses in India in 2005. At present, KSRTC operates TATA, Ashok Leyland, Eicher Motors are More, Also Volvo, Mercedes Benz, Scania buses under the A/C (Airavat) services (Airavat means the mythical white elephant in Kannada).


### Dataset Info. <a name="DatasetInfo"></a>

- Dataset issued by KSRTC contains ticket issued to the passenger.
- Each row is the ticket issued to passenger. Though some observations contains route change of the bus and route direction change of the bus also.

### Structure of Dataset <a name="DataSetStructure"></a>

|  Column Name | Description  |
| ------------ | ------------ |
| ETD_WAYBILL_NO   | Indetifier for Bus  |
| ETD_ROUTE_NO   | Identifier for the current route of the bus  |
|  ETD_ROUTE_TYPE  | Type of route  |
| ETD_TRIP_NO   | Indetifier for the current trip of a bus for agiven route  |
|  ETD_TICKET_TYPE  | Type of ticket sold  |
| ETD_ADULTS   | No of adults boarded the bus  |
| ETD_CHILD   |  No of kids boarded the bus |
|  ETD_AMOUNT  | Expense beared for a ticket sold  |
| ETD_DEPOT_CODE   | Depot for which this belongs  |
| ETD_BATTERY_VOLT   | Battery voltage  |
| ETD_CUR_STOP_NAME   | Name of the current stop from where passenger has boarded  |
| ETD_DST_STOP_NAME   | Name of the current stop from where passenger has hop off  |
| ETD_KMS   | Distance between source bus stop and destination bus stop  |
| ETD_TICKET_TYPE_DESCR   | Description of the type of the ticket sold  |
| ETD_TRIP_DIRECTION   | Direction of a route  |
| ETD_TICKET_NO   | Identfier for the ticket sold  |
| ETD_TICKET_SUBNO   |  Sub Identfier for the ticket sold |
| ETD_CUR_STOP_NO   |  No assigned to the current bus stop for a given route |
| ETD_CUR_STOP_CODE   | Code assigned to the current bus stop for a given route |
| ETD_DST_STOP_NO   | No assigned to the destination bus stop for a given route  |
| ETD_DST_STOP_CODE   | Code assigned to the destination bus stop for a given route  |
| ETD_CUR_SUB_STAGE   | Sub stage assigned to the current bus stop for a given route  |
| ETD_DST_SUB_STAGE   | Sub stage assigned to the destination bus stop for a given route  |
| ETD_DATE  | Date of the ticket issued  |
| ETD_TD_TIME  | Time of the ticket issued  |


## Data Wrangling <a name="datawrangling"></a>

Dataset url : [full_data.zip](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/data/full_data.zip)

This archived file contains a text file named `aug18-dec18.txt`.

This dataset is paginated and contains unnecessary strings as follows.
![](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/images/datapreview.png)

#### Challenges in the dataset
This dataset has following issues:

- Dataset is in a flat text file. It is paginated, 21 rows per page, though all pages are in the same text file seperated by new line.
- Columns in the dataset are not fully qualified names. Each column is seperated by space.
- Size of a column is difficult to determine.
- The text files contains some additional strings in the begining and in the end also.

Fortunately this dataset has following pros.

- Dataset columns positions are fixed throughout the dataset.
- Each page is uniformly seperated by newline throughout the dataset.

### Gathering Data <a name="gatherdata"></a>

To parse dataset into csv, following is the strategy opted:

- Created a [json file](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/src/datastructure.json) to parse text dataset. This json file contains column name as key and value is the object which contains start of the column, size of the column and position of the column.
- Created a [library](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/src/DataProcessingModule.py) to clean the dataset.

The program follows the logic as below.

![](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/images/DataCleaning.png)

Data is gathered in the [notebook](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/notebooks/Data_Wrangling.ipynb).


## How to run this project <a name="run"></a>

1. Download this project to local.
2. Extract data [zip file](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/data/full_data.zip)
3. Create 4 folders inside the [data](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/tree/master/data) folder: `clean_data`, `db`, `processed`, and `raw`.
4. Copy file aug18-dec18.txt from extracted folder `full_data` to folder `raw`
5. Run jupyter notebook [Data_Wrangling.ipynb](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/notebooks/Data_Wrangling.ipynb).
6. For data analysis run jupyter notebook [PassengersDistributionAnalysis.ipynb](https://github.com/vaibhavmaurya/BusAndTicketsOptimization/blob/master/notebooks/PassengersDistributionAnalysis.ipynb)


