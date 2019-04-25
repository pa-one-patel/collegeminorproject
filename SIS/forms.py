from django.contrib.auth.models import User
from django import forms
from .models import Faculty,LeaveRequest
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','is_staff']
        labels = {
            'is_staff' : ('Teaching Staff'),
        }

#UserCreationForm.Meta.fields +

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['photo','specialization']
        labels = {
            'specialization' : ('Department')
        }

class LeaveRequestForm(forms.ModelForm):
    start = forms.DateField(widget=forms.SelectDateWidget())
    end= forms.DateField(widget=forms.SelectDateWidget())
    reason=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = LeaveRequest
        fields = ['start','end','type','reason']

