from django.contrib import admin
from .models import *
# Register your models here.
admin.site.resgiter(Teacher)
admin.site.resgiter(Subject)
admin.site.resgiter(Student)
admin.site.resgiter(Admin)
admin.site.resgiter(Result)

