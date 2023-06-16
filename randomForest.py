import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datetime import date

def calculate_age(date_of_birth):
    year, month, day = map(int, date_of_birth.split('-'))
    current_date = date.today()
    age = current_date.year - year
    if current_date.month < month or (current_date.month == month and current_date.day < day):
        age -= 1
    
    return age


train_data = pd.read_csv('train.csv')

test_data = pd.read_csv('test.csv')

X_train = train_data.drop('Diabetes_012', axis=1)
y_train = train_data['Diabetes_012']


X_test = test_data.drop('Diabetes_012', axis=1)
y_test = test_data['Diabetes_012']

model = RandomForestClassifier()


model.fit(X_train, y_train)


y_pred = model.predict(X_test)

new_data = pd.DataFrame([[1.0,7.0,1.0,19.0,1.0,0.0,0.0,1.0,5.0,25.0,25.0]], columns=X_train.columns)
prediction = model.predict(new_data)
print("Przewidywany status cukrzycowy:", prediction)