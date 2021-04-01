from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from evaluate.forms import TestCreateForm
from evaluate.models import Result

# Create your views here.
@login_required
def createTest(request):
    if request.method == 'POST':
        form = TestCreateForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            # res = Result(test = doc.id, result = '/results/test.csv')
            # res.save()
            return redirect('home-page')
    else:
        form = TestCreateForm()
    context = {
        'form' : form
    }
    return render(request, 'evaluate/createTest.html', context)
