from django.shortcuts import render

from .models import AboutUs, Service, Barber, Price


# Create your views here.
def home(request):
    about = AboutUs.objects.all()

    services = Service.objects.all()
    barbers = Barber.objects.all()
    prices = Price.objects.all()

    return render(
        request,
        "main/home.html",
        {
            "about": about,
            "services": services,
            "barbers": barbers,
            "prices": prices,
        },
    )


# for booking


# def book(request):
#     if request.method == "Post":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save()
#             # sendemail confirmation
#             send_mail(
#                 "Booking Confirmation",
#                 f"Thank you very much for the booking, {booking.name}. We will see you on {booking.date} at {booking.time}."
#                 "cheche@gmail.com",
#                 [booking.email],
#                 fail_silently=False,
#             )
#             return redirect("booking_success")
#         else:
#             form = BookingForm()
#             return render(request, "main/book.html", {"form": form})


# def booking_success(request):
#     return render(request, "main/booking_success.html")
