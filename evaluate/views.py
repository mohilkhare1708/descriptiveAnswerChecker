from django.contrib.auth import login
from evaluate.models import Result
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from evaluate.forms import TestCreateForm
import pandas as pd
import os
#from evaluate.models import Result

# Create your views here.
def findEXT(a):
    if a[-4] == '.':
        return a[-3:]
    if a[-5] == '.':
        return a[-4:]
    return -1

@login_required
def createTest(request):
    if request.method == 'POST':
        form = TestCreateForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            makEXT = findEXT(doc.model_answer_key.name)
            rsEXT = findEXT(doc.response_sheet.name)
            if makEXT not in ['xls', 'xlsx', 'csv'] or rsEXT not in ['xls', 'xlsx', 'csv']:
                print(makEXT, rsEXT, "hihi")
                return render(request, 'evaluate/createTest.html', {'form' : TestCreateForm()})
            doc.save()
            res = Result(test = doc, names = ['Mohil Khare', 'Prasuk Jain', 'Harsh Katkade'], emails = ['mohil.khare@somaiya.edu', 'prasuk.jain@somaiya.edu', 'harsh.katkade@somaiya.edu'], scores = [20, 19, 18])
            res.save()
            data = []
            for i in range(3):
                data.append([res.names[i], res.scores[i], res.emails[i]])
            # return redirect('home-page')
            # return redirect()
            # testSummary(request, {'result': data})
            return render(request, 'evaluate/testSummary.html', {'result' : data, 'len' : 3, 'name' : doc.test_name})

    else:
        form = TestCreateForm()
    context = {
        'form' : form
    }
    return render(request, 'evaluate/createTest.html', context)


@login_required
def testSummary(request, ctx):
    context = ctx
    return render(request, 'evaluate/testSummary.html', context)
