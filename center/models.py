from django.db import models
from django.utils import timezone


# Create your models here.
class DemoApi(models.Model):
    fwl = models.IntegerField()
    yyyj = models.IntegerField()
    yymb = models.IntegerField()

    class Meta:
        verbose_name = '首页上三大统计'


class HealthyApi(models.Model):
    title = models.TextField(max_length=100)
    status = models.BooleanField(default=True)
    class Meta:
        verbose_name = '膳食营养目标'


class ProjectApi(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



