from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from users.forms import LoginForm, UserRegistrationForm

# Create your views here.
def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data 
      user = authenticate(request, username = data['username'], password = data['password'])
      if user is not None:
        login(request, user)
        return HttpResponse('User authenticated and logged in')
      else: 
        return HttpResponse('Invalid user credentials')
  else:
    form = LoginForm()
  return render(request, 'users/login.html', {'form': form})


@login_required
def index(request):
  return render(request, 'users/index.html')


def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      new_user = form.save(commit=False)
      new_user.set_password(form.cleaned_data['password'])
      new_user.save()
      return render(request, 'users/register_done.html')
  else:
    form = UserRegistrationForm(request.POST)
    return render(request, 'users/register.html', {'form': form})
