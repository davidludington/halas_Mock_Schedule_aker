import pandas as pd

# Read data from CSV file
df = pd.read_csv('SampleScheduleInput.csv')

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
mock_schedule = pd.DataFrame(columns=['Name', 'Day', 'Shifts'])

# Iterate over each employee's preferences
for index, row in df.iterrows():
    name = row['Name']
    #iterate over shifts during that day
    for day, timings in shift_timings.items():
        for timing in timings:
            start_time, end_time = timing.split('-')
            if start_time >= row[day] and end_time <= row[day]:
                mock_schedule = mock_schedule._append({'Name': name, 'Day': day, 'Shifts': f'{day} {timing}'}, ignore_index=True)

# Sort DataFrame by the order of days
custom_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mock_schedule['Day'] = pd.Categorical(mock_schedule['Day'], categories=custom_order, ordered=True)
mock_schedule = mock_schedule.sort_values('Day')

def print_schedule(schedule_df):
    # Group the DataFrame by day of the week
    grouped_schedule = schedule_df.groupby('Day')
    
    # Iterate over each group (day of the week)
    for day, group in grouped_schedule:
        print(day + ':')
        # Iterate over each row (shift) in the group
        for index, row in group.iterrows():
            print(f"    {row['Shifts']} - {row['Name']}")



# Output mock schedule
print_schedule(mock_schedule)
