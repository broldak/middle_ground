from django.shortcuts import render
from django.http import HttpResponse
from mground.models import Artist
from django.template import RequestContext

from mground.forms import UserForm, ArtistForm


# Create your views here.

def index(request):
  artists = Artist.objects.all()
  print artists
  context_dict = {'artists': artists}

  return render(request, 'index.html', context_dict)

def register(request):
  registered = False

  context = RequestContext(request)

  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    artist_form = ArtistForm(data=request.POST)

    if user_form.is_valid() and artist_form.is_valid():
      user = user_form.save()

      user.set_password(user.password)
      user.save()

      artist = artist_form.save(commit=False)
      artist.user = user

      artist.save()

      registered = True

  else:
    user_form = UserForm()
    artist_form = ArtistForm()

  return render(request, 'register.html', 
                          {'user_form':user_form, 'artist_form': artist_form, 
                          'registered': registered})