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

## Train the Model
Fit the model with your training data:

```python
model.fit(x_train, y_train)
```
    - x_train = input (hours studied)
    - y_train = output (actual exam scores)

## Predictions
Use the trained model to predict new scores:

```python
model.predict([[6.5]])
```

    - Predicts the score of a student who studied for 6.5 hours

## Evaluate the Model
Check how accurate the model is using metrics like:
```python
| Metric                             | Description                                            |
| ---------------------------------- | ------------------------------------------------------ |
| **MAE** (Mean Absolute Error)      | Average of absolute differences (no squaring)          |
| **MSE** (Mean Squared Error)       | Average of squared differences                         |
| **RMSE** (Root Mean Squared Error) | Square root of MSE (same units as the original target) |
```

### MSE (Mean Squared Error)
    - **What it is**: The average of the squared differences between actual and predicted values.
    - **Pros**: Penalizes large errors more heavily.
    - **Cons**: The result is in squared units, which can be harder to interpret.

### MAE (Mean Absolute Error)
    - **What it is**: The average of the absolute differences between actual and predicted values.
    - **Pros**: Not as sensitive to outliers as MSE/RMSE.
    - **Cons**: Doesn’t penalize large errors as heavily.

### RMSE (Root Mean Squared Error)
    - **What it is**: The square root of the MSE, bringing the error back to the same unit as the target variable.
    - **Pros**: Easier to interpret than MSE because it’s in the original scale.
    - **Cons**: Still sensitive to outliers, like MSE.

### R² Score (Coefficient of Determination)

    - **What it is**: Indicates the proportion of variance in the dependent variable that is explained by the model.
    - **Range**:
            1.0 → Perfect prediction
            0 → No better than predicting the mean
            Negative → Worse than predicting the mean
    - **Pros**: Easy to understand as a percentage of explained variance.
    - **Cons**: Doesn’t directly measure the size of the prediction errors.

### In Simple 

    - Take the difference between predicted and actual values
    - Square each difference
    - Find the average of all squared errors

### Summary

    - Lower MSE = Better model (less error)
    - Units of MSE = Squared units of the target
        (e.g., if scores are in points, MSE is in point²)
