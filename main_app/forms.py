from django.forms import ModelForm
from .models import Widget

class Form(ModelForm):
    class Meta:
        fields = ['description', 'quantity']
        model = Widget
    