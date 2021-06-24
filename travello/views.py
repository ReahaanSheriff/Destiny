from django.db.models import QuerySet
from django.shortcuts import render, redirect
from travello.models import *
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):

    dests=destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def destinations(request):
    return render(request,'destinations.html')

def bookForm(request,id):
    dest=destination.objects.get(id=id)
    return render(request,'book.html',{'dest':dest})



def book(request,did):
    if request.method=='POST':
        fromdate = request.POST['fromdate']
        todate = request.POST['todate']
        nos = request.POST['nos']
        user= User.objects.get(id=request.user.id)
        dest = destination.objects.get(id=did)
        Book.objects.create(did=dest,user_id=user,fromdate = fromdate, todate = todate, nos = nos)
        return redirect('myBookings')
    else:
        return render(request,'register.html')

def myBookings(request):
    if User.objects.filter(id=request.user.id).exists():
        booking = Book.objects.filter(user_id=request.user.id)
        mybook=[]
        myde=[]
        for data in booking:
            temp={}
            temp['id']=data.id
            temp['did']=data.did
            temp['fromdate']=data.fromdate
            temp['todate']=data.todate
            temp['nos']=data.nos
            temp['price']=data.price
            mybook.append(temp)
            myde.append(temp['did'])
        return render(request,'mybooking.html',{'mybook':mybook,'myde':myde})
    else:
        return redirect('/')
