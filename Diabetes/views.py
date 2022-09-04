from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from .models import Glucose 
from .forms import GlucoseForm


# Create your views here.
def home(request):
	# return render(request, 'Diabetes/home.html',{})
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dijabetis') 
		else:
			messages.success(request, ("There Was An Error Logging In , Try Again"))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html',{})
	

def izmeri(request):
	if request.method == "POST":
		form_data = GlucoseForm(request.POST)
		if form_data.is_valid():
			izmerii = form_data.save(commit=False)
			izmerii.user = request.user
			izmerii.save()
			return redirect("izmeri_list")
	izmeri_list = Glucose.objects.filter(user=request.user).all()
	context = {"izmeri_list" : izmeri_list , "form" : GlucoseForm }
	return render(request, 'Diabetes/izmeri.html', context= context)

def edu(request):
	return render(request, 'Diabetes/education.html',{})


def ishrana(request):
	return render(request, 'Diabetes/ishrana.html',{})

def vezbi(request):
	return render(request, 'Diabetes/vezbi.html',{})

def dijabetis(request):
	return render(request, 'Diabetes/dijabetis.html',{})

def potsetnik(request):
	return render(request, 'Diabetes/potsetnik.html',{})