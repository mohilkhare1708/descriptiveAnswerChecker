from evaluate.models import Result, Test
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.full_name = form.cleaned_data.get('full_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title' : 'Register'})

@login_required
def dashboard(request):
    name = request.user
    dates, means= [], []
    tests = Test.objects.all().filter(user=request.user)
    for test in tests:
        dates.append(test.uploaded_at.date().strftime('%m/%d/%Y'))
        res = Result.objects.get(test=test)
        means.append(res.mean_percentage)
    context = {
        'name' : name.profile.full_name,
        'title' : 'Dashboard',
        'table' : tests,
        'dates' : dates,
        'means' : str(means)
    }
    return render(request, 'users/dashboard.html', context)
