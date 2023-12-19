from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,get_object_or_404
from django.views import generic

from .models import * 

from .forms import *


class IndexView(generic.ListView):
    model = Service
    template_name = "home_services/service_list.html"
    
def cform(request):
    # profile = ProfileForm()
    customer = CustomerForm()
    return render(request, 'home_services/customer_form.html', {  'customer': customer})


def pform(request):
    profile = ProfileForm()
    # customer = CustomerForm()
    return render(request, 'home_services/provider_form.html', { 'form': profile})

# class DetailView(generic.DetailView):
#     model = Customer
#     template_name = "home_services/customer_form.html"

def form_submit(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'user_profile/thankyou.html', {})
    else:
        return render(request, 'user_profile/profile_form.html', {'form': form})

def customer_submit(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        # return HttpResponse("This is services list")
        # return render(request, './home_services/service_list.html', {})
        return render(request, 'home_services/received.html', {})
        
    else:
        return render(request, 'home-services/customer_form.html', {'form': form})
    

# def profile(request, id): 
#     user = get_object_or_404(User, pk= id) 
#     # total_likes = Questions.objects.filter(likes=user.id).aggregate(total_likes=Count('likes'))['total_likes']
#     user_profile = User_profile.objects.filter(user=user.id)
#     # question_asked = Questions.objects.filter(user=user.id).order_by('-date_created')[:5]
#     # total_likes_on_yourpost = Questions.objects.filter(user=user).aggregate(total_likes=Count('likes'))['total_likes']
#     # answers = Answer.objects.filter(name=user) 
#     return render(request , 'home_services/user_profile.html',{'profile':user_profile,})

# def profile_submit(request):
#     form = User_profile(request.POST)
#     if form.is_valid():
#         form.save()
#         # return HttpResponse("This is services list")
#         # return render(request, './home_services/service_list.html', {})
#         return render(request, 'home_services/received.html', {})
        
#     else:
#         return render(request, 'home-services/customer_form.html', {'form': form})
    

# def location_view(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'home_services/customer_form.html', {})
#     else:
#         form = LocationForm()

#     return render(request, 'home-services/location.html', {'form': form})

def customer_service_view(request):
    # Assuming you have a specific customer instance you want to display
    # You can modify this part based on your use case
    customer_instance = Customer.objects.first()

    # Retrieve Service information based on the ServiceTitle from Customer model
    service_instance = Service.objects.filter(Title=customer_instance.ServiceTitle).first()

    context = {
        'customer': customer_instance,
        'service': service_instance,
    }

    return render(request, 'home_services/received.html', context)


# def contact_form_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Process the form data and save it to the database
#             ContactSubmission.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 message=form.cleaned_data['message']
#             )
#             # Redirect the user to a thank you page or the home page
#             return HttpResponseRedirect('home_services/thank-you.html')  # Change '/thank-you/' to your actual thank you page
#     else:
#         form = ContactForm()

#     return render(request, 'home_services/service_list.html', {'form': form})


def contact_form_view(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to a thank you page or the home page
            return HttpResponseRedirect('home_services/thank-you.html')  # Change '/thank-you/' to your actual thank you page
    else:
        form = ContactSubmissionForm()

    return render(request, 'home_services/service_list.html', {'form': form})
