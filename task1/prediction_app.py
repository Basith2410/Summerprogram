import joblib
experience = float(input('Enter your experience (in years) : '))
model=joblib.load('salary_prediction_app.pk1')
result=model.predict([[experience]])
print(f'your monthly estimated salary is: {round(result[0])}')
