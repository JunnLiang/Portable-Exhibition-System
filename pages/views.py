from django.shortcuts import render
from django.views.generic import TemplateView
import os, re
import pathlib
from pathlib import Path

from pages.models import ArchiveAudio, ArchivePhoto, ArchiveVideo
# Create your views here.
def shorten_path(file_path, length):
	return Path(*Path(file_path).parts[-length:])

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'about.html'

class ContactUsView(TemplateView):
    template_name = 'contact.html'


def archives_home_view_media(request,*args,**kwargs):
    ArchivePhoto.objects.all().delete()
    ArchiveAudio.objects.all().delete()
    ArchiveVideo.objects.all().delete()

    path = 'pages/static/pages/Archive'  
    rx_media = re.compile(r'\.(mp4|mov|m4a|mp3|jpg|jpeg|JPG|JPEG|png|PNG)')
    r_media = []
    for path, dnames, fnames in os.walk(path):
        r_media.extend([os.path.join(path,x) for x in fnames if rx_media.search(x)])
    for filenames in r_media:
        if filenames.endswith('.m4a') or filenames.endswith('.mp3'):
            ArchiveAudio.objects.create(media=shorten_path(filenames,4), title=pathlib.PureWindowsPath(filenames).name)
        elif filenames.endswith('.mp4') or filenames.endswith('.mov'):
            ArchiveVideo.objects.create(media=shorten_path(filenames,4), title=pathlib.PureWindowsPath(filenames).name)
        else:
            ArchivePhoto.objects.create(media= shorten_path(filenames,4), title=pathlib.PureWindowsPath(filenames).name)

    archive_photo = ArchivePhoto.objects.all()
    archive_audio = ArchiveAudio.objects.all()
    archive_video = ArchiveVideo.objects.all()

    context = {
        'media_audios'     : archive_audio,
        'media_photos'     : archive_photo,
        'media_videos'     : archive_video,
            }

    return render(request,'home_archives.html', context)


class TeamPageView(TemplateView):
    template_name = 'team.html'

