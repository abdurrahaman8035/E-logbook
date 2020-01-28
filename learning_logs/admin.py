from django.contrib import admin
from .models import Topic, Entry
# Register your models here.

#class TopicAdmin(.Model):
	#listview = ('text','date_added')

admin.site.register(Topic)
admin.site.register(Entry)
