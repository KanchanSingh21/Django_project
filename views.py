from django.shortcuts import render ,redirect
from django.http import HttpResponse
from signup.models import signup_details
from login.models import login_details

def signup(request):
    return render(request,'signup.html')

def signup_info(request):
    if request.method=='POST':

        username=request.POST['username']
        mydate=request.POST['mydate']
        myemail=request.POST['myemail']
        myaddress=request.POST['myaddress']
        country=request.POST['country']
        statename=request.POST['statename']
        myGender=request.POST['myGender']
        role=request.POST['role']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        user=signup_details.objects.create(username=username,mydate=mydate,myemail=myemail,myaddress=myaddress,country=country,statename=statename,myGender=myGender,role=role,password=password,confirm_password=confirm_password)
        return HttpResponse("you have successfully inserted your details in database")
   
    

def login(request):
    if request.method=="POST':
        username=request.POST['email']
        password=request.POST['password']
        user=signup_details.object.get(email=username)
        if user.password==password:
            #return redirect("profile)
            pass #remove pass when you will implement above line.
        else:
            return HttpResponse('Entered credential are not in record')
    return render(request,'login.html')

def login_info(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=login_details.objects.create(username=username,password=password)
        return HttpResponse("you have successfully inserted your details in database")
