from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'DileepImage'
urlpatterns = [
    url(r'^$',views.allalbum,name='index'),
    url(r'^add_album/$',views.addalbum,name='add_album'),
    url(r'^album_detail/(?P<pk>[0-9]+)/$',views.albumdetail,name='album_detail'),
    url(r'^add_song/(?P<pk>[0-9]+)/$',views.addsong,name='add_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)$',views.delete_song,name='del_song'),
    url(r'^all_image/(?P<album_id>[0-9]+)/$',views.show_image,name='all_image'),
    url(r'^add_image/(?P<pk>[0-9]+)/$',views.addimage,name='add_image'),
    url(r'^delete_album/(?P<album_id>[0-9]+)/$',views.delete_album,name='del_album'),
    url(r'^update_album/(?P<album_id>[0-9]+)/$',views.update_album,name='edt_album'),
]