from django.contrib.auth import get_user_model  
User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email', 'first_name', 'last_name', 'gender','DOB','public_visibility','city','state' )