from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method=='POST':
        link=request.POST.get('link')
        # print(link)
        quality=request.POST.get('qua')
        # print(quality)
        from pytube import YouTube
        yt=YouTube(link)
        stream=yt.streams.filter(res=quality, file_extension='mp4' ).first()
        stream.download('Videos/')  
    return render(request,'home.html')