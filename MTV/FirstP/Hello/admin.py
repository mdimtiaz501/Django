from django.contrib import admin
from Hello.models import Subject,AccessRecord,Webpage

# Register your models here.
admin.site.register(Subject)
admin.site.register(Webpage)
admin.site.register(AccessRecord)