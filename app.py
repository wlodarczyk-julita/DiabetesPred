from flask import Flask, render_template, request, flash, session, redirect
import joblib
import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import calculate_bmi
import calculate_kcal
import psycopg2  
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

# Załaduj model SVM
# svm_model = joblib.load('svm_model.pkl')
app.secret_key = 'cairocoders-ednalan'
 
conn = psycopg2.connect(host='localhost', port=5433, database='Diabetes', user='postgres', password='postgres')




questions = [
    "Wybierz płeć:",
    "Wpisz swój wiek:",
    "Czy masz wysokie ciśnienie krwi?",
    "Wpisz swoje BMI. Możesz je obliczyć w zakładce BMI.",
    "Czy palisz papierosy?",
    "Czy uprawiasz jakąś aktywność fizyczną?",
    "Czy uwzględniasz w swojej diecie świeże owoce?",
    "Czy uwzględniasz w swojej diecie świeże warzywa?",
    "Jakie jest twoje ogólne samopoczucie w skali od 0 do 5?",
    "Jakie jest twoje psychiczne samopoczucie w skali od 0 do 30?",
    "Jakie jest twoje samopoczucie fizyczne w skali od 0 do 30?",
]
answers = []

questions_BMI = [
    "Podaj swoją wagę (kg):",
    "Podaj swój wzrost (m2):",
]

questions_KCAL = [
    "Podaj swoją wagę (kg):",
    "Podaj swój wzrost (m2):",
    "Podaj swój wiek (lata):",
    "Podaj swój styl życia:",
    "Podaj swoją płeć:",
]

