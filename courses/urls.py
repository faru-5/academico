from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('courses/', views.coursesPage, name='courses'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('courses/module/<int:pk>/', views.ModuleDetail.as_view(), name='module'),
    path('courses/module/edit/create/', views.ModuleCreate.as_view(), name='create_module'),
    path('courses/edit/create/', views.CourseCreate.as_view(), name='create_course'),
    path('courses/<int:pk>/delete/', views.CourseDelete.as_view(), name='delete_course'),
    path('courses/teacher/manage/', views.teacher_manage, name='teacher_manage'),
    path('courses/<int:pk>/edit/', views.CourseUpdate.as_view(), name='edit_course'),

]