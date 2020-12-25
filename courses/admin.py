from django.contrib import admin
from .models import Subject, Course, Module


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'date_created', 'instructor']
    search_fields = ['title', 'subject', 'date_created', 'instructor']
    prepopulated_fields = {'slug': ['title', 'subject', 'instructor']}


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title', 'course']
    prepopulated_fields = {'slug': ['title', 'course']}
