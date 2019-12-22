from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username',
                'email',
                'password1',
                'password2')
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label='Rumuz'
        self.fields['email'].label='Eposta Adresi'
