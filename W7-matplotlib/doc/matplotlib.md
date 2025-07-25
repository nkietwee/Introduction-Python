
# Matplotlib Lesson Plan for Students

## 1. Introduction to Matplotlib
- **What is Matplotlib?**
  Matplotlib is a widely-used Python library for creating static, animated, and interactive visualizations in Python. It provides a variety of plotting functions to visualize data in a meaningful way, such as line plots, scatter plots, histograms, bar charts, etc.

- **Why use Matplotlib?**
  It helps us to quickly understand data patterns and trends through various plot types, and it integrates well with other libraries like NumPy and Pandas for numerical computations.

## 2. Setting Up
- To install Matplotlib, students will run:
  ```bash
  pip install matplotlib
  ```
  This installs the latest version of Matplotlib in your environment.

- To use Matplotlib in Python code:
  ```python
  import matplotlib.pyplot as plt
  ```
  `plt` is the standard alias used for Matplotlib's PyPlot interface, which is easier to use for creating plots.

## 3. Basic Plotting
- **Line Plot:**
  A line plot is used to visualize continuous data. The function `plt.plot(x, y)` plots the values in `x` against `y`. For example:
  ```python
  plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # x-values: 1, 2, 3, 4, y-values: 1, 4, 9, 16
  plt.show()  # Display the plot
  ```
  ```python
  x = (0, 2, 4, 6, 8)
  y = (0, 2, 4, 6, 8)
  plt.plot(x, y)
  plt.show()
  ```
  This will display a simple line graph.

- **Scatter Plot:**
  Scatter plots are used to visualize relationships between two continuous variables by displaying points at their coordinates. Example:
  ```python
  plt.scatter([1, 2, 3], [4, 5, 6])
  plt.show()
  ```

## 4. Customizing Plots
- **Titles, Labels, and Gridlines:**
  You can add descriptive elements to your plot, like a title and labels for both the x and y axes. Example:
  ```python
  plt.plot([1, 2, 3], [4, 5, 6])
  plt.title('Sample Plot')  # Title for the plot
  plt.xlabel('X Axis')  # Label for the x-axis
  plt.ylabel('Y Axis')  # Label for the y-axis
  plt.grid(True)  # Display gridlines
  plt.show()
  ```

- **Line Style and Color:**
  You can change the color, style, and marker type in your plot:
  ```python
  plt.plot([1, 2, 3], [4, 5, 6], color='red', linestyle='--', marker='o')
  plt.show()
  ```
  - `color='red'` changes the color of the line.
  - `linestyle='--'` makes the line dashed.
  - `marker='o'` marks each data point with a circle.
ref : https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

## 5. Multiple Plots
- **Subplots:**
  You can have multiple plots in the same figure using `subplots()`:
  ```python
  fig, ax = plt.subplots(2, 2)  # 2 rows, 2 columns of plots
  ax[0, 0].plot([1, 2, 3], [4, 5, 6])  # Top-left plot
  ax[0, 1].scatter([1, 2, 3], [6, 7, 8])  # Top-right plot
  plt.show()
  ```
  `fig`: This is the figure object that holds all the subplots.

  `ax`: This is a 2D NumPy array that contains axes objects for each subplot. ax[0, 0] refers to the subplot in the first row, first column (top-left), and ax[0, 1] refers to the subplot in the first row, second column (top-right).
  This creates a grid of subplots where you can plot different types of data in each subplot.

## 6. Another Visualizations
- **Histograms:**
  Histograms display the distribution of a dataset. They group data into bins. Example:
  ```python
  plt.hist([1, 2, 1, 1, 3, 3, 4, 4, 4], bins=4)  # Data and number of bins
  plt.show()
  ```
  This will show the distribution of the numbers in your dataset, divided into 4 bins.

- **Bar Charts:**
  Bar charts are used to show comparisons between categories:
  ```python
  plt.bar([1, 2, 3], [4, 5, 6])  # Categories and their values
  plt.show()
  ```

## 7. Working with Data
- **Pandas Integration:**
  Matplotlib works well with Pandas DataFrames, making it easy to plot data directly from a table. Example:
  ```python
  import pandas as pd
  df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
  df.plot(kind='bar')  # Bar chart from the DataFrame
  plt.show()
  ```

## 8. Customization with Styles
- You can change the overall style of the plot using pre-built themes, such as `ggplot` or `seaborn`:
  ```python
  plt.style.use('ggplot')  # Using the 'ggplot' style
  ```
  ref : https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

## 9. Saving Figures
- After generating a plot, you can save it to a file:
  ```python
  plt.plot([1, 2, 3], [1, 4, 9])
  plt.savefig('plot.png')  # Save the plot as a PNG image
  ```

## 10. Practical Examples and Exercises
- **Real-World Examples:**
  You can show how Matplotlib is useful in different fields such as finance (stock prices), scientific research (experiment results), or social media (user engagement over time).

---