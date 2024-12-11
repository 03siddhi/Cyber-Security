from django.shortcuts import render,redirect
from django.core.mail import send_mail # for mail send we need to import it
from .models import Service

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User



# Create your views here.
# views.py
'''
from django.http import JsonResponse
from .models import User, Contact, Booking

def get_logged_in_users(request):
    users = User.objects.filter(is_logged_in=True)  # Example filter
    data = list(users.values('id', 'username', 'login_time'))
    return JsonResponse(data, safe=False)

def get_contacted_users(request):
    contacts = Contact.objects.all()
    data = list(contacts.values('id', 'username', 'contact_date', 'message'))
    return JsonResponse(data, safe=False)

def get_service_bookings(request):
    bookings = Booking.objects.all()
    data = list(bookings.values('id', 'username', 'service', 'booking_date', 'status'))
    return JsonResponse(data, safe=False)
'''









# myapp/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Order, Appointment, SurveyAnswer

def is_admin(user):
    return user.is_authenticated and user.is_staff


def status(request):
    return render(request, 'status.html', {})




def admin_page(request):
    orders = Order.objects.all()
    appointments = Appointment.objects.all()
    survey_answers = SurveyAnswer.objects.all()
    context = {
        'orders': orders,
        'appointments': appointments,
        'survey_answers': survey_answers,
    }
    return render(request, 'admin_page.html', context)








def viewcart(request):
    return render(request, 'viewcart.html', {})




def shop(request):
    return render(request, 'shop.html', {})


def login(request):
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view')  # Redirect to 'view' after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout(request):
   return render(request, 'home.html', {})
    






def bookservice(request):
    return render(request, 'bookservice.html', {})


def view(request):
    return render(request,'view.html',{})


    


def home(request):
    return render(request, 'home.html', {})

def survey(request):
    return render(request, 'survey.html', {})



def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        
        ### Send an Email End ###

        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})



def service(request):
    return render(request, 'service.html', {'service':service})


def pricing(request):
    return render(request, 'pricing.html', {})



def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

      




       ### Send an Email Start ###
       




        ### Send an Email End ###


        return render(request, 'appointment.html', {
            'your_name':your_name,
            'your_phone':your_phone,
            
            'your_address':your_address,
            'your_schedule':your_schedule,
            'your_date':your_date,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})


def booknow(request):
    return render(request, 'booknow.html')


#settingsession
from django.shortcuts import render

def set_session(request):
    request.session['key'] = 'value'
    return render(request, 'template.html')


from django.shortcuts import render

def get_session(request):
    value = request.session.get('key', 'default_value')
    return render(request, 'template.html', {'value': value})




# views.py
from django.shortcuts import render
from .models import Patient

def create_patient(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        
        patient = Patient.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            phone_number=phone_number,
            address=address
        )
        patient.save()
        return render(request, 'patient_success.html', {'patient': patient})

    return render(request, 'create_patient.html')



# views.py
'''
from django.http import JsonResponse
from website.models import Booking  # Ensure this import path is correct

def get_service_bookings(request):
    bookings = Booking.objects.all()
    data = list(bookings.values('id', 'username', 'service', 'booking_date', 'status'))
    return JsonResponse(data, safe=False)

'''








