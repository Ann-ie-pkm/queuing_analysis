import pandas as pd

# Input data
data = {
    'Arrival Time': [0, 8, 14, 15, 23, 26, 34, 41, 43, 46, 47, 48, 53, 59, 62, 70, 71, 73, 77, 78],
    'Service Time': [4, 1, 4, 3, 2, 4, 5, 4, 5, 3, 3, 5, 4, 1, 5, 4, 3, 3, 2, 3]
}

df = pd.DataFrame(data)

# Initialize lists
queuing_time = []
exit_time = []
server_idle_time = []
total_time = []

exit = 0
for index, row in df.iterrows():
    arrival = row['Arrival Time']
    service = row['Service Time']
    
    # Server idle time
    idle = max(0, arrival - exit)
    server_idle_time.append(idle)
    
    # Queuing time
    queue = max(0, exit - arrival)
    queuing_time.append(queue)
    
    # Exit time
    exit = max(exit, arrival) + service
    exit_time.append(exit)
    
    # Total time
    total = queue + service
    total_time.append(total)

# Add to dataframe
df['Queuing Time'] = queuing_time
df['Exit Time'] = exit_time
df['Server Idle Time'] = server_idle_time
df['Total Time'] = total_time

print(df)
