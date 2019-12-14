from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from login.forms import LoginForm

def register(request):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.save()
            print(user.password)
            user.set_password(user.password)
            user.save()

            messages.success(request, "Successfully registered")
            return HttpResponseRedirect("/login")

    messages.error(request, "Error while registering")
    return HttpResponseRedirect("/login")

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out")
    return HttpResponseRedirect("/login")

def login_attempt(request):
    success = False

    if "demo" in request.POST:
        username = password = "demo"
    else:
        username = request.POST["username"]
        password = request.POST["password"]

    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            success = True

    return success

def detail(request):
	return HttpResponseRedirect("<h2>Hi"+str(User.username)+ "</h2>")

def login_index(request):
	html=''
	if request.method == "POST":
		result = login_attempt(request)
		if result:
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username, password=password)
			html='/login/' + str(user.id) + '/'
			messages.success(request, "Successfully logged in")
			return HttpResponseRedirect(html)
		else:
			messages.error(request, "Error logging in")
			return HttpResponseRedirect("")
	form_responses = messages.get_messages(request)
	response_message = None

	for response in form_responses:
		response_message = response
		break

	form_responses.used = True
	return render(request, "login/login.html", {"response_message": response_message})
