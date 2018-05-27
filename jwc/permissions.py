from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from .models import User, Student, Teacher


class NotStudent(APIException):
    default_detail = '10'


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session['id']
        if Student.objects.filter(user__id=user_id).exists():
            return True
        raise NotStudent


class NotTeacher(APIException):
    default_detail = '11'


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session['id']
        if Teacher.objects.filter(user__id=user_id, user__is_teacher=True).exists():
            return True
        raise NotTeacher


class NotAdmin(APIException):
    default_detail = '12'


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session['id']
        if User.objects.filter(id=user_id, is_admin=True).exists():
            return True
        raise NotAdmin
