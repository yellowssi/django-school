# Generated by Django 2.0.4 on 2018-05-31 23:19

from django.db import migrations


def courses(apps, schema_editor):
    Course = apps.get_model("jwc", "Course")
    db_alias = schema_editor.connection.alias
    Course.objects.using(db_alias).bulk_create([
        Course(id='08305071', name='数字逻辑', college_id='1', credit='5', time='50'),
        Course(id='08305003', name='离散数学1', college_id='1', credit='4', time='50'),
        Course(id='08305004', name='离散数学2', college_id='1', credit='4', time='50'),
        Course(id='08305009', name='数据结构1', college_id='1', credit='4', time='60'),
        Course(id='08305010', name='数据结构2', college_id='1', credit='4', time='60'),
        Course(id='08305014', name='数据库原理1', college_id='1', credit='4', time='60'),
        Course(id='08305015', name='数据库原理2', college_id='1', credit='4', time='60')
    ])


class Migration(migrations.Migration):

    dependencies = [
        ('jwc', '0003_auto_20180530_1111'),
    ]

    operations = [
        migrations.RunPython(courses),
    ]
