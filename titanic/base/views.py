from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):
    model = pickle.load(open('model.sav', 'rb'))
    scaled = pickle.load(open('scler.sav', 'rb'))

    prediction = model.predict(scaled.transform([
        [pclass, sex, age, sibsp, parch, fare, C, Q, S]
    ]))

    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'



