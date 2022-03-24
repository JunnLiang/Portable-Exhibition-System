from django.contrib import admin
from .models import ArchivePhoto, ArchiveVideo, ArchiveAudio
# Register your models here.

admin.site.register(ArchivePhoto)
admin.site.register(ArchiveVideo)
admin.site.register(ArchiveAudio)
