from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import AlbumModel,SongModel,ImageModel
from django.http import HttpResponse,HttpResponseRedirect
from .form import Add_Album,Add_Song,Add_image
import requests
import os
import time
from bs4 import BeautifulSoup
import urllib.parse

imgexten = ['jpg','png','jpeg']


def allalbum(request):
        context= {"object_list":AlbumModel.objects.all()}
        return render(request,"DileepImage/albummodel_list.html",context)


def albumdetail(request,pk=None):
        object_list = AlbumModel.objects.get(id=pk)
        context = {'album':object_list}
        template_name = 'DileepImage/albummodel_detail.html'
        return render(request,template_name,context)




def addalbum(request):
        form = Add_Album(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            context = {}
            # return HttpResponseRedirect(instance.get_absolute_url())
            return render(request, 'DileepImage/albummodel_detail.html', {'album': instance})

        context = {'form':form}
        template_name = 'DileepImage/add_album.html'
        return render(request,template_name,context)



def addsong(request,album_id):
        form = Add_Song(request.POST or None, request.FILES or None)
        album = get_object_or_404(AlbumModel,pk=album_id)
        if form.is_valid():
            album_song = album.songmodel_set.all()
            for s in album_song:
                if s.song_name == form.cleaned_data.get("song_name"):
                    context = {
                        'album': album,
                        'form': form,
                        'error_message': 'You already added that song',
                    }
                    return render(request, 'DileepImage/add_song.html', context)

            instance = form.save(commit=False)
            instance.user = album
            song_file_name = instance.song_file
            exten = str(song_file_name).split('.')[-1]
            print(exten)
            if exten!='mp3':
                context = {'album': album,'error_message':'Not a MP3 Song','form':form,}
                return render(request,"DileepImage/add_song.html",context)

            instance.save()
            context = {'album':album}
            return render(request,"DileepImage/albummodel_detail.html",context)

        context = {'form':form,'album':album}
        return render(request,"DileepImage/add_song.html",context)


def delete_song(request, album_id, song_id):
        album = get_object_or_404(AlbumModel, pk=album_id)
        song = get_object_or_404(SongModel, pk=song_id)
        song.delete()
        return render(request, 'DileepImage/albummodel_detail.html', {'album': album})



def addimage(request,album_id):
        form = Add_image(request.POST or None, request.FILES or None)
        album = get_object_or_404(AlbumModel,pk=album_id)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = album
            song_file_name = instance.image
            exten = str(song_file_name).split('.')[-1]
            print(exten)
            if exten.lower() not in imgexten:
                context = {'album': album, 'error_message': 'We accept only jpg, png, jpeg','form': form }
                return render(request, "DileepImage/add_song.html", context)

            instance.save()
            context = {'album': album}
            return render(request, "DileepImage/view_image.html", context)
        context = {'form': form, 'album': album}
        return render(request, "DileepImage/add_image.html", context)


def show_image(request,album_id=None):
        context = {'album':AlbumModel.objects.get(pk=album_id)}
        return render(request,'DileepImage/view_image.html',context)


def delete_album(request,album_id=None):
        alb = get_object_or_404(AlbumModel,pk=album_id)
        alb.delete()
        context = {'object_list':AlbumModel.objects.all()}
        return render(request,'DileepImage/albummodel_list.html',context)


def update_album(request,album_id=None):
        instance = get_object_or_404(AlbumModel,pk=album_id)
        form = Add_Album(request.POST or None,request.FILES or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            context = {'object_list': AlbumModel.objects.all()}
            return render(request,'DileepImage/albummodel_list.html',context)
        context = {'form':form}
        return render(request,'DileepImage/add_album.html',context)

def youtube_search(request,album_id=None):
    album = get_object_or_404(AlbumModel,pk=album_id)
    if request.method=='GET':
        urrl = request.GET.get('query')
        if request.GET.get('query')==None:
            urrl = "taylor swift song"
        strr = '+'.join(str(urrl).split())
        url = 'https://www.youtube.com/results?search_query='+strr
        data = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
        data = BeautifulSoup(data.content,'html5lib')
        title = {}
        for tit in data.find_all('a',{'class':'yt-uix-tile-link'}):
            title[tit.get_text()] = tit.get('href').split('=')[-1]

        context = {"all_name_link":title,'album':album }
        return render(request,'DileepImage/youtube.html',context)
    title = {'all_name_link':'top 10 song'}
    context = {'album':album,"all_name__link":title}
    return render(request,'DileepImage/youtube.html',context)






	


	
