from django.shortcuts import render

def top(request):
    if request.method == 'GET':
        
    
        return render(request, 'top.html', { })
