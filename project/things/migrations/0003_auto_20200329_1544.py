# Generated by Django 3.0.4 on 2020-03-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_answer_option_question_student_testinfo_testresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_table',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='User_table',
        ),
    ]