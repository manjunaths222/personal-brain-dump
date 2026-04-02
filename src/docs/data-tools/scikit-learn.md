---
title: "Scikit Learn"
---

Scikit-Learn

Introduction: Open-source Python ML library built on NumPy, SciPy, and matplotlib.
Install: pip install scikit-learn

Key Features: Simple consistent API, wide range of ML models, preprocessing tools, efficient implementations.

Basic Workflow:
1. Import Libraries
2. Load Data
3. Data Preprocessing
4. Split Data (Training & Testing)
5. Model Training
6. Model Evaluation
7. Model Deployment

Preprocessing:
- Missing Data: SimpleImputer
- Encoding: OneHotEncoder, LabelEncoder
- Scaling: StandardScaler, MinMaxScaler

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.iloc[:, :-1])
```

Train/Test Split:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

Algorithms:
- Linear Regression: LinearRegression()
- Logistic Regression: LogisticRegression()
- Decision Tree: DecisionTreeClassifier(max_depth=3)
- Random Forest: RandomForestClassifier(n_estimators=100)
- KNN: KNeighborsClassifier(n_neighbors=5)
- SVM: SVC(kernel='linear')

Evaluation Metrics:
- Regression: mean_squared_error(), r2_score()
- Classification: accuracy_score(), confusion_matrix(), classification_report()

Hyperparameter Tuning:
```python
from sklearn.model_selection import GridSearchCV
params = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid_search = GridSearchCV(SVC(), params, cv=5)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
```

Pipelines:
```python
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SVC(kernel='linear'))
])
pipeline.fit(X_train, y_train)
```

Real-World Example (House Prices):
```python
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f'MSE: {mean_squared_error(y_test, y_pred):.2f}')
```
