from django.db import models
from datetime import date, datetime
from django.conf import settings
from dateutil.relativedelta import relativedelta

# Create your models here.
now = datetime.now()


class Study(models.Model):
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    max_people = models.IntegerField()
    participated = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="participate"
    )
    start_at = models.DateField(default=str(now)[:10])  # 경고창이 떠서 now의 형식을 바꿈
    end_at = models.DateField(default=(now + relativedelta(months=6)))
    member_number = models.IntegerField(default=1)

    @property
    def is_activate(self):
        if self.end_at is None:
            return True
        else:
            return date.today() < self.end_date


class StudyTodos(models.Model):
    study_pk = models.ForeignKey("Study", on_delete=models.CASCADE)
    management_pk = models.ForeignKey("StudyTodosManagement", on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.TextField()
    start = models.DateField()
    end = models.DateField()
    is_completed = models.BooleanField(default=False)


class StudyTodosManagement(models.Model):
    pass
