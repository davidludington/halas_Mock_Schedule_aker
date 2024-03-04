# CSV Schedule builder
- This project was initiated because of my role as Fitness Supervisor Lead at my school's recreation center. One of my main roles as a Fitness Supervisor Lead is to build the schedule based on the availability indicated by the Fitness Supervisors at Halas. Because these are all student-held positions, the schedule must be built each semester around their class schedules and given availability. Since the schedule is frequently rebuilt, I saw a need for a tool to automate this task and thus make my role as FS lead more accurate and streamlined

## how to use
- change line 4 to match the exact name of you csv file
- save file
- create csv file with the csv format indicated below with the times that employess are NOT avalible to work
 
```bash
python3 ./schedule.py  
```
## CSV format 
- as of now the csv file you wish to build a schedule must be in the format of "Name, hours requested, Monday, Wednesday, Tuesday, Thursday, Friday, Saturday, Sunday"

## Required downloads
- Python - im using version Python 3.12.2
- pandas 
  
