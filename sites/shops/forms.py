from django  import forms
from .models import *

class addform(forms.ModelForm):
    class Meta:
        model = add
        fields = '__all__'