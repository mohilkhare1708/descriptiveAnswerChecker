from django.contrib.auth import login
from evaluate.models import Result
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from evaluate.forms import TestCreateForm

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
                return render(request, 'evaluate/createTest.html', {'form' : form, 'title' : 'Evaluate'})
            doc.save()
            res = Result.objects.get(test = doc)
            return redirect('testSummary', res.pk)
    else:
        form = TestCreateForm()
    context = {
        'form' : form,
        'title' : 'Evaluate'
    }
    return render(request, 'evaluate/createTest.html', context)


@login_required
def testSummary(request, pk):
    res = Result.objects.get(pk = pk)
    if res.test.user != request.user:
        return render(request, 'layouts/accessDenied.html')
    data = []
    for i in range(len(res.names)):
        data.append([res.names[i], res.scores[i], res.emails[i]])
    context = {
        'result' : data,
        'title' : 'Test Summary',
        'name' : res.test.test_name,
        'maxScore' : res.high_score,
        'noStudents' : res.total_students,
        'classAvg' : res.mean_percentage
    }
    return render(request, 'evaluate/testSummary.html', context)
