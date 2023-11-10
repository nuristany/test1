from django.shortcuts import render, redirect, HttpResponse
from django.db.models.aggregates import Count,Max, Avg, Sum
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.core.mail import send_mail
from .forms import DonorForm
from . models import Donor

# Create your views here.



def home(request):

    user_count = Donor.objects.aggregate(total = Count('id'))


    # Fetch the total contributions in USD
    total_contrib_usd = Donor.objects.filter(currency='USD').aggregate(total_contrib=Sum('monthly_contribution'))

    # Fetch the total contributions in AFG
    total_contrib_afg = Donor.objects.filter(currency='AFG').aggregate(total_contrib=Sum('monthly_contribution'))

    return render(request, 'dam/home.html', {'total_contrib_usd': total_contrib_usd, 'total_contrib_afg': total_contrib_afg, 'user_count':user_count})

# def register_donor(request):
#     if request.method == 'POST':
#         form = DonorForm(request.POST)
#         if form.is_valid:
#             donor = form.save()

#             template = get_template('dam/thank_you_email.html')

#             context = {
#                 'first_name':donor.first_name,
#                 'last_name': donor.last_name,
#                 'message':'Thank you for registering with our cause. Your support is greatly appreciated!'
#             }

#             print(context)

#             content = template.render(context)

#             # Send a thank you email
#             subject = 'Thank You for Registering'
#             from_email = 'donateforkunardam@gmail.com'
#             recipient_list = [donor.email]

#             email = EmailMessage(subject, content, from_email, recipient_list)
#             email.content_subtype = 'html'  # Set the content type to HTML
#             email.send()

#             return redirect('thank_you')
        
        
#     else:
#         form = DonorForm()


#     return render(request, 'dam/register_donor.html', {'form':form})



# def thank_you(request):
#     return render(request, 'dam/thank_you.html')

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_donor(request):
    error_message = None  # Initialize error message

    if request.method == 'POST':
        form = DonorForm(request.POST)
        try:
            if form.is_valid():
                donor = form.save()

                # Prepare email content
                template = get_template('dam/thank_you_email.html')
                context = {
                    'first_name': donor.first_name,
                    'last_name': donor.last_name,
                    'message': 'Thank you for registering with our cause. Your support is greatly appreciated!'
                }
                content = template.render(context)

                # Send a thank you email
                subject = 'Thank You for Registering'
                from_email = 'donateforkunardam@gmail.com'
                recipient_list = [donor.email]

                email = EmailMessage(subject, content, from_email, recipient_list)
                email.content_subtype = 'html'  # Set the content type to HTML
                email.send()

                return redirect('thank_you')
        except ValueError as e:
            error_message = str(e)  # Capture and store the error message

    else:
        form = DonorForm()

    return render(request, 'dam/register_donor.html', {'form': form, 'error_message': error_message})

def thank_you(request):
    return render(request, 'dam/thank_you.html')

