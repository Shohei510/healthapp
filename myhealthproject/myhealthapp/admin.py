from django.contrib import admin
from .models import Student, Class, Teacher, User, HealthRecord

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(User)
admin.site.register(HealthRecord)
