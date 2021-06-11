import joblib
experience = float(input('Enter your experience : '))
model=joblib.load('salary_prediction_app.pk1')
result=model.predict([[experience]])
print(f'This is your predicted salary: {round(result[0])}')
