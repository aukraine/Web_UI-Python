from django.db import models
import datetime

class RoleModel(models.Model):
    class Meta:
        db_table = 'roles'

    name = models.CharField(max_length=30, default=None)

class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    login = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=30, default=None)
    role = models.ForeignKey(RoleModel, on_delete = models.DO_NOTHING)
    date = models.DateField(default=None)

class UserDataModel(models.Model):
    class Meta:
        db_table = 'usersdata'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='userid')
    name = models.CharField(max_length=30, default=None)
    last = models.CharField(max_length=30, default=None)
    age = models.PositiveSmallIntegerField(default=None)
    email = models.CharField(max_length=30, default=None)

class GradeModel(models.Model):
    class Meta:
        db_table = 'grades'

    name = models.CharField(max_length=20, default=None)

class CourseModel(models.Model):
    class Meta:
        db_table = 'courses'

    name = models.CharField(max_length=20, default=None)

class StageModel(models.Model):
    class Meta:
        db_table = 'stages'

    department = models.CharField(max_length=20, default=None)
    name = models.CharField(max_length=50, default=None)

class QuestionModel(models.Model):
    class Meta:
        db_table = 'questions'

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default=None)
    tooltip = models.TextField(max_length=350, null=True, default=None)

class AnswerModel(models.Model):
    class Meta:
        db_table = 'answers'

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING)
    like = models.NullBooleanField(default=None, null=True)
    grade = models.ForeignKey(GradeModel, on_delete=models.DO_NOTHING, default=None, null=True)
    date = models.DateTimeField()

class CommentExpModel(models.Model):
    class Meta:
        db_table = 'comments'

    #user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    expert = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeModel, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=250, default=None)
    date = models.DateTimeField()