answers_BMI = []
answers_KCAL = []
@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
 
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'sex' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        sex = request.form['sex']
    
        _hashed_password = generate_password_hash(password)
 
        #Check if account exists using MySQL
        # cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        # account = cursor.fetchone()
        # print(account)
        # # If account exists show error and validation checks
        # if account:
        #     flash('Account already exists!')
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #     flash('Invalid email address!')
        # elif not re.match(r'[A-Za-z0-9]+', username):
        #     flash('Username must contain only characters and numbers!')
        # elif not username or not password or not email:
        #     flash('Please fill out the form!')
        # else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
        cursor.execute("INSERT INTO users (fullname, username, password, email,sex) VALUES (%s,%s,%s,%s,%s)", (fullname, username, _hashed_password, email, sex))
        conn.commit()
        flash('You have successfully registered!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('register.html')




# @app.route('/form', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         user_answer = request.form['answer']
#         answers.append(user_answer)
        
#         if len(answers) < len(questions):
#             return render_template('test.html', question=questions[len(answers)])
#         else:
#             data = pd.DataFrame(columns=['Sex', 'Age', 'HighBP', 'BMI', 'Smoker', 'PhysActivity', 'Fruits', 'Veggies', 'GenHlth', 'MentHlth', 'PhysHlth'])
#             sex = answers[0]
#             age = answers[1]
#             highBP = answers[2]
#             bmi = answers[3]
#             smoker = answers[4]
#             physActivity = answers[5]
#             fruits = answers[6]
#             veggies = answers[7]
#             genHlth = answers[8]
#             mentHlth = answers[9]
#             physHlth = answers[10]
#             new_data = {'Sex': [sex], 'Age': [age], 'HighBP': [highBP], 'BMI':[bmi], 'Smoker': [smoker], 'PhysActivity':[physActivity], 'Fruits': [fruits], 'Veggies':[veggies], 'GenHlth':[genHlth], 'MentHlth':[mentHlth], 'PhysHlth':[physHlth] }
#             train_data = pd.read_csv('train.csv')

#             test_data = pd.read_csv('test.csv')

#             X_train = train_data.drop('Diabetes_012', axis=1)
#             y_train = train_data['Diabetes_012']


#             X_test = test_data.drop('Diabetes_012', axis=1)
#             y_test = test_data['Diabetes_012']

#             model = RandomForestClassifier()
#             model.fit(X_train, y_train)
#             data = pd.DataFrame(new_data, columns=X_train.columns)
#             prediction = model.predict(data)
#             # prediction = SVC.predict([answers])  
#             if prediction == 2:
#                 result = "Istnieje ryzyko, że jesteś chory na cukrzycę typu 2."
#             else:
#                 result = "Ryzyko cukrzycy typu 2 jest niskie."
#         print(result)
#             # return render_template('result.html', result=result)

    
#     return render_template('test.html', question=questions[0])


@app.route('/', methods=['GET','POST'])
def gender():
    return render_template('main.html')

@app.route('/bmi', methods=['GET','POST'])
def calculateBMI():
    if request.method == 'POST':
        req = request.form
        weight = req['question1']
        height = req['question2']
        age = req['question3']
        sex = req['question4']

        bmi = calculate_bmi.calculate_bmi.calculate_bmi(weight, height)
        bmiDescribe = calculate_bmi.calculate_bmi.describe_bmi(bmi,age,sex)
        print(bmi)
        print(bmiDescribe)
        return render_template('bmiSubmit.html', bmi=bmi, bmiDescribe=bmiDescribe)
    return render_template('bmi.html')

@app.route('/kcal', methods=['GET', 'POST'])
def calculateKcal():
    if request.method == 'POST':
        req = request.form
        weight = req['question1']
        height = req['question2']
        age = req['question3']
        lifestyle = req['question4']
        sex = req['question5']
        kcal = calculate_kcal.calculate_kcal.calculate_kcal(weight, height, age, lifestyle, sex)
        kcalRedu = kcal - 250
        kcalMass = kcal + 250
        print(weight, height, age, lifestyle, sex)
        print(kcal)
        return render_template('kcalSubmit.html', kcal=kcal, kcalRedu=kcalRedu, kcalMass=kcalMass)
    return render_template('kcal.html')


@app.route('/form', methods=['GET', 'POST'])
def calculate_k():
    if request.method == 'POST':
        req = request.form
        sex = req['sex']
        bmi = req['BMI']
        age = req['age']
        hp = req['hp']
        smoke = req['smoke']
        physActivity = req['physActivity']
        fruit = req['fruit']
        veggie = req['veggie']
        generalHealth = req['generalHealth']
        mentalHealth = req['mentalHealth']
        physHealth = req['physHealth']

        new_data = {'Sex': [sex], 'Age': [age], 'HighBP': [hp], 'BMI':[bmi], 'Smoker': [smoke], 'PhysActivity':[physActivity], 'Fruits': [fruit], 'Veggies':[veggie], 'GenHlth':[generalHealth], 'MentHlth':[mentalHealth], 'PhysHlth':[physHealth] }
        train_data = pd.read_csv('train.csv')

        test_data = pd.read_csv('test.csv')

        X_train = train_data.drop('Diabetes_012', axis=1)
        y_train = train_data['Diabetes_012']


        X_test = test_data.drop('Diabetes_012', axis=1)
        y_test = test_data['Diabetes_012']

        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        data = pd.DataFrame(new_data, columns=X_train.columns)
        prediction = model.predict(data)
        # prediction = SVC.predict([answers])  
        if prediction == 2:
            result = "Istnieje ryzyko, że jesteś chory na cukrzycę typu 2."
        else:
            result = "Ryzyko cukrzycy typu 2 jest niskie."
        print(result)
            # return render_template('result.html', result=result)
        return render_template('result.html')
    return render_template('test.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/sport')
def sport():
    return render_template('coursesSport.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/mental')
def mental():
    return render_template('mental.html')

@app.route('/pilates')
def pilates():
    return render_template('pilates.html')

@app.route('/sportAfter')
def sportAfter():
    return render_template('coursesSportAfter.html')

@app.route('/result')
def result():
    return render_template('result.html')

   













if __name__ == '__main__':
    app.run()