from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin

admin.site.register(BlogModel)
admin.site.register(CoursePartModel)
admin.site.register(ServiceModel)
admin.site.register(Profile)
admin.site.register(ContactModel)
admin.site.register(Recent)