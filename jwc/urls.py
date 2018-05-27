from django.urls import path
from .views import (StudentLoginAPI, LogoutAPI, StudentSemesterCourseAPI, StudentSemesterGradesAPI, StudentAllGradesAPI)

urlpatterns = [
    path('login/', StudentLoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('course/', StudentSemesterCourseAPI.as_view()),
    path('grades/semester/', StudentSemesterGradesAPI.as_view()),
    path('grades/all/', StudentAllGradesAPI.as_view()),
]
