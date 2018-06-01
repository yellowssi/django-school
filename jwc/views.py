import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .permissions import (StudentPermission, TeacherPermission, AdminPermission, UserPermission)
from .models import (College, User, Student, Teacher, Semester, Course, SemesterCourse, StudentSemesterCourse)
from .serializers import (CollegeSerializer, AdminSerializer, StudentSerializer, TeacherSerializer, SemesterSerializer,
                          CourseSerializer, SemesterCourseSerializer, StudentCourseSerializer, StudentGradeSerializer,
                          TeacherCourseSerializer, CourseStudentListSerializer, TeacherGradesSerializer)


class RegisterAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def post(self, request, format=None):
        user_id = request.data['id']
        name = request.data['name']
        gender = request.data['gender']
        birth = request.data['birth']
        mobile = request.data['mobile']
        password = request.data['password']
        identity = request.data['identity']
        if user_id and name and gender and birth and mobile and identity:
            if identity == 1:
                origin = request.data['origin']
                college_id = request.data['college_id']
                user = User.objects.create_student(user_id, name, gender, birth, mobile, origin, college_id, password)
                if user:
                    return Response({'detail': 0})
            elif identity == 2:
                title = request.data['title']
                salary = request.data['salary']
                college_id = request.data['college_id']
                user = User.objects.create_teacher(user_id, name, gender, birth, mobile, title, salary, college_id, password)
                if user:
                    return Response({'detail': 0})
            elif identity == 3:
                user = User.objects.create_admin(user_id, name, gender, birth, mobile, password)
                if user:
                    return Response({'detail': 0})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CollegeAPI(APIView):
    permission_classes = (UserPermission, )

    def get(self, request, format=None):
        colleges = College.objects.all()
        colleges_list = CollegeSerializer(colleges, many=True).data
        return Response({'colleges': colleges_list})


class StudentLoginAPI(APIView):
    def post(self, request, format=None):
        student_id = request.data['id']
        password = request.data['password']
        if student_id and password:
            try:
                student = User.objects.get(id=student_id)
                if student.check_password(password) and Student.objects.filter(user=student).exists():
                    request.session['id'] = student.id
                    return Response({'detail': 0})
                else:
                    return Response({'detail': '学号或密码错误'})
            except Exception as e:
                return Response({'detail': '学号或密码错误'})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TeacherLoginAPI(APIView):
    def post(self, request, format=None):
        teacher_id = request.data['id']
        password = request.data['password']
        if teacher_id and password:
            try:
                teacher = User.objects.get(id=teacher_id, is_teacher=True)
                if teacher.check_password(password) and Teacher.objects.filter(user=teacher).exists():
                    request.session['id'] = teacher.id
                    return Response({'detail': 0})
                else:
                    return Response({'detail': '学号或密码错误'})
            except Exception as e:
                return Response({'detail': '学号或密码错误'})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AdminLoginAPI(APIView):
    def post(self, request, format=None):
        admin_id = request.data['id']
        password = request.data['password']
        if admin_id and password:
            try:
                admin = User.objects.get(id=admin_id, is_admin=True)
                if admin.check_password(password):
                    request.session['id'] = admin.id
                    return Response({'detail': 0})
                else:
                    return Response({'detail': '学号或密码错误'})
            except Exception as e:
                return Response({'detail': '学号或密码错误'})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    def get(self, request, format=None):
        try:
            del request.session['id']
        except Exception:
            pass
        return Response({'detail': 0})


class StudentListAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, format=None):
        students = Student.objects.all()
        students_list = StudentSerializer(students, many=True).data
        return Response({'students': students_list})


class TeacherListAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, format=None):
        teachers = Teacher.objects.all()
        teachers_list = TeacherSerializer(teachers, many=True).data
        return Response({'teachers': teachers_list})


class AdminListAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, format=None):
        admins = User.objects.all().filter(is_admin=True)
        admins_list = AdminSerializer(admins, many=True).data
        return Response({'admins': admins_list})


class CourseAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, format=None):
        courses = Course.objects.all()
        courses_list = CourseSerializer(courses, many=True).data
        return Response({'courses': courses_list})

    def post(self, request, format=None):
        operation = request.data['operation']
        if operation == 1:
            course_id = request.data['id']
            course_name = request.data['name']
            course_college_id = request.data['college_id']
            course_credit = request.data['credit']
            course_time = request.data['time']
            if course_id and course_name and course_college_id and course_credit and course_time:
                course = Course.objects.create(id=course_id, name=course_name, college_id=course_college_id,
                                               credit=course_credit, time=course_time)
                if course:
                    return Response({'detail': 0})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif operation == 2:
            course_id = request.data['course_id']
            if Course.objects.filter(id=course_id).exists():
                Course.objects.filter(id=course_id).delete()
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SemesterAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, format=None):
        semesters = Semester.objects.all()
        semesters_list = SemesterSerializer(semesters, many=True).data
        return Response({'semesters': semesters_list})

    def post(self, request, format=None):
        year = request.data['year']
        autumn_start_date = request.data['autumn_start_date']
        autumn_end_date = request.data['autumn_end_date']
        winter_start_date = request.data['winter_start_date']
        winter_end_date = request.data['winter_end_date']
        spring_start_date = request.data['spring_start_date']
        spring_end_date = request.data['spring_end_date']
        summer_start_date = request.data['summer_start_date']
        summer_end_date = request.data['summer_end_date']
        if year and autumn_start_date and autumn_end_date\
                and winter_start_date and winter_end_date\
                and spring_start_date and spring_end_date\
                and summer_start_date and summer_end_date:
            autumn_semester = Semester.objects.create(year=year, season='autumn', start_date=autumn_start_date, end_date=autumn_end_date)
            winter_semester = Semester.objects.create(year=year, season='winter', start_date=winter_start_date, end_date=winter_end_date)
            spring_semester = Semester.objects.create(year=year, season='spring', start_date=spring_start_date, end_date=spring_end_date)
            summer_semester = Semester.objects.create(year=year, season='summer', start_date=summer_start_date, end_date=summer_end_date)
            if autumn_semester and winter_semester and spring_semester and summer_semester:
                return Response({'detail': 0})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SemesterStatusAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def post(self, request, format=None):
        semester_id = request.data['semester_id']
        try:
            semester = Semester.objects.get(id=semester_id)
            operation = request.data['operation']
            if operation == 1:
                if not semester.status:
                    Semester.objects.filter(status=True).update(status=False)
                    semester.status = True
                    semester.save()
                    return Response({'detail': 0})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif operation == 2:
                if semester.status:
                    semester.status = False
                    semester.save()
                    return Response({'detail': 0})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AdminGetSemesterCourseAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def get(self, request, semester_id, format=None):
        semester_courses = SemesterCourse.objects.all().filter(semester__id=semester_id)
        semester_courses_list = SemesterCourseSerializer(semester_courses, many=True).data
        return Response({'semester_courses': semester_courses_list})


class AdminAddSemesterCourseAPI(APIView):
    permission_classes = (UserPermission, AdminPermission,)

    def post(self, request, format=None):
        operation = request.data['operation']
        if operation == 1:
            semester_id = request.data['semester_id']
            course_id = request.data['course_id']
            teacher_id = request.data['teacher_id']
            time = request.data['time']
            number = request.data['number']
            if semester_id and course_id and teacher_id and time and number:
                semester_course = SemesterCourse.objects.create(
                    semester_id=semester_id,
                    course_id=course_id,
                    teacher_id=teacher_id,
                    time=time,
                    number=number)
                if semester_course:
                    return Response({'detail': 0})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif operation == 2:
            semester_course_id = request.data['semester_course_id']
            if SemesterCourse.objects.filter(id=semester_course_id).exists():
                SemesterCourse.objects.filter(id=semester_course_id).delete()
                return Response({'detail': 0})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CheckSemesterStatusAPI(APIView):
    permission_classes = (UserPermission, StudentPermission)

    def get(self, request, format=None):
        try:
            semester = Semester.objects.get(status=True)
            if semester.season == 'autumn':
                season = '秋季学期'
            elif semester.season == 'winter':
                season = '冬季学期'
            elif semester.season == 'spring':
                season = '春季学期'
            else:
                season = '冬季学期'
            semester_info = semester.year + season
            return Response({'semester_info': semester_info})
        except Exception as e:
            return Response()


