from django.shortcuts import render, redirect
from django.http import HttpResponse

## Author: Sanjana Kothari and Naga Bathula
## This file contains the views for the Twitter API application.

# Create your views here.
def load_home_page(request):
    
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content', '')
    
    if content:
        print('Content:' + content);
        return redirect('home')
        
    return render(request, 'home.html')


