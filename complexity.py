import os
import matplotlib.pyplot as plt
from radon.complexity import cc_visit


def calculate_complexity(file_name):
    complexity = 0
    try:
        with open(file_name, 'r') as file:
            code = file.read()
            results = cc_visit(code)
            for result in results:
                complexity += result.complexity
    except Exception as e:
        print(f"Error occurred during complexity calculation for {file_name}: {e}")
    return complexity


def plot_complexity(files, complexities):
    """Plot the Cyclomatic Complexity for each file."""
    plt.bar(files, complexities)
    plt.xlabel('File')
    plt.ylabel('Cyclomatic Complexity')
    plt.title('Cyclomatic Complexity of Python Files')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    files = ["before.py", "own.py", "own2.py", "chat.py"]
    complexities = []

    for file_name in files:
        if os.path.exists(file_name):
            complexity = calculate_complexity(file_name)
            complexities.append(complexity)
            print(f"Cyclomatic Complexity of {file_name}: {complexity}")
        else:
            print(f"File not found: {file_name}")

    plot_complexity(files, complexities)


"""1–10
    Considered ideal, this range is easy to understand and maintain, and testing is more straightforward.
10–20
    Indicates moderate complexity, which is manageable, but rigorous testing and code reviews are important.
20–40
    Considered a high level of complexity, this range can be challenging to understand and test properly.
>40
    Extremely complex and should be avoided."""