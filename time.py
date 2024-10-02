import timeit
import matplotlib.pyplot as plt

# Specify the file names
file_names = ['before.py', 'own.py','own2.py', 'chat.py']

# Initialize lists to store execution times
execution_times = []

# Iterate over the file names
for file_name in file_names:
    # Read the contents of the file
    with open(file_name, 'r') as file:
        code = file.read()

    # Measure the execution time of the code in the file
    time_taken = timeit.timeit(stmt=code, number=1000)
    execution_times.append(time_taken)
    print("Execution time of", file_name, ":", time_taken)

# Plot the execution times
plt.bar(file_names, execution_times, color=['red', 'blue', 'green','yellow'])
plt.xlabel('File Name')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Each File')
plt.show()
