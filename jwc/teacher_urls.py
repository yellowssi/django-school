from django.urls import path
from .views import (TeacherLoginAPI, LogoutAPI, TeacherSemesterCourseAPI, TeacherNextSemesterCourseAPI,
                    TeacherCourseStudentListAPI, TeacherCourseGradesAPI)


urlpatterns = [
    path('login/', TeacherLoginAPI.as_view()),
    path('logout/', LogoutAPI.as_view()),
    path('course/', TeacherSemesterCourseAPI.as_view()),
    path('course/next/', TeacherNextSemesterCourseAPI.as_view()),
    path('course/students-list/<int:semester_course_id>/', TeacherCourseStudentListAPI.as_view()),
    path('course/grades/<int:semester_course_id>/', TeacherCourseGradesAPI.as_view()),
]
