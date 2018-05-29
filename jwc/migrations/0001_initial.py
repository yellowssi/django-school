# Generated by Django 2.0.4 on 2018-05-29 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='名称')),
                ('address', models.CharField(max_length=255, verbose_name='地址')),
                ('tel', models.CharField(max_length=8, unique=True, verbose_name='联系电话')),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
                'db_table': 'college',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('credit', models.PositiveSmallIntegerField(verbose_name='学分')),
                ('time', models.PositiveSmallIntegerField(verbose_name='学时')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.College', verbose_name='学院')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='编号')),
                ('year', models.CharField(max_length=5, verbose_name='学年')),
                ('season', models.CharField(choices=[('autumn', '秋季学期'), ('winter', '冬季学期'), ('spring', '春季学期'), ('summer', '夏季学期')], max_length=6, verbose_name='学期')),
                ('start_date', models.DateField(unique_for_date=True, verbose_name='开始日期')),
                ('end_date', models.DateField(unique_for_date=True, verbose_name='结束日期')),
                ('status', models.BooleanField(default=False, verbose_name='是否开放选课')),
            ],
            options={
                'verbose_name': '学年学期',
                'verbose_name_plural': '学年学期',
                'db_table': 'semester',
            },
        ),
        migrations.CreateModel(
            name='SemesterCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='编号')),
                ('time', models.CharField(max_length=20, verbose_name='上课时间')),
                ('number', models.PositiveSmallIntegerField(verbose_name='容量')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.Course', verbose_name='课程')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.Semester', verbose_name='学期')),
            ],
            options={
                'verbose_name': '学期课程',
                'verbose_name_plural': '学期课程',
                'db_table': 'semester_course',
            },
        ),
        migrations.CreateModel(
            name='StudentSemesterCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='编号')),
                ('pgrade', models.CharField(max_length=3, null=True, verbose_name='平时成绩')),
                ('egrade', models.CharField(max_length=3, null=True, verbose_name='考试成绩')),
                ('sgrade', models.CharField(max_length=3, null=True, verbose_name='总评成绩')),
                ('semester_course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.SemesterCourse', verbose_name='学期课程')),
            ],
            options={
                'verbose_name': '学生各学期课程',
                'verbose_name_plural': '学生各学期课程',
                'db_table': 'student_semester_course',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='电话')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='是否教师')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否管理员')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jwc.User', verbose_name='用户')),
                ('origin', models.CharField(max_length=50, verbose_name='籍贯')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.College', verbose_name='学院')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jwc.User', verbose_name='用户')),
                ('title', models.CharField(choices=[('professor', '教授'), ('associate', '副教授'), ('lecturer', '讲师'), ('assistant', '助教')], max_length=10, verbose_name='职称')),
                ('salary', models.PositiveIntegerField(verbose_name='薪水')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.College', verbose_name='学院')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='studentsemestercourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='semestercourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jwc.Teacher', verbose_name='教师'),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'college')},
        ),
        migrations.AlterUniqueTogether(
            name='studentsemestercourse',
            unique_together={('student', 'semester_course')},
        ),
        migrations.AlterUniqueTogether(
            name='semestercourse',
            unique_together={('semester', 'course', 'teacher')},
        ),
    ]
