from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Course(models.Model):
    class Meta:
        ordering = ['pk']

    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        ordering = ['pk']

    number = models.IntegerField()  # course number according to the list
    name = models.CharField(max_length=100)  # title
    video = models.TextField(blank=True, null=False)  # href to video
    text = models.TextField()  # lesson's text
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE
    )  # from which course this lesson

    def __str__(self):
        return self.name


class Educator(models.Model):
    class Meta:
        ordering = ['pk']

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    teaches_courses = models.ManyToManyField(
        to=Course,
        related_name="teachers",
    )

    def __str__(self):
        return self.user.username


class Student(models.Model):
    class Meta:
        ordering = ['pk']

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
    studying_on_courses = models.ManyToManyField(
        to=Course,
        related_name="students",
    )

    def __str__(self):
        return self.user.username
