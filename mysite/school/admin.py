from django.contrib import admin

# Register your models here.

from school.models import Student, Car, Foto

admin.site.register(Student)
admin.site.register(Car)
admin.site.register(Foto)