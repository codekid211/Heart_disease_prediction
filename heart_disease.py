# -*- coding: utf-8 -*-
"""Heart_Disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FHUkAfQo01uCvQ9N3GllHLo9kRcAsCkh

# Importing all the necessary libraries
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeRegressor

"""#Pre Processing The Data"""

heart = pd.read_csv('/content/heart.csv')

print(heart.head())
print(heart.isnull().sum())

heart.info()
def plot_selected_columns(heart, columns_to_plot):

    subset_data = heart[columns_to_plot]
    subset_data.plot(subplots=True, figsize=(25, 20))
    plt.show()

selected_columns = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'Oldpeak', 'MaxHR']
plot_selected_columns(heart, selected_columns)



plt.figure(figsize=(12, 8))
selected_columns = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'Oldpeak', 'MaxHR','HeartDisease']
correlation_matrix = heart[selected_columns].corr(numeric_only=True)
sns.heatmap(heart.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

"""#Spliting the Data into training and testing"""

X = heart.drop('HeartDisease', axis=1)
y = heart['HeartDisease']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


numerical_features = X.select_dtypes(include=['int64']).columns
numerical_transformer = StandardScaler()


categorical_features = X.select_dtypes(include=['object']).columns
categorical_transformer = OneHotEncoder()


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

"""Differnt models being used"""

models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=0),
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC(),


}

"""#Running Each Model and Checking the Best One"""

best_model_name = None
best_accuracy = 0.0

# Train and evaluate each model
for model_name, model in models.items():
    full_model = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('classifier', model)])

    full_model.fit(X_train, y_train)
    y_pred = full_model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    classification_report_str = classification_report(y_test, y_pred)
    confusion_mat = confusion_matrix(y_test, y_pred)

    print(f"Model: {model_name}")
    print(f"Accuracy: {accuracy:.4f}")
    print("Classification Report:")
    print(classification_report_str)
    print("Confusion Matrix:")
    print(confusion_mat)
    print("-" * 50)

    if accuracy > best_accuracy:
      best_accuracy = accuracy
      best_model_name = model_name

# Print the best model result
print(f"The best model is: {best_model_name} with an accuracy of {best_accuracy:.4f}")

"""#Plot the Actual vs Predicted Values"""

import plotly.graph_objs as go


for i in range(len(y_pred)):
    y_pred[i] = round(y_pred[i], 2)

results = pd.DataFrame({'Actual': y_test, 'Prediction': y_pred})
results['Difference'] = (results['Actual'] - results['Prediction']).round(4)


fig = go.Figure(data=[go.Table(
    header=dict(values=list(results.columns)),
    cells=dict(values=[results.Actual, results.Prediction, results['Difference']])
)])

table_trace = go.Table(
    header=dict(values=list(results.columns)),
    cells=dict(values=[results.Actual, results.Prediction, results['Difference']])
)

fig = go.Figure(data=[table_trace])


fig.update_layout(
    width=450,
    height=400
)


fig.show()

"""#Live prediction"""


while True:

    Age =int(input("Enter value for Age: "))
    Sex =(input("Enter value for Sex(M/F): "))
    ChestPainType =(input("Enter value for ChestPainType(ASY,ATA,NAP,TA): "))
    RestingBP = int(input("Enter value for RestingBP: "))
    Cholesterol = int(input("Enter value for Cholesterol: "))
    FastingBS = int(input("Enter value for FastingBS: "))
    RestingECG =(input("Enter value for RestingECG(LVH,Normal,ST): "))
    MaxHR = float(input("Enter value for MaxHR: "))
    ExerciseAngina =(input("Enter value for ExerciseAngina(Y/N): "))
    Oldpeak =float(input("Enter value for Oldpeak: "))
    ST_Slope =(input("Enter value for ST_Slope(Down,Flat,Up): "))



    user_input = {
        'Age': [Age],
        'Sex': [Sex],
        'ChestPainType':[ChestPainType],
        'RestingBP':[RestingBP],
        'Cholesterol':[Cholesterol],
        'FastingBS':[FastingBS],
        'RestingECG':[RestingECG],
        'MaxHR':[MaxHR],
        'ExerciseAngina':[ExerciseAngina],
        'Oldpeak':[Oldpeak],
        'ST_Slope':[ST_Slope]

    }


    user_input_df = pd.DataFrame(user_input)
    preprocessed_input = preprocessor.transform(user_input_df)


    best_model = models[best_model_name]
    user_prediction = best_model.predict(preprocessed_input)


    print(f"\nPrediction for the user input: {user_prediction[0]}\n")


    another_prediction = input("Do you want to make another prediction? (yes/no): ").lower()
    if another_prediction != 'yes':
        break