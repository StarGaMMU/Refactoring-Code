import os
import matplotlib.pyplot as plt

# Define the file paths
file_paths = ["before.py", "own.py","own2.py", "chat.py"]

# Initialize lists to store file sizes
file_sizes_mb = []

# Get the size of each file in MB
for file_path in file_paths:
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file_path)

    # Convert bytes to megabytes (MB)
    file_size_mb = file_size_bytes / (1024)  # Convert bytes to KB
    file_sizes_mb.append(file_size_mb)

# Plot the file sizes
plt.plot(file_paths, file_sizes_mb, marker='o')
plt.title('File Sizes')
plt.xlabel('File')
plt.ylabel('Size (KB)')
plt.grid(True)
plt.show()
