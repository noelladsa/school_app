from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    school_name = models.CharField(max_length=200, unique=True)
    school_address = models.CharField(max_length=400)


class SchoolProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    school = models.ForeignKey(School)


class ClassRoom(models.Model):
    school = models.ForeignKey(School)
    class_name = models.CharField(max_length=200)
    teacher = models.OneToOneField(SchoolProfile, related_name='SchoolProfile')
    students = models.ManyToManyField(SchoolProfile,
                                      related_name='SchoolProfile1')

    class Meta:
        unique_together = ('school', 'class_name')


class Quiz(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=800)
    created_on = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(SchoolProfile,
                                   related_name='SchoolProfile2')
    used = models.IntegerField()
    related_course = models.CharField(max_length=200)
    allowed_attempts = models.IntegerField(default=1)
    timed = models.DateTimeField()
    quizzed_classes = models.ManyToManyField(ClassRoom, through='ActiveQuiz')
    student_work = models.ManyToManyField(SchoolProfile, through='StudentWork',
                                          related_name='SchoolProfile3')


class Question(models.Model):
    description = models.CharField(max_length=800)
    image = models.ImageField()
    tags = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    description = models.CharField(max_length=800)
    image = models.ImageField()
    is_right = models.BooleanField()
    explanation = models.CharField(max_length=200)


class QuizDefinition(models.Model):
    quiz = models.OneToOneField(Quiz)
    section_name = models.CharField(max_length=200)
    question = models.ManyToManyField(Question)


class ActiveQuiz(models.Model):
    quiz = models.ForeignKey(Quiz)
    class_room = models.ForeignKey(ClassRoom)
    due_by = models.DateField()
    notes = models.CharField(max_length=800)

    class Meta:
        unique_together = ('quiz', 'class_room')


class IncompleteState(models.Model):
    time_remaining = models.DateTimeField()
    choice = models.ManyToManyField(Choice)


class StudentWork(models.Model):
    student = models.ForeignKey(SchoolProfile)
    quiz = models.ForeignKey(Quiz)
    state = models.ForeignKey(IncompleteState, null=True)
    best_score = models.IntegerField()
    no_of_attempts = models.IntegerField()

    class Meta:
        unique_together = ('student', 'quiz')
