# Generated by Django 2.0.4 on 2018-06-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwc', '0004_auto_20180601_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsemestercourse',
            name='egrade',
            field=models.CharField(max_length=5, null=True, verbose_name='考试成绩'),
        ),
        migrations.AlterField(
            model_name='studentsemestercourse',
            name='pgrade',
            field=models.CharField(max_length=5, null=True, verbose_name='平时成绩'),
        ),
        migrations.AlterField(
            model_name='studentsemestercourse',
            name='sgrade',
            field=models.CharField(max_length=5, null=True, verbose_name='总评成绩'),
        ),
    ]
