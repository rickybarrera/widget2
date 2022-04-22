from django.shortcuts import render, redirect
from requests import request
from . models import Widget
from .forms import Form
# Create your views here.
def home (request):
    widget = Widget.objects.all()
    form = Form()
    if request.POST:
        desc = request.POST.get('description', None)
        quant = request.POST.get('quantity', None)
        new_widget = Widget.objects.create(description=desc, quantity=quant )
        return render (request,'home.html', {'widget': widget, 'form': form})
    else:
        return render (request,'home.html', {'widget': widget, 'form': form})

def delete_widget(request, pk):
    widget = Widget.objects.get(id=pk)
    print(widget)
    widget.delete()
    return redirect ('home')
    