class NextSemesterCourseSearchAPI(APIView):
    def post(self, request, format=None):
        semester = Semester.objects.get(status=True)
        if semester:
            course_id = request.data.get('course_id', False)
            course_name = request.data.get('course_name', False)
            if course_id and course_name:
                semester_courses = SemesterCourse.objects.all().filter(course__id__contains=course_id, course__name__contains=course_name, semester=semester)
            elif course_id and not course_name:
                semester_courses = SemesterCourse.objects.all().filter(course__id__contains=course_id, semester=semester)
            elif not course_id and course_name:
                semester_courses = SemesterCourse.objects.all().filter(course__name__contains=course_name, semester=semester)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            semester_courses_list = SemesterCourseSerializer(semester_courses, many=True).data
            for semester_course in semester_courses_list:
                number = StudentSemesterCourse.objects.filter(semester_course__id=semester_course['id']).count()
                semester_course['number'] = str(number) + '/' + str(semester_course['number'])
            return Response({'semester_courses': semester_courses_list})
        return Response({'detail': '选课系统未开通'})


class StudentCourseListAPI(APIView):
    permission_classes = (UserPermission, StudentPermission)

    def get(self, request, format=None):
        today = datetime.datetime.today()
        semester = Semester.objects.get(start_date__lte=today, end_date__gte=today)
        student_id = request.session['id']
        courses = StudentSemesterCourse.objects.all().filter(student__user__id=student_id, semester_course__semester=semester)
        courses_list = StudentCourseSerializer(courses, many=True).data
        return Response({'courses': courses_list})


