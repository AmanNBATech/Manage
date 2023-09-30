from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.db.models import Q
from rest_framework import viewsets
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET","POST"])
def abc(request):
    if request.method =='GET':
      data=add.objects.all()
      d=aman(data,many=True)
      return Response (d.data,status = status.HTTP_200_OK)   
    else:
        d=aman(data=request.data)
        if d.is_valid():
            d.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='login')
def index(request):                                                                                 
    data = City.objects.all()
    print(data)
    return render(request,'index.html',{"data":data})

def sign(request):
   if request.method=='GET':
      return render(request,'signup.html')
   else:
      username=request.POST['username']  
      email=request.POST['email']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']
      if pass1==pass2:
         
         if User.objects.filter(username=username).exists():
            
            messages.warning(request,'username already exist')
            return redirect('sign')
         
         
        
         elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exist')
            return redirect('sign')
        
         else:
         
          User.objects.create_user(username=username,email=email,password=pass1)
          messages.success(request,'Account Has been created')
          return redirect('login')
      
      else:
         return redirect('sign')


def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    else:
        username=request.POST['username']
        password=request.POST['pass1']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'invalid userame or password')
            return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('login')


def enquiry(request):
    if request.method=='GET':                                       
        data = City.objects.all()
        return render(request,'index.html',{"data":data})
    else:
        name=request.POST['name']       
        date=request.POST['date']
        phone=request.POST['phone']
        city= City.objects.get(city= request.POST['city'])
        ab=hotel(name=name,ph=phone,date=date,city=city)
        ab.save()
        return render(request,'index.html')      

def contact(request):
   return render(request,'contact.html')       



def room(request):
    data=add.objects.all()  

    return render(request,'room.html',{'data':data})

def bk(request,id):
  
   data2 = add.objects.get(id=id)
   return render(request,'booking.html',{'data2':data2})

def ins(request):
   
   if request.method=="GET":
      form=addform()
      inse=add.objects.all()
      return render(request,'add.html',{'form':form,'inse':inse})
   
   else:
      form=addform(request.POST,request.FILES)
      if form.is_valid():
         form.save()
         return redirect('ins')
      

def book_room(request,id):
    add.objects.get(id=id)
    
    if request.method == "POST":
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        customer_name = request.POST['customer_name']
        room= request.POST['room']
        conflicting_bookings = bookingss.objects.filter(
            Q(room=room) &
            (
                (Q(check_in_date__lte=check_in_date) & Q(check_out_date__gte=check_in_date)) |
                (Q(check_in_date__lte=check_out_date) & Q(check_out_date__gte=check_out_date)) |
                (Q(check_in_date__gte=check_in_date) & Q(check_out_date__lte=check_out_date))
            )
        )
        
        if conflicting_bookings.exists():
            messages.warning(request,'Room is already booked for the selected dates')
            return render(request, 'booking.html')
        
        
        
        i = add.objects.get(id=id)
        bookingss.objects.create(   
            customer_name=customer_name,
            room=i,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )
      

    return render(request, 'booking.html')



def contact(request):
   return render(request,'contact.html')


def service(request):
   return render(request,'service.html')


def team(request):
   return render(request,'team.html')


def about(request):
   return render(request,'about.html')


def testimonial(request):
   return render(request,'testimonial.html')

def home(request):
   return render(request,'index.html')

def bookin(request):
   return render(request,'booking.html')

   





       
       
   


      

      

