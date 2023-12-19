from django.shortcuts import render, redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import UserProfile

# from .forms import UserProfileForm
from .forms import UserProfileForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# class IndexView(generic.ListView):
#     model = Profile
#     template_name = "user_profile/profile_list.html"


# def index(request):
#     profile = ProfileForm()
#     customer = CustomerForm()
#     return render(request, 'user_profile/profile_form.html', { 'form': profile , 'customer': customer})

# def form_submit(request):
#     form = ProfileForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return render(request, 'user_profile/thankyou.html', {})
#     else:
#         return render(request, 'user_profile/profile_form.html', {'form': form})
    


# def customer_submit(request):
#     form = CustomerForm(request.POST)
#     if form.is_valid():
#         form.save()
#         # return HttpResponse("This is services list")
#         # return render(request, './home_services/service_list.html', {})
#         return HttpResponseRedirect(reverse('home_services:home'))
        
#     else:
#         return render(request, 'user_profile/profile_form.html', {'form': form})

# def user_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user.userprofile)

#         if form.is_valid():
#             form.save()
#             return redirect('user_profile')  # Redirect to the profile page
#     else:
#         form = UserProfileForm(instance=request.user.userprofile)

#     return render(request, 'user_profile/user_profile.html', {'form': form})
# def create_profile(request,id):
#     return render(request , "user_profile/create_profile.html")
def create_profile(request,id): 
    user = request.user
   
    return render(request , 'user_profile.html')
def user_profile(request):
    current_user = request.user
    # print(current_user.id)
    # print(user)
    
    if request.method == 'POST':   
        city = request.POST.get('city')    
        phone = request.POST.get('phone')   
        image = request.FILES.get('image') if 'image' in request.FILES else None
        
        user_profile = UserProfile(
            user=request.user,
            city=city,
            phone=phone,
            image=image
        )
        user_profile.save()
    user_profile = UserProfile.objects.filter(user=current_user)
   
    return render(request, 'user_profile/user_profile.html', {'user_profile': user_profile,'user':current_user})

def edit_profile(request):
    user = request.user
    # user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)

    if request.method == 'POST':
        # user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if  profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            return redirect('profile')  # Redirect to the profile page

    return render(request, "user_profile/edit_profile.html", { 'profile_form': profile_form})

def sign_up(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('user_profile:login')) 
        return render(request, "user_profile/signup_form.html")
    elif request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        print(user)
        return HttpResponseRedirect(reverse('user_profile:login')) 
    

def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home_services:home')) 
        return render(request, "user_profile/login_form.html")
    elif request.method == "POST":
        username = request.POST.get('username') # POST["username"]
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home_services:home')) 
        else:
            return render(request, "user_profile/login_form.html", {"login_message": "Username/password is incorrect"})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_profile:login'))