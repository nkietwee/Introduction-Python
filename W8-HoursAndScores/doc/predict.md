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
   
    - Plot a scatter graph to explore the relationship between hours and scores.
    - Check if the relationship is linear.

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
    - Mean Squared Error (MSE)
    - R² Score (closer to 1 is better)

### Mean Squared Error (MSE)
MSE (Mean Squared Error) is a metric used to evaluate the accuracy of regression models.
It tells us how far off the model’s predictions are from the actual values — on average — by squaring the errors.


### In Simple 
    - Take the difference between predicted and actual values
    - Square each difference
    - Find the average of all squared errors

### Summary
    - Lower MSE = Better model (less error)
    - Units of MSE = Squared units of the target
        (e.g., if scores are in points, MSE is in point²)
