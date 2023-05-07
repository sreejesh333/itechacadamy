from django.shortcuts import render,redirect
from . models import user,student_details,cards
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
      if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        mark1 = request.POST.get('mark1')
        date_of_birth = request.POST.get('date_of_birth')
        course = request.POST.get('course')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')
        parent_name = request.POST.get('parent_name')
        parent_number = request.POST.get('parent_number')
        parent_occupation = request.POST.get('parent_occupation')
        
        if first_name=="" or phone=="" :
            messages.info(request,'All fields are required....!form not submitted')
            return redirect('contact')  
        elif len(str(phone))!=10 :
                messages.info(request,'phone number incorrect')
                return redirect('contact')
        elif user.objects.filter(phone=phone).exists():
            messages.info(request,'Phone number already registered ')
            return redirect('contact')
        else:
            usercontact = user(first_name=first_name,last_name=last_name,phone=phone,email=email,date_of_birth=date_of_birth,mark1=mark1,course=course,address=address,qualification=qualification,parent_name=parent_name,parent_occupation=parent_occupation,parent_number=parent_number)
            usercontact.save()
            
            messages.info(request,' Form Sucessfully registered ')
            subject = 'Thank you for Registering our course'
            message = 'We have received your registration and will be in touch soon.'
            
            send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Sender email address
            [email],  # Recipient email address
            fail_silently=False,
            )
            
      return render(request, 'contact.html')

# def startcontact(request):
#     if request.method == 'POST':
#         start_name  = request.POST.get('start_name')
#         start_phone = request.POST.get('start_phone')
#         userdetails = student_details(start_name=start_name,start_phone=start_phone,)
#         userdetails.save()
#         return redirect('index')
#     contact=student_details.objects.all()
#     return render(request, 'startcontact.html', {'contact': contact})
    

def index(request):
    card_element=cards.objects.all() 
    if request.method == 'POST':
        start_name  = request.POST.get('start_name')
        start_phone = request.POST.get('start_phone')
        userdetails = student_details(start_name=start_name,start_phone=start_phone,)
        userdetails.save()
    contact=student_details.objects.all()
    return render(request,'index.html',{'card_element':card_element,'contact': contact})
    

def abc(request):
    return render(request,'abc.html')

def advanced(request):
    return render(request,'advanced.html')

def diploma(request):
    return render(request,'diploma.html')
def online(request):
    return render(request,'online.html')

def view(request):
    students=user.objects.all()
    context={
        'students': students
    }
    print(context)
    return render(request,'view.html',context)


