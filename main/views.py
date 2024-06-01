from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import AboutUs,Story,Service,Barber,ServicePrice,Booking
from .forms import BookingForm

# Create your views here.
def home(request):
    about = AboutUs.objects.all()
    stories = Story.objects.all()
    services = Service.objects.all()
    barbers = Barber.objects.all()
    service_prices = ServicePrice.objects.all()
    return render(request,'main/home.html',{
        'about':about,
        'stories':stories,
        'services':services,
        'barbers':barbers,
        'service_prices':service_prices
    })

#for booking

def book(request):
    if request.method == 'Post':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            #sendemail confirmation
            send_mail(
                'Booking Confirmation',
                f'Thank you very much for the booking, {booking.name}. We will see you on {booking.date} at {booking.time}.'
                'cheche@gmail.com',
                [booking.email],
                fail_silently=False,
            )
            return redirect('booking_success')
        else:
            form = BookingForm()
            return render(request,'main/book.html',{'form':form})
        
def booking_success(request):
    return render(request,'main/booking_success.html')
 