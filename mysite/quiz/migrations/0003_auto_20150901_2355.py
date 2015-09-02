# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20150901_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to=b'')),
                ('is_right', models.BooleanField()),
                ('explanation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=800)),
                ('image', models.ImageField(upload_to=b'')),
                ('tags', models.CharField(max_length=200)),
                ('created_by', models.ForeignKey(to='quiz.SchoolProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200)),
                ('description', models.CharField(max_length=800)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('used', models.IntegerField()),
                ('related_course', models.CharField(max_length=200)),
                ('allowed_attempts', models.IntegerField(default=1)),
                ('timed', models.DateTimeField()),
                ('created_by', models.ForeignKey(to='quiz.SchoolProfile')),
            ],
        ),
        migrations.CreateModel(
            name='QuizDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_name', models.CharField(max_length=200)),
                ('question', models.ManyToManyField(to='quiz.Question')),
                ('quiz', models.OneToOneField(to='quiz.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='quiz.Question'),
        ),
    ]
