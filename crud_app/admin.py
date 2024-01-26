from django.contrib import admin
from crud_app.models import student
# Register your models here.
class stuadmin(admin.ModelAdmin):
    list = ['sno','sname','sclass','scity']
admin.site.register(student,stuadmin)