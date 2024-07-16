from django.shortcuts import render


def main_screen(request):
    return render(request,'blog/mainmenu.html')

# Create your views here.
