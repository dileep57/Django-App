from django.contrib import admin
from .models import AlbumModel,SongModel,ImageModel

admin.site.register(AlbumModel)
admin.site.register(ImageModel)
admin.site.register(SongModel)

