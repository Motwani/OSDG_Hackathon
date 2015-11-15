from django.contrib import admin

from .models import Feedback
from .models import PQuestion,Prof
# Register your models here.


admin.site.register(Feedback)
admin.site.register(PQuestion)
admin.site.register(Prof)