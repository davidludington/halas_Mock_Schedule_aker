import pandas as pd

# Read data from CSV file
df = pd.read_csv('SampleScheduleInput.csv')

# Define shift timings
shift_timings = {

    'Monday': ['6:30-10', '10-1', '1-5', '5-8', '8-11:30'],
    'Tuesday': ['6:30-10', '10-1', '1-5', '5-8', '8-11:30'],
    'Wednesday': ['6:30-10', '10-1', '1-5', '5-8', '8-11:30'],
    'Thursday': ['6:30-10', '10-1', '1-5', '5-8', '8-11:30'],
    'Friday': ['6:30-10', '10-1', '1-5', '5-8', '8-11:30'],
    'Saturday': ['7:45-11', '11-2', '2-5', '5-9'],
    'Sunday': ['7:45-11', '11-2', '2-5', '5-9']
}

# Initialize mock schedule dataframe
mock_schedule = pd.DataFrame(columns=['Name', 'Shifts'])

# Iterate over each employee's preferences
for index, row in df.iterrows():
    name = row['Name']
    
    # Iterate over each day
    for day, timings in shift_timings.items():
        for timing in timings:
            start_time, end_time = timing.split('-')
            # Check if the employee is available during this shift
            if start_time >= row[day] and end_time <= row[day]:
                mock_schedule = mock_schedule._append({'Name': name, 'Shift': f'{day} {timing}'}, ignore_index=True)



# Output mock schedule
print(mock_schedule)
