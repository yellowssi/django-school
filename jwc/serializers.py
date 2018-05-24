from rest_framework import serializers
from .models import (College, Student, Teacher, Course, SemesterCourse, StudentSemesterCourse)


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'name', 'address', 'tel')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    name = serializers.ReadOnlyField(source='user.name')
    gender = serializers.ReadOnlyField(source='user.gender')
    birth = serializers.ReadOnlyField(source='user.birth')
    mobile = serializers.ReadOnlyField(source='user.mobile')
    college_name = serializers.ReadOnlyField(source='college.name')

    class Meta:
        model = Student
        fields = ('id', 'name', 'gender', 'birth', 'mobile', 'origin', 'college_name')


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    name = serializers.ReadOnlyField(source='user.name')
    gender = serializers.ReadOnlyField(source='user.gender')
    birth = serializers.ReadOnlyField(source='user.birth')
    mobile = serializers.ReadOnlyField(source='user.mobile')
    college_name = serializers.ReadOnlyField(source='college.name')

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'gender', 'birth', 'mobile', 'title', 'salary', 'college_name')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    college_name = serializers.HyperlinkedModelSerializer(source='college.name')

    class Meta:
        model = Course
        fields = ('id', 'name', 'college_name', 'credit', 'time')


class SemesterCourseSerializer(serializers.HyperlinkedModelSerializer):
    course_id = serializers.ReadOnlyField(source='course.id')
    course_name = serializers.ReadOnlyField(source='course.name')
    teacher_name = serializers.ReadOnlyField(source='teacher.user.name')

    class Meta:
        model = SemesterCourse
        fields = ('id', 'course_id', 'course_name', 'teacher_name', 'time', 'number')


class StudentCourseSerializer(serializers.HyperlinkedModelSerializer):
    course_id = serializers.ReadOnlyField(source='semester_course.course.id')
    course_name = serializers.ReadOnlyField(source='semester_course.course.name')
    course_credit = serializers.ReadOnlyField(source='semester_course.course.credit')
    teacher_name = serializers.ReadOnlyField(source='semester_course.teacher.name')
    time = serializers.ReadOnlyField(source='semester_course.time')

    class Meta:
        model = StudentSemesterCourse
        fields = ('id', 'course_id', 'course_name', 'course_credit', 'teacher_name', 'time')


class StudentGradeSerializer(serializers.HyperlinkedModelSerializer):
    course_id = serializers.ReadOnlyField(source='semester_course.course.id')
    course_name = serializers.ReadOnlyField(source='semester_course.course.name')
    course_credit = serializers.ReadOnlyField(source='semester_course.course.credit')
    teacher_name = serializers.ReadOnlyField(source='semester_course.teacher.name')

    class Meta:
        model = StudentSemesterCourse
        fields = ('id', 'course_id', 'course_name', 'course_credit', 'teacher_name', 'sgrade')


class TeacherCourseSerializer(serializers.HyperlinkedModelSerializer):
    course_id = serializers.ReadOnlyField(source='course.id')
    course_name = serializers.ReadOnlyField(source='course.name')
    course_credit = serializers.ReadOnlyField(source='course.credit')

    class Meta:
        model = SemesterCourse
        fields = ('id', 'course_id', 'course_name', 'course_credit', 'time', 'number')


class CourseStudentListSerializer(serializers.HyperlinkedModelSerializer):
    student_id = serializers.ReadOnlyField(source='student.user.id')
    student_name = serializers.ReadOnlyField(source='student.user.name')
    student_gender = serializers.ReadOnlyField(source='student.user.gender')
    student_college = serializers.ReadOnlyField(source='student.college.name')

    class Meta:
        model = StudentSemesterCourse
        fields = ('id', 'student_id', 'student_name', 'student_gender', 'student_college')


class TeacherGradesSerializer(serializers.HyperlinkedModelSerializer):
    student_id = serializers.ReadOnlyField(source='student.user.id')
    student_name = serializers.ReadOnlyField(source='student.user.name')
    student_gender = serializers.ReadOnlyField(source='student.user.gender')
    student_college = serializers.ReadOnlyField(source='student.college.name')

    class Meta:
        model = StudentSemesterCourse
        fields = ('id', 'student_id', 'student_name', 'student_gender', 'student_college', 'pgrade', 'egrade', 'sgrade')
