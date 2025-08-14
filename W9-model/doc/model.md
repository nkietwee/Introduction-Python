# Difference Between Classification and Regression

## Overview

In **machine learning**, both **classification** and **regression** are types of **supervised learning**.  
The main difference lies in the type of output variable:

- **Classification** → Predicts **categories or classes** (discrete values)
- **Regression** → Predicts **continuous numerical values**

---

## Classification

**Definition:**  
A model that predicts which category a given input belongs to.

**Example use cases:**
- Email spam detection (Spam / Not Spam)
- Disease diagnosis (Positive / Negative)
- Image recognition (Cat / Dog / Other)

**Model types for classification:**
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- Neural Network (for classification tasks)

## Classification Example

We will use the famous Iris dataset to classify flowers.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset from CSV
df = pd.read_csv("iris.csv")

# Separate features and labels
X = df.drop(columns=['label'])
y = df['label']

# Split dataset (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
clf = LogisticRegression(max_iter=200)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Show results
print("Classification Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

```

## Example Out

```python
Classification Accuracy: 1.0

Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00         9
           2       1.00      1.00      1.00        11

    accuracy                           1.00        30
   macro avg       1.00      1.00      1.00        30
weighted avg       1.00      1.00      1.00        30
```

---

## Regression

**Definition:**  
A model that predicts a continuous numerical value based on input features.

**Example use cases:**
- Predicting house prices
- Forecasting temperature
- Estimating sales revenue

**Model types for regression:**
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regression (SVR)
- Neural Network (for regression tasks)

## Regression Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset from CSV
df = pd.read_csv("california_housing.csv")

# Separate features and target
X = df.drop(columns=['MedHouseVal'])
y = df['MedHouseVal']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
reg = LinearRegression()
reg.fit(X_train, y_train)

# Predict
y_pred = reg.predict(X_test)

# Evaluate
print("Regression MSE:", mean_squared_error(y_test, y_pred))
```

## Example Output

```python
Regression MSE: 0.555891598695806
```

---

## Model for Predicting Last Values (Time Series)

Sometimes, we want to predict the **last or next value in a sequence**, often seen in **time series forecasting**.

**Definition:**  
A model trained on historical sequential data to predict future values.

**Example use cases:**
- Stock price prediction
- Weather forecasting
- Demand prediction

**Common models for time series prediction:**
- ARIMA / SARIMA
- Prophet (by Facebook)
- LSTM (Long Short-Term Memory Networks)
- GRU (Gated Recurrent Unit)
- XGBoost / LightGBM for time series

## Last Values (Time Series) Example

### Import

```python
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
```
- **from statsmodels.tsa.arima.model import ARIMA** → Brings in the ARIMA model class to build and train time series forecasting models.
- **from sklearn.metrics import mean_squared_error** → Brings in a function to measure prediction error (MSE/RMSE) between actual and predicted values.

### Load Data from CSV

```python
rng = pd.date_range("2020-01-01", periods=200, freq="D")
y = 0.05*np.arange(200) + 2*np.sin(np.arange(200)/6) + np.random.normal(0, 0.3, 200)
df = pd.DataFrame({"date": rng, "value": y})
df.to_csv("series.csv", index=False)
```
- pd.date_range(..., periods=200, freq="D") creates a sequence of 200 daily dates starting from 2020-01-01.
- y combines:
    - Trend: 0.05 * t
    - Seasonality: 2 * sin(t/6)
    - Noise: Gaussian noise N(0, 0.3)
- Saves the generated dataset to series.csv (you can skip this part if you already have a file).

```python
data = pd.read_csv("series.csv", parse_dates=["date"])
data = data.set_index("date").asfreq("D")
data = data.sort_index()
```

- parse_dates ensures the "date" column is treated as datetime.
- set_index("date") makes date the index.
- .asfreq("D") enforces a clear daily frequency.
- .sort_index() ensures the time order is correct.

### Train / Test Split

```python
train_ratio = 0.8
split_idx = int(len(data) * train_ratio)
train = data.iloc[:split_idx]["value"]
test  = data.iloc[split_idx:]["value"]
```

- Uses the first 80% of the data for training and the last 20% for testing.
- Important for time series: we split chronologically, not randomly.

### Build / Fit ARIMA Model

```python
model = ARIMA(train, order=(1,1,1))
fitted = model.fit()
```

- ARIMA(p,d,q) parameters:
    - p: Auto-Regressive (AR) order — number of lag observations used.
    - d: Differencing order — times the series is differenced to remove trend.
    - q: Moving Average (MA) order — number of lagged forecast errors in the model.
- Here (1,1,1) is a simple starting point (tunable in practice).

### Forecast

```python
forecast = fitted.forecast(steps=len(test))
```

- Predicts forward the same number of steps as the length of the test set.

### Evaluate

```python
rmse = mean_squared_error(test, forecast, squared=False)
```

- Computes Root Mean Squared Error (RMSE) — lower is better.
- RMSE is in the same units as the data.

### Print Results

```python
print("ARIMA summary:")
print(fitted.summary())
print("\nFirst 5 forecasted values:")
print(forecast.head())
print("\nRMSE on test:", rmse)
```

- fitted.summary() prints model coefficients, AIC/BIC scores, and diagnostics.
- Shows the first 5 forecasted values.
- Displays RMSE.

## 5. Summary Table

| Feature              | Classification                  | Regression                 | Time Series Prediction               |
|----------------------|---------------------------------|----------------------------|--------------------------------------|
| Output type          | Category / label (discrete)     | Continuous numeric value   | Continuous or discrete               |
| Examples             | Spam detection, image labeling  | House price, temperature   | Stock prices, sales forecasting      |
| Common algorithms    | Logistic Regression, SVM, RF    | Linear Regression, SVR, RF | ARIMA, LSTM, Prophet                 |
