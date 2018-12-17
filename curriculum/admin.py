from django.contrib import admin

# Register your models here.
from curriculum.models import *

admin.site.register(Topic)
admin.site.register(Recommend)
admin.site.register(RecommendList)
admin.site.register(UserTopic)
