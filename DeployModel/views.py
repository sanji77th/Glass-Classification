from django.http import HttpResponse
from django.shortcuts import render
import joblib
from numpy import dtype

def home(request):
    return render(request,"home.html")

def result(request):
    
    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])

    ans = cls.predict([lis])

    cat_lis = ['building windows float processed','building windows non float processed','vehicle windows float processed','vehicle windows non float processed','containers','tableware','headlamps']
    cat_ans = cat_lis[ans[0]-1]

    print(cat_ans)

    return render(request,'result.html',{'ans':cat_ans})
