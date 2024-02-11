from django.contrib.auth.forms import UserCreationForm
 
from .models import CustomUser
 
class UserRegistrationForm(UserCreationForm):
 
    class Meta:
        model = CustomUser
        fields = ("email","description", "is_author")

    def save(self, commit: bool = True) -> CustomUser:
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
 
        return CustomUser.objects.create_user(email, password, commit=commit)

