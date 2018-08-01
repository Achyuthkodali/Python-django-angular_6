from django.shortcuts import render, HttpResponse

# Create your views here.
def signup1(request):
    return render(request, 'signup/signup.html')
