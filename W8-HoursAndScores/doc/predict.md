# Predict Exam Score from Study Hours

## Objective
This project aims to predict exam scores based on the number of hours spent studying using a simple machine learning model.

## Dataset
You can use your own dataset in .csv format with Hours and Score columns.

## Choose a Model
Select Linear Regression as the prediction model because:
- The relationship between study hours and exam scores is approximately linear.

## Analyze and Visualize the Data (EDA)
```python
plt.scatter(Hours, Scores)
```

### Visualize the data and regression line

- **Visualize the data** means showing your data as a picture, usually by plotting points on a graph (called a scatter plot) so you can see how your data looks.
- **A regression line** is a straight line that best fits your data points. It shows the general trend or relationship between two things — for example, how exam scores change when study hours increase.
- **Combining both** means you plot the actual data points and draw the regression line on the same graph to see how well the line fits the data.

### Histogram
- A histogram is a type of bar chart that shows how data is distributed — it tells you how many data points fall into different ranges or “bins.”
- It groups your data into intervals and counts how many values fall into each interval.
- For example, it can show how many students studied between 1-2 hours, 2-3 hours, etc., or how many students scored between 60-70 points, 70-80 points, etc.

## Example Predict

### Import 

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
```

- Imports pandas as pd to handle table-like data using DataFrames.
- Imports matplotlib.pyplot as plt for plotting graphs.
- Imports seaborn for statistical data visualization (e.g., histograms with KDE curves).
- Imports the Linear Regression model from scikit-learn.
- Imports train_test_split to split the dataset into training and testing sets.
- Imports evaluation metrics: MAE, MSE, and R².
- Imports NumPy for numerical calculations (e.g., square roots).

### Load Data

```python
df = pd.read_csv("/HoursAndScores_100.csv")
df = df.loc[:, ['Hours', 'Scores']]
```

- Reads a CSV file named HoursAndScores_100.csv from the root directory /.
- Returns it as a DataFrame and assigns it to the variable df.
- The CSV should have at least the columns Hours and Scores.

### Define Features / Target and Split Data

```python
X = df[['Hours']]
y = df['Scores']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

- Sets X as the feature matrix containing the Hours column (kept as a DataFrame, not Series).
- Sets y as the target vector using the column Scores.
- Important: In the created data, the column is Score (no s). Using Scores will cause an error unless you rename the column or change this line.
- X_train
    - The features (input data, e.g., Hours studied) used to train the model.
    - This is the 80% (because test_size=0.2) portion of X selected for training.
- X_test
    - The features used to test the model after training.
    - This is the 20% portion of X reserved for evaluation.
- y_train
    - The target values (output data, e.g., Scores) corresponding to X_train.
    - Used by the model to learn the mapping from X_train → y_train.
- y_test
    - The target values corresponding to X_test.
    - Used to check how well the trained model performs on unseen data.
- Splits the data into 80% training and 20% testing.
- random_state=42 ensures the split is reproducible.

### Train the Model

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

- Creates a LinearRegression model object.
- Fits the model to the training data (learns slope and intercept).

### Predictions

```python
predections = model.predict(X_test)
```

- Predicts exam scores for the testing set.
- Variable name is misspelled — should be predictions, but kept as in the original file.

### Visualize — Scatter Plot + Regression Line

```python
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score')
plt.grid(True)
plt.legend()
plt.show()
```

- Creates a new plot with a specific size.
- Plots actual data points in blue.
- Plots the regression line in red, using predictions from the model for all X.
- Labels the axes, sets a title, enables gridlines, shows legend, and displays the plot.

### Histogram of Scores

```python
sns.histplot(data=df, x='Scores', bins=20, kde=True)
plt.title('Distribution of Exam Scores')
plt.xlabel('Score')
plt.grid(True)
plt.show()
```

- Plots a histogram of the Scores column with 20 bins and a KDE curve.
- Again, must ensure Scores exists in df.
- Titles the plot, labels the x-axis, enables gridlines, and shows the plot.


## Evaluate the Model
Check how accurate the model is using metrics like:
```python
| Metric                             | Description                                                        |
| ---------------------------------- | ------------------------------------------------------------------ |
| **MAE** (Mean Absolute Error)      | Average of absolute differences (no squaring)                      |
| **MSE** (Mean Squared Error)       | Average of squared differences                                     |
| **RMSE** (Root Mean Squared Error) | Square root of MSE (same units as the original target)             |
| **R²** (R-squared)                 | Proportion of variance explained by the model (ranges from 0 to 1) |
```

### MSE (Mean Squared Error)
- **What it is**: The average of the squared differences between actual and predicted values.
- **Pros**: Penalizes large errors more heavily.
- **Cons**: The result is in squared units, which can be harder to interpret.
- **Code**: mean_squared_error(y_test, predections)

### MAE (Mean Absolute Error)
- **What it is**: The average of the absolute differences between actual and predicted values.
- **Pros**: Not as sensitive to outliers as MSE/RMSE.
- **Cons**: Doesn’t penalize large errors as heavily.
- **Code**: mean_absolute_error(y_test , predections)

### RMSE (Root Mean Squared Error)
- **What it is**: The square root of the MSE, bringing the error back to the same unit as the target variable.
- **Pros**: Easier to interpret than MSE because it’s in the original scale.
- **Cons**: Still sensitive to outliers, like MSE.
- **Code**: rmse = np.sqrt(mean_squared_error(y_test, predections))

### R² Score (Coefficient of Determination)
- **What it is**: Indicates the proportion of variance in the dependent variable that is explained by the model.
- **Range**:
    1.0 → Perfect prediction
    0 → No better than predicting the mean
    Negative → Worse than predicting the mean
- **Pros**: Easy to understand as a percentage of explained variance.
- **Cons**: Doesn’t directly measure the size of the prediction errors.
- **Code**: r2_score(y_test, predections)

### Residuals

```python
Residuals = y_test - predections
Residuals
```

- Calculates residuals = actual values − predicted values.
- Displays the residuals.

### Final Fit on All Data & Add Columns

```python
final_model = LinearRegression()
final_model.fit(X,y)
y_hat = final_model.predict(X)
df['predection'] = y_hat
df['residual'] = df['Scores'] - df['predection']
df
```

- Creates a new LinearRegression model.
- Fits this model to the entire dataset.
- Predicts exam scores for all data points.
- Adds a new column predection to df containing the predicted scores (spelling kept from original).
- Adds a residual column = actual score − predicted score.
- Again, Scores must exist in df.
- Displays the full DataFrame with original data, predictions, and residuals.

## In Simple 
- Take the difference between predicted and actual values
- Square each difference
- Find the average of all squared errors

