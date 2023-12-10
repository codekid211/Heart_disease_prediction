
# Heart Disease Predicition

Introducing AI.works, the ultimate remote work companion. A platform for efficient productivity tracking, multilingual meeting assistance, and engaging in insightful content discussions with our intelligent chatbot – your all-in-one solution for efficient digital collaboration.

## Dataset
This project utilizes the heart failure prediction dataset from Kaggle, available [here](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction). The dataset provides a comprehensive set of features for predicting heart failure, forming the foundation for our explorations.

## Project Breif
![architecture](assets/PA.jpg)

Workflow:
Data Splitting:

We partition the dataset into training and testing subsets to evaluate model performance effectively.

Model Training:
Employing Random Forest, Decision Tree, Support Vector Machine, and Logistic Regression models for heart disease prediction.

Model Evaluation:
Assessing the predictive power of each model on the test set.

Identifying the Best Model:
Comparing model performances to determine the most effective predictor.

Live Predictions:
Deploying the best model, Random Forest in this case, for predictions with real-world values.

## Deployment

To deploy this project run

First clone the repo

Then install the following libraries
```python
pip install -r requirements.txt
```
You also require API keys for the following
- huggingface
- Fitbit

After install all the dependencies 
```bash
- open cmd and run
- python Heart_Disease.py
```

## Screenshots

![Result of Random forest](assets/RF.png)
![Result of Decision Tree](assets/DT.png)
![Result of Logistic Regression](assets/LR.png)
![Result of SVM](assets/SVM.png)

## Contribution
If you have ideas for improvement or wish to contribute, please open an issue or submit a pull request. Collaboration is highly encouraged!
