#encoding=utf-8

from django.contrib import admin
from core import models

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.UserProfile,UserProfileAdmin)

class UserLinkAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.UserLink,UserLinkAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['name','alias','start_time','creator','create_time','tags']
    list_filter = ['start_time','create_time']

admin.site.register(models.Event,EventAdmin)

class EnrollAdmin(admin.ModelAdmin):
    list_display = ['event','user','comment','is_permited']
    list_filter = ['event','is_permited']

admin.site.register(models.Enroll,EnrollAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ['event','title','sub_title','author','tags']
    list_filter = ['event']

admin.site.register(models.Topic,TopicAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Vote,VoteAdmin)

class LiveMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.LiveMessage,LiveMessageAdmin)

class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Photo,PhotoAdmin)


