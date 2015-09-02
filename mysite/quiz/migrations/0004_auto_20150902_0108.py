# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20150901_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveQuiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('due_by', models.DateField()),
                ('notes', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='IncompleteState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_remaining', models.DateTimeField()),
                ('choice', models.ManyToManyField(to='quiz.Choice')),
            ],
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('best_score', models.IntegerField()),
                ('no_of_attempts', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(to='quiz.School'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_by',
            field=models.ForeignKey(related_name='SchoolProfile2', to='quiz.SchoolProfile'),
        ),
        migrations.AlterField(
            model_name='schoolprofile',
            name='school',
            field=models.ForeignKey(to='quiz.School'),
        ),
        migrations.AddField(
            model_name='studentwork',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='studentwork',
            name='state',
            field=models.ForeignKey(to='quiz.IncompleteState', null=True),
        ),
        migrations.AddField(
            model_name='studentwork',
            name='student',
            field=models.ForeignKey(to='quiz.SchoolProfile'),
        ),
        migrations.AddField(
            model_name='activequiz',
            name='class_room',
            field=models.ForeignKey(to='quiz.ClassRoom'),
        ),
        migrations.AddField(
            model_name='activequiz',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quizzed_classes',
            field=models.ManyToManyField(to='quiz.ClassRoom', through='quiz.ActiveQuiz'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='student_work',
            field=models.ManyToManyField(related_name='SchoolProfile3', through='quiz.StudentWork', to='quiz.SchoolProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='studentwork',
            unique_together=set([('student', 'quiz')]),
        ),
        migrations.AlterUniqueTogether(
            name='activequiz',
            unique_together=set([('quiz', 'class_room')]),
        ),
    ]
