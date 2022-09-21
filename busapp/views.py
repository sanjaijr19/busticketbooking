from django.shortcuts import render,redirect,HttpResponse
from busapp.models import Driver
from busapp.form import DriverForm
from django.http import JsonResponse
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
from django.core.exceptions import ValidationError
# from .forms import ContactUsForm, RegistrationFormSeller, RegistrationForm, RegistrationFormSeller2, CartForm
from django.urls import reverse_lazy, reverse
# from .models import SellerAdditional, CustomUser, Contact, Product, ProductInCart, Cart
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,"busapp/index.html")
#
#
# def detail(request):
#     return render(request,"busapp/details.html")
#
#
# def empDetails(request):
#     name="sanjai"
#     emp_data=Driver.objects.all()
#     emp_dict = {"emp_list":emp_data}
#     return render(request, "busapp/index.html", context =emp_dict)
#
#
# def create_view(request):
#     form=DriverForm()
#     if request.method =="POST":
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home/")
#     return render(request,"busapp/details.html",{"form":form})


def empDetails(request):
    name="sanjai"
    emp_data=Driver.objects.all()
    emp_dict = {"emp_list":emp_data}
    return render(request, "busapp/index.html", context =emp_dict)
    #return HttpResponse("<h1 this is my application <h1>")

#u
def create_view(request):
    form=DriverForm()
    if request.method =="POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request,"busapp/create.html",{"form":form})

def delete_view(request,id):
    emp_data=Driver.objects.get(id=id)
    emp_data.delete()
    return redirect("/home")

def update_view(request,id):
    emp_data=Driver.objects.get(id=id)
    # emp_data={"emp_data":emp_data}
    # return render(request, "busapp/update.html", context=emp_data)
    if request.method == "POST":
        drivername=request.POST["drivername"]
        age=request.POST["age"]
        contact_no=request.POST["contact_no"]
        bus_no=request.POST["bus_no"]
        emp_data.drivername = drivername
        emp_data.age=age
        emp_data.contact_no=contact_no
        emp_data.bus_no=bus_no
        emp_data.save()
        return redirect("/home")
    return render(request, "busapp/update.html",{"emp_data":emp_data})
    # return render(request, "busapp/update.html", {"context":emp_data})
    # if request.method == "POST":
    #     drivername=request.POST["drivername"]
    #     age=request.POST["age"]
    #     contact_no=request.POST["contact_no"]
    #     bus_no=request.POST["bus_no"]
    #     emp_data.drivername=drivername
    #     emp_data.age=age
    #     emp_data.contact_no=contact_no
    #     emp_data.bus_no=bus_no
    #     emp_data.save()
    #     return redirect("/home")
    #
    # if request.method == "POST":
    #     form = DriverForm(request.POST, instance=emp_data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("/home")
    # return render(request, "dataApp2/update.html", {"Employee": emp_data})



    # emp_data = {"emp_data":emp_data}

    # return render(request, "busapp/update.html", context=emp_data)
def rough(request):
    emp_data = Driver.objects.all()
    emp_dict = {"emp_list": emp_data}
    return render(request,"busapp/rough.html",context =emp_dict)

# from django.contrib.auth.models import Group
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def addtopremiumGroup(request):
#     group=Driver.objects.get(name="Driver")
#     request.user.groups.add(group)
#     return HttpResponse("successfully added")

# from django.contrib.auth.decorators import group_required
# @group_required("Driver")
# def premiumproducts(request):
#     if request.user.groups.filter(name="premium").exist():
#         product=Driver.objects.all()
from django.contrib.auth.models import User,auth,UserManager
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import get_object_or_404, render
# def login(request,user):
#     User=User.objects.create_user(username=username,email=email,password=password)
#     User.last_name="lennon"
#     User.save()
#     user = authenticate(username='john', password='secret')
#     if user is not None:
#         # A backend authenticated the credentials
#         auth.login(request,user)
#         return redirect("/home")
#     else:
#         messages.info(request, "invalid user")
#         return render(request, "busapp/login.html")
#         # No backend authenticated the credentials

def homepage(request):
    return render(request,"busapp/homepage.html")

def signup(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=name,email=email,password=password,)
        if user:
            login(request,user)
            return render(request,'busapp/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'busapp/signup.html', context)
    else:
        return render(request, 'busapp/signup.html', context)

def signin(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name,password=password)
        if user:
            login(request,user)
            # username = request.session['username']
            context["user"] = name
            context["id"] = request.user.id
            return render(request, 'busapp/success.html',context)
            return HttpResponseRedirect('success')
            return redirect("home/")
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'busapp/signin.html',context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'busapp/signin.html',context)

def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'busapp/signin.html', context)



# #create group
# from django.contrib.auth.models import Group
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
#
# @login_required
# def busticket(request):
#     group=Group.objects.get(name="Driver")
#     request.user.groups.add(group)
#     return HttpResponse("successfullyadded")
#
#
#
# from busapp.models import User
# from .decorators import group_required
# @group_required('driver')
# def driver(request):
#     if request.user.groups.filter(name='Driver').exists():
#         product=Driver.objects.all()
#         return render(request,"busapp/index.html",{"product":product})
#     else:
#         return HttpResponse("restricted page")
# #
# from .mixins import CheckPremiumGroupMixin
# class PremiumProducts(CheckPremiumGroupMixin,ListView):
#     template_name="busapp/index.html"
#     model=Driver
#     context_object_name="product"
#     paginate_by=2
#     permission_required = "busapp.view_premiumproduct"
#
# from django.contrib.auth.models import Permission, User
# from django.contrib.contenttypes.models import ContentType
# from django.shortcuts import get_object_or_404
#
# from busapp.models import BlogPost

# def user_gains_perms(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     # any permission check will cache the current set of permissions
#     user.has_perm('busapp.change_blogpost')
#
#     content_type = ContentType.objects.get_for_model(BlogPost)
#     permission = Driver.objects.get(
#         codename='change_blogpost',
#         content_type=content_type,
#     )
#     user.user_permissions.add(permission)
#
#     # Checking the cached permission set
#     user.has_perm('busapp.change_blogpost')  # False
#
#     # Request new instance of User
#     # Be aware that user.refresh_from_db() won't clear the cache.
#     user = get_object_or_404(User, pk=user_id)
#
#     # Permission cache is repopulated from the database
#     user.has_perm('busapp.change_blogpost')  # True
#     return render(request,"busapp/index.html")

