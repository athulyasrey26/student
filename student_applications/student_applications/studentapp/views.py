from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.http import JsonResponse
from django.core import serializers
from .serializer import ApplicationSerializer


def user_logout(request):
   context = {}
   context['segment'] = 'index'
   context['departments'] = Department.objects.all()
   logout(request)
   return render(request, 'home.html', context)
    

def application_view(request):
   context = {}
   context['segment'] = 'buttonpage'
   context['departments'] = Department.objects.all()
   context['purposes'] = Purpose.objects.all()
   context['materials'] = Materials.objects.all()
   context['application'] = Application.objects.all()
   # if request.method == 'POST':
   #    form = ApplicationForm(request.POST)
   #    if form.is_valid():
   #       form.save()
   #       return render(request, 'success.html',context)
   if request.method == 'GET':
      form = ApplicationForm()
      context['form'] = form
   return render(request, 'application.html', context)


def applicationsubmit(request):
    # request should be ajax and method should be POST.
   if request.method == "POST":
      # get the form data
      form = ApplicationForm(request.POST)
      # save the data and after fetch the object in instance
      if form.is_valid():
         instance = form.save()
         # serialize in new friend object in json
         ser_instance =ApplicationSerializer(instance)
         # send to client side.
         return JsonResponse(ser_instance.data, status=200)
      else:
         # some form errors occured.
         return JsonResponse({"error": form.errors}, status=400)

   # some error occured
   return JsonResponse({"error": ""}, status=400)

def load_courses(request):
   print(request.GET)
   department_id = request.GET.get('department_id')
   courses = Course.objects.filter(department_id=department_id)
   course_list = list(courses.values('id', 'name'))
   return JsonResponse({'courses': course_list})


def home(request):
   context = {}
   context['segment'] = 'index'
   context['departments'] = Department.objects.all()
   return render(request, 'home.html', context)

def buttonpage(request):
   context = {}
   context['segment'] = 'buttonpage'
   context['departments'] = Department.objects.all()
   return render(request, 'buttonpage.html', context)
   

def login_view(request):
   context = {}
   context['segment'] = 'login'
   context['departments'] = Department.objects.all()

   if request.method == 'POST':
       form = AuthenticationForm(request, request.POST)
       if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
               login(request, user)
               return redirect('buttonpage')
         else:
            print("exception")
            
       else:
         print("error")
         form = AuthenticationForm()
         context['form'] = form
   return render(request, 'login.html', context)



class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

