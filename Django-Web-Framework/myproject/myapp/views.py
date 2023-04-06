from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from .models import Menu

# Create your views here.

# def form_view(request):
#     form = BookingForm()
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {"form" : form}
#     return render(request, "booking.html", context)
#
# def home(request):
#     return HttpResponse("Welcome to Little Lemon !")

# def about(request):
#     return HttpResponse("About us")

# def menu(request):
#     return HttpResponse("Menu for Little Lemon")

# def book(request):
#     return HttpResponse("Make a booking")

# def drinks(request, drink_name):
#     drink = {
#         'mocha': 'type of coffee',
#         'tea': 'type of beverage',
#         'lemonade': 'type of refreshment'
#     }
#     choice_of_drink = drink[drink_name]
#     return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)

# def about(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
#     return render(request, "about.html", {'content': about_content})

# def menu(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
#     return render(request, "menu.html", {'content': about_content})


# def menu(request):
#     menu_items = Menu.objects.all()
#     items_dict = {'menu': menu_items}
#     return render(request, 'menu.html', items_dict)

# def home(request):
#     return render(request, 'index.html')
#
# def menu(request):
#     return render(request, 'menu.html')
#
# def about(request):
#     return render(request, 'about.html')
#
# def book(request):
#     return render(request, 'book.html')

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    return render(request, 'menu_item.html', { "menu_item": menu_item})
