

# About Tickets Issued Dataset

This dataset is issued by KSRTC. It is a State Road Transport Corporation.
## Organization : KSRTC

### BackGround of Organization

The Karnataka State Road Transport Corporation (KSRTC) is a state-owned road
transportation company catering to the different cities, towns and villages within and outside Karnataka. The corporation has the largest fleet of Volvo buses among the different state-owned transport companies in India. It is wholly owned by the Government of Karnataka.

### Services Provided by Organization
Services covers 92% villages in Karnataka. KSRTC operates with a total fleet of 23829 buses (KSRTC-8348, NEKRTC-4343, NWKRTC-4716, and BMTC–6422). It transports, on an average, 74.57 lakh passengers per day. It also operates to the neighbouring states of Maharashtra, Andhra Pradesh, Telangana, Tamil Nadu, Puducherry, Goa and Kerala. KSRTC was the first state transport corporation to introduce Volvo B7RLE low floor city buses in India in 2005. At present, KSRTC operates TATA, Ashok Leyland, Eicher Motors are More, Also Volvo, Mercedes Benz, Scania buses under the A/C (Airavat) services (Airavat means the mythical white elephant in Kannada).


## Dataset

- Dataset issued by KSRTC contains ticket issued to the passenger.
- Each row is the ticket issued to passenger. Though some observations contains route change of the bus and route direction change of the bus also.

### Structure of Dataset

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