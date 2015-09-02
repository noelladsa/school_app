# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=200)),
                ('school', models.OneToOneField(to='quiz.School')),
                ('students', models.ManyToManyField(related_name='SchoolProfile1', to='quiz.SchoolProfile')),
                ('teacher', models.OneToOneField(related_name='SchoolProfile', to='quiz.SchoolProfile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together=set([('school', 'class_name')]),
        ),
    ]
