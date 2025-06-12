from django.contrib import admin
from .models import Section, Module, Course, LearningPreference, Lesson
# Register your models here.


# class student(admin.ModelAdmin):
#     list_display = ('name', 'content')

admin.site.register(Section)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(LearningPreference)
admin.site.register(Lesson)

# class img_(admin.ModelAdmin):
#     list_display=('id', 'name', 'img')
# admin.site.register(Img,img_)