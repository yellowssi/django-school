from django.urls import path
from .views import (StudentLoginAPI, LogoutAPI, StudentSemesterCourseAPI, StudentSemesterGradesAPI, StudentAllGradesAPI,
                    NextSemesterCourseSearchAPI, StudentCourseListAPI, CheckSemesterStatusAPI)

urlpatterns = [
    path('login/', StudentLoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('semester/', CheckSemesterStatusAPI.as_view()),
    path('course/next/', StudentSemesterCourseAPI.as_view()),
    path('course/', StudentCourseListAPI.as_view()),
    path('course/next/search/', NextSemesterCourseSearchAPI.as_view()),
    path('grades/semester/', StudentSemesterGradesAPI.as_view()),
    path('grades/all/', StudentAllGradesAPI.as_view()),
]
