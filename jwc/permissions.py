from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from .models import User, Student, Teacher


class NotUser(APIException):
    status_code = 401
    default_detail = '10'


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session.get('id', False)
        if user_id:
            return True
        raise NotUser


class NotStudent(APIException):
    status_code = 403
    default_detail = '11'


class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session.get('id', False)
        if Student.objects.filter(user__id=user_id).exists():
            return True
        raise NotStudent


class NotTeacher(APIException):
    status_code = 403
    default_detail = '12'


class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session.get('id', False)
        if Teacher.objects.filter(user__id=user_id, user__is_teacher=True).exists():
            return True
        raise NotTeacher


class NotAdmin(APIException):
    status_code = 403
    default_detail = '13'


class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        user_id = request.session.get('id', False)
        if User.objects.filter(id=user_id, is_admin=True).exists():
            return True
        raise NotAdmin
