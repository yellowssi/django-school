from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class College(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=100, unique=True, verbose_name='名称')
    address = models.CharField(max_length=255, verbose_name='地址')
    tel = models.CharField(max_length=8, unique=True, verbose_name='联系电话')

    class Meta:
        db_table = 'college'
        verbose_name = '学院'
        verbose_name_plural = verbose_name


class UserManager(BaseUserManager):
    def create_student(self, id, name, gender, birth, mobile, origin, college_id, password=None):
        if User.objects.filter(id=id):
            raise ValueError('已注册')
        else:
            user = self.model(
                id=id,
                name=name,
                gender=gender,
                birth=birth,
                mobile=mobile
            )
            user.set_password(password)
            user.save()
            Student.objects.create(user=user, origin=origin, college__id=college_id)
            return user

    def create_teacher(self, id, name, gender, birth, mobile, title, salary, college_id, password=None):
        if User.objects.filter(id=id):
            raise ValueError('已注册')
        else:
            user = self.model(
                id=id,
                name=name,
                gender=gender,
                birth=birth,
                mobile=mobile,
                is_teacher=True
            )
            user.set_password(password)
            user.save()
            Teacher.objects.create(user=user, title=title, salary=salary, college__id=college_id)
            return user

    def create_admin(self, id, name, gender, birth, mobile, password=None):
        if User.objects.filter(id=id):
            raise ValueError('已注册')
        else:
            admin = self.model(
                id=id,
                name=name,
                gender=gender,
                birth=birth,
                mobile=mobile,
                is_admin=True
            )
            admin.set_password(password)
            admin.save()
            return admin


class User(AbstractBaseUser):
    id = models.CharField(max_length=8, primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=50, verbose_name='姓名')
    gender = models.CharField(max_length=6,
                              choices=(
                                  ('male', '男'),
                                  ('female', '女')
                              ), verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='电话')

    is_teacher = models.BooleanField(default=False, verbose_name='是否教师')
    is_admin = models.BooleanField(default=False, verbose_name='是否管理员')

    objects = UserManager()
    REQUIRED_FIELDS = (id, name, gender, birth, mobile)
    USERNAME_FIELD = 'id'

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def get_username(self):
        return getattr(self, 'id')

    def get_name(self):
        return getattr(self, 'name')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='用户')
    origin = models.CharField(max_length=50, verbose_name='籍贯')
    college = models.ForeignKey(College, on_delete=models.PROTECT, verbose_name='学院')

    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='用户')
    title = models.CharField(max_length=10,
                             choices=(
                                 ('professor', '教授'),
                                 ('Associate', '副教授'),
                                 ('lecturer', '讲师'),
                                 ('assistant', '助教')
                             ), verbose_name='职称')
    salary = models.PositiveIntegerField(verbose_name='薪水')
    college = models.ForeignKey(College, on_delete=models.PROTECT, verbose_name='学院')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name


class Semester(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='编号')
    year = models.CharField(max_length=5, verbose_name='学年')
    season = models.CharField(max_length=6,
                              choices=(
                                  ('autumn', '秋季学期'),
                                  ('winter', '冬季学期'),
                                  ('spring', '春季学期'),
                                  ('summer', '夏季学期')
                              ), verbose_name='学期')
    start_date = models.DateField(unique_for_date=True, verbose_name='开始日期')
    end_date = models.DateField(unique_for_date=True, verbose_name='结束日期')
    status = models.BooleanField(default=False, verbose_name='是否开放选课')

    class Meta:
        db_table = 'semester'
        verbose_name = '学年学期'
        verbose_name_plural = verbose_name


class Course(models.Model):
    id = models.CharField(max_length=8, primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=100, verbose_name='名称')
    college = models.ForeignKey(College, on_delete=models.PROTECT, verbose_name='学院')
    credit = models.PositiveSmallIntegerField(verbose_name='学分')
    time = models.PositiveSmallIntegerField(verbose_name='学时')

    class Meta:
        db_table = 'course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'college')


class SemesterCourse(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='编号')
    semester = models.ForeignKey(Semester, on_delete=models.PROTECT, verbose_name='学期')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='课程')
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, verbose_name='教师')
    time = models.CharField(max_length=20, verbose_name='上课时间')
    number = models.PositiveSmallIntegerField(verbose_name='容量')

    class Meta:
        db_table = 'semester_course'
        verbose_name = '学期课程'
        verbose_name_plural = verbose_name
        unique_together = ('semester', 'course', 'teacher')


class StudentSemesterCourse(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='编号')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, verbose_name='学生')
    semester_course = models.ForeignKey(SemesterCourse, on_delete=models.PROTECT, verbose_name='学期课程')
    pgrade = models.CharField(max_length=3, null=True, verbose_name='平时成绩')
    egrade = models.CharField(max_length=3, null=True, verbose_name='考试成绩')
    sgrade = models.CharField(max_length=3, null=True, verbose_name='总评成绩')

    class Meta:
        db_table = 'student_semester_course'
        verbose_name = '学生各学期课程'
        verbose_name_plural = verbose_name
        unique_together = ('student', 'semester_course')
