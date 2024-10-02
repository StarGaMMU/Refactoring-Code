import timeit
import matplotlib.pyplot as plt
import importlib.util


# Function to execute code and measure time
def measure_execution_time(code):
    execution_time = timeit.timeit(stmt=code, number=1)
    return execution_time

# Function to calculate energy consumption
def calculate_energy_consumption(power, time):
    return power * time

# Example power consumption in watts (replace with actual values)
power_consumption_watts = 10

# Script paths and names
script_paths = ["before.py", "own.py", "own2.py", "chat.py"]
script_names = ["Before", "Own", "Own2", "Chat"]

# Create an empty list to store execution times
execution_times = []

# Measure execution time for each script
for script_path in script_paths:
    # Read the content of the script
    with open(script_path, 'r') as file:
        code = file.read()

    # Measure execution time
    time_taken = measure_execution_time(code)
    execution_times.append(time_taken)

# Calculate energy consumption for each script
energies = [calculate_energy_consumption(power_consumption_watts, time) for time in execution_times]

# Plotting
plt.bar(script_names, energies, color=['blue', 'green', 'orange', 'red'])
plt.xlabel('Script')
plt.ylabel('Energy Consumption (Joules)')
plt.title('Energy Consumption Comparison')
plt.show()
