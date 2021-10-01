from django.contrib import admin
from .models import *

# Register your models here.

class admin_resume(admin.ModelAdmin):
    list_display = ('name','contact','email','address','image','linkedln','github','insta','skill1','skill2','skill3','skill4','objective','work1','work2','edu1','edu2','ih1','ih2','ref')

admin.site.register(Resume, admin_resume)