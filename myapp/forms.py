from .models import Last_User
from django.forms import ModelForm

class IpForm(ModelForm):
    class Meta():
        model = Last_User
        fields = ['ip']