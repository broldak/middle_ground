from mground.models import Artist
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  def __init__(self, *args, **kwargs):
    super(UserForm, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'email', 'password']:
        self.fields[fieldname].help_text = None

  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class ArtistForm(forms.ModelForm):
  class Meta:
    model = Artist
    fields = ('website',)
