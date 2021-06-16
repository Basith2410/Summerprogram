import joblib
experience = float(input('Share your experience( in years ) : '))
model=joblib.load('salary_prediction_app.pk1')
result=model.predict([[experience]])
print(f'Estimated salary is: {round(result[0])}')