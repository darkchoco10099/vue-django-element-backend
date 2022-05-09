from django.contrib import admin
from center.models import DemoApi, HealthyApi

# Register your models here.
admin.site.register([DemoApi, HealthyApi])