class StudentSemesterCourseAPI(APIView):
    permission_classes = (UserPermission, StudentPermission,)

    def get(self, request, format=None):
        student_id = request.session['id']
        semester = Semester.objects.get(status=True)
        student_semester_courses = StudentSemesterCourse.objects.all().filter(student__user__id=student_id,
                                                                              semester_course__semester=semester)
        student_semester_courses_list = StudentCourseSerializer(student_semester_courses, many=True).data
        return Response({'courses': student_semester_courses_list})

    def post(self, request, format=None):
        operation = request.data['operation']
        if operation == 1:
            student_id = request.session['id']
            semester = Semester.objects.get(status=True)
            semester_course_id = request.data['semester_course_id']
            try:
                semester_course = SemesterCourse.objects.get(id=semester_course_id)
                if semester_course.semester == semester and \
                        not StudentSemesterCourse.objects.filter(student__user__id=student_id,
                                                                 semester_course__course=semester_course.course,
                                                                 semester_course__semester=semester).exists():
                    StudentSemesterCourse.objects.create(student_id=student_id, semester_course=semester_course)
                    return Response({'detail': '选课成功'})
                else:
                    return Response({'detail': '选课失败'})
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        elif operation == 2:
            student_id = request.session['id']
            semester = Semester.objects.get(status=True)
            student_semester_course_id = request.data['semester_course_id']
            try:
                student_semester_course = StudentSemesterCourse.objects.get(id=student_semester_course_id)
                if student_semester_course.student.user.id == student_id and student_semester_course.semester_course.semester == semester:
                    student_semester_course.delete()
                    return Response({'detail': '退课成功'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentSemesterGradesAPI(APIView):
    permission_classes = (UserPermission, StudentPermission,)

    def get(self, request, format=None):
        student_id = request.session['id']
        today = datetime.datetime.today()
        semester = Semester.objects.filter(start_date__lte=today, end_date__gte=today)
        semester_courses = StudentSemesterCourse.objects.all().filter(student__user__id=student_id,
                                                                      semester_course__semester__id=semester.id-1)
        grades_list = StudentGradeSerializer(semester_courses, many=True).data
        return Response({'grades': grades_list})


class StudentAllGradesAPI(APIView):
    permission_classes = (UserPermission, StudentPermission,)

    def get(self, request, format=None):
        student_id = request.session['id']
        today = datetime.datetime.today()
        semester = Semester.objects.filter(start_date__lte=today, end_date__gte=today)
        courses = StudentSemesterCourse.objects.all().filter(student__user__id=student_id,
                                                             semester_course__id__lt=semester.id)
        grades_list = StudentGradeSerializer(courses, many=True).data
        return Response({'grades': grades_list})


class TeacherSemesterCourseAPI(APIView):
    permission_classes = (UserPermission, TeacherPermission,)

    def get(self, request, format=None):
        teacher_id = request.session['id']
        today = datetime.datetime.today()
        semester = Semester.objects.get(start_date__lte=today, end_date__gte=today)
        courses = SemesterCourse.objects.all().filter(teacher__user__id=teacher_id, semester=semester)
        courses_list = TeacherCourseSerializer(courses, many=True).data
        return Response({'courses': courses_list})


class TeacherNextSemesterCourseAPI(APIView):
    permission_classes = (UserPermission, TeacherPermission,)

    def get(self, request, format=None):
        teacher_id = request.session['id']
        today = datetime.datetime.today()
        semester = Semester.objects.get(start_date__lte=today, end_date__gte=today)
        courses = SemesterCourse.objects.all().filter(teacher__user__id=teacher_id, semester__id=semester.id+1)
        courses_list = TeacherCourseSerializer(courses, many=True).data
        return Response({'courses': courses_list})


class TeacherCourseStudentListAPI(APIView):
    permission_classes = (UserPermission, TeacherPermission,)

    def get(self, request, semester_course_id, format=None):
        teacher_id = request.session['id']
        try:
            semester_course = SemesterCourse.objects.get(id=semester_course_id)
            today = datetime.datetime.today()
            semester = Semester.objects.filter(start_date__lte=today, end_date__gte=today)
            if semester_course.teacher.user.id == teacher_id and semester_course.semester == semester:
                students = StudentSemesterCourse.objects.all().filter(semester_course=semester_course)
                students_list = CourseStudentListSerializer(students, many=True).data
                return Response({'students': students_list})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TeacherCourseGradesAPI(APIView):
    permission_classes = (UserPermission, TeacherPermission,)

    def get(self, request, semester_course_id, format=None):
        teacher_id = request.session['id']
        try:
            semester_course = SemesterCourse.objects.get(id=semester_course_id)
            today = datetime.datetime.today()
            semester = Semester.objects.filter(start_date__lte=today, end_date__gte=today)
            if semester_course.teacher.user.id == teacher_id and semester_course.semester == semester:
                students = StudentSemesterCourse.objects.all().filter(semester_course=semester_course)
                students_list = TeacherGradesSerializer(students, many=True).data
                return Response({'students': students_list})
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        teacher_id = request.session['id']
        grades_list = request.data['grades']
        today = datetime.datetime.today()
        semester = Semester.objects.filter(start_date__lte=today, end_date__gte=today)
        for grades in grades_list:
            student_semester_course = StudentSemesterCourse.objects.get(id=grades.id)
            if student_semester_course.semester_course.teacher.user.id == teacher_id and student_semester_course.semester_course.semester == semester:
                student_semester_course.pgrade = grades.pgrade
                student_semester_course.egrade = grades.egrade
                student_semester_course.sgrade = grades.pgrade*0.5 + grades.egrade*0.5
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 0})
