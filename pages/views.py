from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user) # Prints the user infomation in the console
    return render(request, "home.html", {"site_title": "Home"}) # return an html template

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1><p>This page does not use sharedlayoutbecause its missing Templage Tags.</p>")

def about_view(request, *args, **kwargs):
    my_context = {
        "site_title": "About",
        "my_text": "This is about us",
        "my_number": 1234567890,
        "my_list": ['a', 'b', 'c']
    }
    return render(request, "about.html", my_context) # return an html template
