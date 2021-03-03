from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # creates a server side form object with the POST data
        if form.is_valid():  # validates the form
            user = form.save()  # stores the data
            login(request, user)
            
            return redirect('articles:list')  # redirects the user to the 'list' url in the articles namespace
            
    elif request.method == 'GET':
        form = UserCreationForm()  # creates a new form object to pass to the template
    
    return render(request, 'accounts/signup.html', {'form':form})  # if form.is_valid == FALSE, its POST data gets reloaded in the form

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # we label this as data because the AuthenticationForm doesn't primarily expect POST requests.
        if form.is_valid():
            user = form.get_user()  # built-in function to get the user data from the AuthenticationForm.
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    elif request.method == 'GET':
        form = AuthenticationForm()  #creates a new authentication form

    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':  # good practice to log users out with a POST request
        logout(request)

        return redirect('articles:list')