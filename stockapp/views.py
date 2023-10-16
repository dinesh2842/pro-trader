from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.conf import settings
from .models import contact_us
from django.views import View
from django.http import JsonResponse
import json






def homepage(request):
     return render(request,'index.html')

def errorpage(request):
     return render(request,'404.html')

def explore(request):
     return render(request,'explore.html')

def activity(request):
     return render(request,'activity.html')

def leaderboard(request):
     return render(request,'leaderboard.html')

def payouts(request):
     return render(request,'payouts.html')

'''def contactus(request):
     return render(request,'contact.html')'''

def dashboard(request):
     return render(request,'dash.html')

def dashboardone(request):
     return render(request,'dashboard1.html')

def dashboardtwo(request):
     return render(request,'dashboard-2.html')

def success(request):
     return render(request,'success.html')

def token(request):
     return render(request,'token.html')

def calendar(request):
     return render(request,'calendar.html')

def billing(request):
     return render(request,'billing.html')

def accounts(request):
     return render(request,'accounts.html')



def register(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          email = request.POST.get('emailid')
          pass1 = request.POST.get('password1')
          pass2 = request.POST.get('password2')
          if pass1 != pass2:
               return HttpResponse("Password does not match")
          else:
               my_user = User.objects.create_user(username,email,pass1)
               my_user.save()
          return redirect('login')
     #print(username,email,pass1)
     return render(request,'register.html')

def loginpage(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          pass1 = request.POST.get('pass')
          #print(username,pass1)
          user = authenticate(request,username=username,password=pass1)
          if user is not None:
               login(request,user)
               
          else:
               return HttpResponse("Username or password doesn't match")
          return redirect('dashboard')
     return render(request,'signin.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        number = request.POST.get('number')
        message = request.POST.get('message')
        contact = contact_us(name=name,email=email,subject=subject,number=number,message=message)
        contact.save()
        #print(name,email,project,message)
        send_mail('Got a Message from Contact Form',
                  'Hi Team,\n\nWe have received a request from user.Please find the below information\nName: '+name+'\nEmail: '+email+'\n:Subject '+subject+'\n:Number '+number+'\nMessage: '+message+'\n\nBest regards,\nDevtech',
                  settings.EMAIL_HOST_USER,
                  ['team@devtechnician.com'],
                  fail_silently=False)
        send_mail('Thanks for Contacting Us',
                  'Hi '+name+',\nThank you for submitting a request. Our team will get in touch with you shortly.\n\nBest regards,\nPro Trader',
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently=False)
        return redirect('mainpage')
    return render(request, 'contact.html')

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})







