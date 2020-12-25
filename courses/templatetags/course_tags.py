from django import template
from ..models import Module,  Course
from django.contrib.auth.models import User

register = template.Library()

@register.inclusion_tag('courses/tags/tags.html')
def module_list(ide):
    modulelists = []
    for module in Module.objects.all():
        if module.course.id == ide:
            modulelists.append(module)
    return {'modulelists':list(modulelists)}

@register.simple_tag
def total_modules(ide):
    modulelists = []
    for module in Module.objects.all():
        if module.course.id == ide:
            modulelists.append(module)
    if len(modulelists) == 1:
        return f'{len(modulelists)} module'
    elif len(modulelists) > 1:
        return f'{len(modulelists)} modules'
    else:
        return f'no module'


@register.inclusion_tag('courses/tags/tags.html')
def course_list():
    courses = []
    for course in Course.objects.all():
        courses.append(course)
    return {'courses':courses}

@register.inclusion_tag('courses/tags/tags.html')
def tutor_list():
    tutors = []
    for user in User.objects.all():
        if user.is_superuser or user.is_teacher:
            tutors.append(user)
    return {'tutors':tutors}

@register.inclusion_tag('courses/tags/tags.html')
def tag_list():
    tags = []
    for tag in Course.tags.all():
        tags.append(tag)
    return {'tags':tags}

