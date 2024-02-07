from django.forms import ModelForm
from .models import driver_signup_db

class Driver_Signup_form(ModelForm):
    class Meta:
        model = driver_signup_db
        fields = "__all__"