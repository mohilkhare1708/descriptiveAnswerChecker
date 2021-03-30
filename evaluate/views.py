from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from evaluate.forms import TestCreateForm

# Create your views here.
@login_required
def createTest(request):
    if request.method == 'POST':
        form = TestCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = TestCreateForm()
    context = {
        'form' : form
    }
    return render(request, 'evaluate/createTest.html', context)
