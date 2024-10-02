if __name__ == '__main__':
    from memory_profiler import memory_usage
    import os
    import matplotlib.pyplot as plt

    # Define the paths to your scripts
    script_paths = ["before.py", "own.py", "own2.py", "chat.py"]
    script_names = ["Before", "Own", "Own2", "Chat"]

    # Create an empty list to store memory usage results for each script
    memory_usage_results = []

    def execute_code(x):
        os.system(f"python {x}")

    # Execute each script and measure its memory usage
    for script_path in script_paths:
        memory_usage_result = memory_usage(lambda: execute_code(script_path))
        memory_usage_results.append(memory_usage_result)

    # Plot memory usage for each script
    fig, ax = plt.subplots()

    for i, memory_usage_result in enumerate(memory_usage_results):
        ax.bar(script_names[i], max(memory_usage_result))

    # Set plot title and axis labels
    ax.set_title("Maximum Memory Usage")
    ax.set_xlabel("Script")
    ax.set_ylabel("Memory Usage (MB)")

    plt.show()