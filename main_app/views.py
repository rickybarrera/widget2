from django.shortcuts import render
from . models import Widget
from .forms import Form
# Create your views here.
def home (request):
    widget = Widget.objects.all()
    form = Form()
    desc = request.POST.get('description', None)
    quant = request.POST.get('quantity', None)
    new_widget = Widget.objects.create(description=desc, quantity=quant )
    return render (request,'home.html', {'widget': widget, 'form': form})