import timeit
import matplotlib.pyplot as plt

# Define the functions or code blocks to benchmark in each file
functions_to_benchmark = [
    'main()',  # Assuming each file has a main function
    # Add more functions or code blocks to benchmark if needed
]

# Specify the file names
file_names = ['before.py', 'own.py', 'own2.py', 'chat.py']

# Initialize lists to store execution times
execution_times = []

# Iterate over the file names
for file_name in file_names:
    # Read the contents of the file
    with open(file_name, 'r') as file:
        code = file.read()

    # Measure the execution time of each function or code block
    total_time = 0
    for func in functions_to_benchmark:
        time_taken = timeit.timeit(stmt=func, setup=code, number=1000)
        total_time += time_taken

    execution_times.append(total_time)
    print("Execution time of", file_name, ":", total_time)

# Plot the execution times
plt.bar(file_names, execution_times, color=['red', 'blue', 'green', 'yellow'])
plt.xlabel('File Name')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Each File')
plt.show()