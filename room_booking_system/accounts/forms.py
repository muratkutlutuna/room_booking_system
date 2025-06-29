from django import forms
from rooms.models import Room # Import your Room model
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    """
    Form for user registration.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class RoomBookingForm(forms.ModelForm):
    """
    Form for booking a room.
    """
    class Meta:
        model = Room
        fields = ('room_number', 'start_time', 'end_time')
