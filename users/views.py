from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from users.forms import LoginForm

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