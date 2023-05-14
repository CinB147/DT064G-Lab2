import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



#Quadratic function
def f(x, a): #O(n)
    return a * x*2

def fsq(x, a): #O(n^2)
    return a * x**2

def flog(x, a, b): #O(nlog(n))
    return a * (x * np.log(x)) + b

def read_file(filename):
    num_elements = []
    time_ms = []
    standard_deviation = []

    with open(filename, "r") as file:
        for line in file:
            values = line.split()
            num_elements.append(int(values[0]))
            time_ms.append(float(values[1]))
            standard_deviation.append(float(values[2]))

    return num_elements, time_ms, standard_deviation



#------------------INSERTION_random----------------#

# Load data from the file using the read_file function
x_insert1, y_insert1, y_erinsert1 = read_file('SortAlgoritm/Insertionsort/Random.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_insert1, y_insert1)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Insertion Sort Random- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_insert1, y_insert1, yerr=y_erinsert1, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_insert1), np.max(x_insert1), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Insertionsort/Random.png")
# Show the plot
plt.show()

#------------------INSERTION_constant----------------#

# Load data from the file using the read_file function
x_insert2, y_insert2, y_erinsert2 = read_file('SortAlgoritm/Insertionsort/Constant.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(f, x_insert2, y_insert2)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Insertion Sort Constant - Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_insert2, y_insert2, yerr=y_erinsert2, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_insert2), np.max(x_insert2), 1000)
y_fit = f(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Insertionsort/Constant.png")
# Show the plot
plt.show()

#------------------INSERTION_Rising----------------#

# Load data from the file using the read_file function
x_insert3, y_insert3, y_erinsert3 = read_file('SortAlgoritm/Insertionsort/Rising.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(f, x_insert3, y_insert3)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Insertion Sort Rising - Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_insert3, y_insert3, yerr=y_erinsert3, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_insert3), np.max(x_insert3), 1000)
y_fit = f(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Insertionsort/Rising.png")
# Show the plot
plt.show()

#------------------INSERTION_Falling----------------#

# Load data from the file using the read_file function
x_insert4, y_insert4, y_erinsert4 = read_file('SortAlgoritm/Insertionsort/Falling.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(f, x_insert4, y_insert4)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Insertion Sort Falling - Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_insert4, y_insert4, yerr=y_erinsert4, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_insert4), np.max(x_insert4), 1000)
y_fit = f(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Insertionsort/Falling.png")
# Show the plot
plt.show()


#------------------SELECTION_random----------------#

# Load data from the file using the read_file function
x_select1, y_select1, y_erselect1 = read_file('SortAlgoritm/SelectionSort/Random.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_select1, y_select1)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Selection Sort Random- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_select1, y_select1, yerr=y_erselect1, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_select1), np.max(x_select1), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/SelectionSort/Random.png")
# Show the plot
plt.show()

#------------------SELECTION_Const----------------#

# Load data from the file using the read_file function
x_select2, y_select2, y_erselect2 = read_file('SortAlgoritm/SelectionSort/Constant.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_select2, y_select2)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Selection Sort Constant- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_select2, y_select2, yerr=y_erselect2, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_select2), np.max(x_select2), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/SelectionSort/Constant.png")
# Show the plot
plt.show()

#------------------SELECTION_Rising----------------#

# Load data from the file using the read_file function
x_select3, y_select3, y_erselect3 = read_file('SortAlgoritm/SelectionSort/Rising.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_select3, y_select3)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Selection Sort Rising- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_select3, y_select3, yerr=y_erselect3, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_select3), np.max(x_select3), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/SelectionSort/Rising.png")
# Show the plot
plt.show()

#------------------SELECTION_Falling----------------#

# Load data from the file using the read_file function
x_select4, y_select4, y_erselect4 = read_file('SortAlgoritm/SelectionSort/Falling.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_select4, y_select4)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Selection Sort Falling- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_select4, y_select4, yerr=y_erselect4, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_select4), np.max(x_select4), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/SelectionSort/Falling.png")
# Show the plot
plt.show()


#------------------QuickSort_random----------------#

# Load data from the file using the read_file function
x_quick1, y_quick1, y_erquick1 = read_file('SortAlgoritm/QuickSort/Random.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(f, x_quick1, y_quick1)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quick Sort Random- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quick1, y_quick1, yerr=y_erquick1, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quick1), np.max(x_quick1), 1000)
y_fit = f(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/QuickSort/Random.png")
# Show the plot
plt.show()

#------------------QuickSort_Constant----------------#

# Load data from the file using the read_file function
x_quick2, y_quick2, y_erquick2 = read_file('SortAlgoritm/QuickSort/Constant.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quick2, y_quick2)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quick Sort Constant- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quick2, y_quick2, yerr=y_erquick2, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quick2), np.max(x_quick2), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/QuickSort/Constant.png")
# Show the plot
plt.show()

#------------------QuickSort Rising----------------#

# Load data from the file using the read_file function
x_quick3, y_quick3, y_erquick3 = read_file('SortAlgoritm/QuickSort/Rising.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quick3, y_quick3)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quick Sort Rising- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quick3, y_quick3, yerr=y_erquick3, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quick3), np.max(x_quick3), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/QuickSort/Rising.png")
# Show the plot
plt.show()

#------------------QuickSort Falling----------------#

# Load data from the file using the read_file function
x_quick4, y_quick4, y_erquick4 = read_file('SortAlgoritm/QuickSort/Falling.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quick4, y_quick4)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quick Sort Falling- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quick4, y_quick4, yerr=y_erquick4, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quick4), np.max(x_quick4), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/QuickSort/Falling.png")
# Show the plot
plt.show()

#------------------QuickSortMid Random----------------#

# Load data from the file using the read_file function
x_quickmid1, y_quickmid1, y_erquickmid1 = read_file('SortAlgoritm/Quicksort median-of-three/Random.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(flog, x_quickmid1, y_quickmid1)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quicksort median-of-three Random- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quickmid1, y_quickmid1, yerr=y_erquickmid1, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quickmid1), np.max(x_quickmid1), 1000)
y_fit = flog(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Quicksort median-of-three/Random.png")
# Show the plot
plt.show()

#------------------QuickSortMid Const----------------#

# Load data from the file using the read_file function
x_quickmid2, y_quickmid2, y_erquickmid2 = read_file('SortAlgoritm/Quicksort median-of-three/Constant.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quickmid2, y_quickmid2)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quicksort median-of-three Constant- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quickmid2, y_quickmid2, yerr=y_erquickmid2, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quickmid2), np.max(x_quickmid2), 1000)
y_fit = fsq(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Quicksort median-of-three/Constant.png")
# Show the plot
plt.show()


#------------------QuickSortMid Rising----------------#

# Load data from the file using the read_file function
x_quickmid3, y_quickmid3, y_erquickmid3 = read_file('SortAlgoritm/Quicksort median-of-three/Rising.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quickmid3, y_quickmid3)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quicksort median-of-three Rising- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quickmid3, y_quickmid3, yerr=y_erquickmid3, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quickmid3), np.max(x_quickmid3), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Quicksort median-of-three/Rising.png")
# Show the plot
plt.show()

#------------------QuickSortMid Falling----------------#

# Load data from the file using the read_file function
x_quickmid4, y_quickmid4, y_erquickmid4 = read_file('SortAlgoritm/Quicksort median-of-three/Falling.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(fsq, x_quickmid4, y_quickmid4)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("Quicksort median-of-three Falling- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_quickmid4, y_quickmid4, yerr=y_erquickmid4, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_quickmid4), np.max(x_quickmid4), 1000)
y_fit = fsq(x_fit, params[0])
plt.plot(x_fit, y_fit, label="O(n^2)", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/Quicksort median-of-three/Falling.png")
# Show the plot
plt.show()

#------------------std::sort Random----------------#

# Load data from the file using the read_file function
x_stdsort1, y_stdsort1, y_erstdsort1 = read_file('SortAlgoritm/std_sort/Random.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(flog, x_stdsort1, y_stdsort1)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("std::sort Random- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_stdsort1, y_stdsort1, yerr=y_erstdsort1, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_stdsort1), np.max(x_stdsort1), 1000)
y_fit = flog(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/std_sort/Random.png")
# Show the plot
plt.show()


#------------------std::sort Const----------------#

# Load data from the file using the read_file function
x_stdsort2, y_stdsort2, y_erstdsort2 = read_file('SortAlgoritm/std_sort/Constant.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(flog, x_stdsort2, y_stdsort2)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("std::sort Constant- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_stdsort2, y_stdsort2, yerr=y_erstdsort2, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_stdsort2), np.max(x_stdsort2), 1000)
y_fit = flog(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/std_sort/Constant.png")
# Show the plot
plt.show()

#------------------std::sort Rising----------------#

# Load data from the file using the read_file function
x_stdsort3, y_stdsort3, y_erstdsort3 = read_file('SortAlgoritm/std_sort/Rising.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(flog, x_stdsort3, y_stdsort3)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("std::sort Rising- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_stdsort3, y_stdsort3, yerr=y_erstdsort3, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_stdsort3), np.max(x_stdsort3), 1000)
y_fit = flog(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/std_sort/Rising.png")
# Show the plot
plt.show()

#------------------std::sort Falling----------------#

# Load data from the file using the read_file function
x_stdsort4, y_stdsort4, y_erstdsort4 = read_file('SortAlgoritm/std_sort/Falling.txt')

# Fit the quadratic function to the data
params, _ = curve_fit(flog, x_stdsort4, y_stdsort4)

# Create the plot
plt.figure(figsize=(7, 4))
plt.title("std::sort Falling- Time Complexity Analysis")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (ms)")
plt.grid(True)
# Plot the data with error bars
plt.errorbar(x_stdsort4, y_stdsort4, yerr=y_erstdsort4, fmt='o', label="Measured Time")
# Plot the fit
x_fit = np.linspace(np.min(x_stdsort4), np.max(x_stdsort4), 1000)
y_fit = flog(x_fit, *params)
plt.plot(x_fit, y_fit, label="O(nlog(n))", color='r')
plt.legend()
# Save the plot to a file
plt.savefig("SortAlgoritm/std_sort/Falling.png")
# Show the plot
plt.show()