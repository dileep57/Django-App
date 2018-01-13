from django.db import models
from django.urls import reverse

def bannerloc(instance,filename):
    name = str(instance.first_name) + str(instance.last_name)
    return '{0}{1}'.format(name, '/Banner/' + filename)


class AlbumModel(models.Model):
    first_name   = models.CharField(max_length=200)
    last_name    = models.CharField(max_length=200)
    location     = models.CharField(max_length=200)
    banner       = models.ImageField(upload_to=bannerloc,null=True,blank=True,height_field="height_field",width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field  = models.IntegerField(default=0)
    timestamp    = models.DateTimeField(auto_now_add=True,auto_now=False)
    update       = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.first_name+"_"+str(self.id)

    def get_absolute_url(self):
        return reverse("DileepImage:index")


def location(instance,filename):
    lis = str(instance.user).split('_')
    obj = AlbumModel.objects.get(pk=str(lis[1]))
    name = str(obj.first_name) + str(obj.last_name)
    file_extension = str(filename).split('.')
    if file_extension[-1]=='mp3':
        return '{0}/{1}'.format(name,'Song/'+filename)
    else:
        return '{0}/{1}'.format(name,'Images/'+filename)


class ImageModel(models.Model):
    user = models.ForeignKey(AlbumModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=location)

    def __str__(self):
        self.name = str(self.image).split('.')[0]
        return self.name


class SongModel(models.Model):
    user = models.ForeignKey(AlbumModel,on_delete=models.CASCADE,null=True,blank=True)
    song_name = models.CharField(max_length=200,null=True,blank=True)
    song_file = models.FileField(upload_to=location)

    def __str__(self):
        return self.song_name

    def get_absolute_url(self):
        return "DileepImage:index"







