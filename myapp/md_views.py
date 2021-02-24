from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import User, Bus, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib import messages



def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # return HttpResponse("hi")
            if user.is_superuser :
                return redirect("admin_home")
            else:
                messages.error(request,'Invalid Login Details')
                return HttpResponseRedirect("admin_login")
        else:
            messages.error(request,'Invalid Login Details')
            return HttpResponseRedirect("admin_login")
        return("admin_login/")
    else:
        return render(request,"admin_template/admin_login.html")

def admin_home(request):
    bus=Bus.objects.all()
    context = {
        "buses":bus,
    }
    return render(request,"admin_template/admin_home.html",context)


def add_bus(request):
    if request.method == "POST":
        bus_name=request.POST.get("bus name")
        source=request.POST.get("source")
        destination=request.POST.get("destination")
        # nos=request.POST.get("nos")
        rem=request.POST.get("rem")
        price=request.POST.get("price")
        date=request.POST.get("date")
        time=request.POST.get("time")
        # print("busname",bus_name,"source",source,"destination",destination,"nos",nos,"rem",rem,"price",price,"date",date,"time",time)
        bus = Bus.objects.create(bus_name=bus_name,source=source,dest=destination,rem=rem,price=price,date=date,time=time)
        return redirect("/")
    else:
        return render(request,"admin_template/add_bus.html")


def admin_logout(request):
    logout(request)
    return redirect("admin_login")