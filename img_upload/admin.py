from django.contrib import admin
from img_upload.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('file',)