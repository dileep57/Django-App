from django import forms
from .models import AlbumModel,SongModel,ImageModel
from django.urls import reverse


class Add_Album(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['first_name','last_name','location','banner']

    def get_absolute_url(self):
        return reverse('DileepImage:index')

class Add_Song(forms.ModelForm):
    class Meta:
        model = SongModel
        fields = ['song_name','song_file']

    def get_absolute_url(self):
        return reverse('DileepImage:index')

class Add_image(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']

    def get_absolute_url(self):
        return reverse('DileepImage:index')