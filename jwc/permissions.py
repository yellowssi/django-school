from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException


class NotStudent(APIException):
    default_detail = '10'


class StudentPermission(BasePermission):
    pass


class NotTeacher(APIException):
    default_detail = '11'


class TeacherPermission(BasePermission):
    pass


class NotAdmin(APIException):
    default_detail = '12'


class AdminPermission(BasePermission):
    pass
