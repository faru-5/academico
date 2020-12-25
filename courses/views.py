from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.views.generic import *
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import success
from .filters import CourseFilter




def homepage(request):
    subjects = Subject.objects.all()
    modules = Module.objects.all()
    courses = Course.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            success(request, username)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'courses/index.html',{'subjects':subjects, 'modules':modules,
                                                    'courses':courses, 'users':users, 'form':form})


def coursesPage(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()
    courseFilter = CourseFilter(request.GET, queryset=courses)

    courses = courseFilter.qs
    return render(request, 'courses/courses.html', {'subjects':subjects, 'courses':courses, 'courseFilter':courseFilter})


class CourseDetail(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    

class ModuleDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    template_name = 'courses/module/module.html'
    model = Module


class CourseCreate(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/edit/create_course.html'
    fields = ['subject', 'title', 'overview', 'coursevideo','coverImage','tags']
    success_url = '/courses/teacher/manage/'

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class ModuleCreate(LoginRequiredMixin, CreateView):
    model = Module
    template_name = 'courses/edit/create_module.html'
    fields = [ 'course', 'order','title', 'video', 'description']
    success_url = '/courses/module/edit/create/'
    

class CourseDelete(DeleteView):
    model = Course
    template_name = 'courses/edit/delete/delete_course.html'
    success_url = '/courses/teacher/manage/'


class CourseUpdate(UpdateView):
    model = Course
    template_name = 'courses/edit/update_course.html'
    fields = ['subject', 'title', 'overview', 'coursevideo','coverImage', 'cost','tags']
    success_url = '/courses/teacher/manage/'

    def form_valid(self, form):
        form.instance.instructor = self.request.user
        return super().form_valid(form)

def teacher_manage(request):
    courses = Course.objects.all()
    
    user_course_len = [course for course in courses if course.instructor.id == request.user.id ]
    course_length = Course.objects.all()
    
    context = {'courses':courses, 'course_length':len(course_length), 'user_course_len':len(user_course_len)}
    return render(request, 'courses/edit/manage/teacher_manage.html', context)


# def enrolled(request):
#     return render(request, 'courses/enrolled.html')

