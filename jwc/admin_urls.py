from django.urls import path
from .views import (RegisterAPI, AdminLoginAPI, LogoutAPI, TeacherListAPI, StudentListAPI, AdminListAPI,
                    SemesterAPI, SemesterStatusAPI, CourseAPI, SemesterCourseAPI, CollegeAPI)

urlpatterns = [
    path('login/', AdminLoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('teacher/', TeacherListAPI.as_view()),
    path('student/', StudentListAPI.as_view()),
    path('admin/', AdminListAPI.as_view()),
    path('college/', CollegeAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('semester/', SemesterAPI.as_view()),
    path('semester/status/', SemesterStatusAPI.as_view()),
    path('course/', CourseAPI.as_view()),
    path('course/semester/<int:semester_id>', SemesterCourseAPI.as_view()),
]
