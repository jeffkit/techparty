#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """
    一次沙龙的活动。
    """
    name = models.CharField(u'名称',max_length=50)
    alias = models.SlugField(u'标识',max_length=50)
    intro = models.TextField(u'内容')
    hash_tag = models.CharField(u'标签',max_length=20) # 用于微博、Twitter
    start_time = models.DateTimeField(u'开始时间')
    end_time = models.DateTimeField(u'结束时间')
    creator = models.ForeignKey(User,verbose_name=u'发起人')
    create_time = models.DateTimeField(u'发起时间',auto_now_add=True)
    #Tags 使用第三方Tag app

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'活动'
        verbose_name_plural = u'活动'

class Enroll(models.Model):
    """
    某一次活动的报名纪录
    """
    event = models.ForeignKey(Event,verbose_name=u'活动')
    user = models.ForeignKey(User,verbose_name=u'成员')
    time = models.DateTimeField(u'报名时间')
    comment = models.CharField(u'报名理由',max_length=140) #yeah,140 chars,a tweet's length
    is_permited = models.BooleanField(u'允许') # 被通过的报名才能收到邀请邮件

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = u'报名'
        verbose_name_plural = u'报名'


class Topic(models.Model):
    """
    某次活动的一个主题
    """
    event = models.ForeignKey(Event,verbose_name=u'活动')
    title = models.CharField(u'标题',max_length=50)
    sub_title = models.CharField(u'副标题',max_length=50,null=True,blank=True)
    description = models.TextField(u'简介')
    author = models.ForeignKey(User,verbose_name=u'讲师')
    add_time = models.DateTimeField(u'加入时间')
    #Tags 使用第三方Tag app

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'主题'
        verbose_name_plural = u'主题'

class Vote(models.Model):
    """
    某位成员为某个主题所投的票
    """
    topic = models.ForeignKey(Topic,verbose_name=u'主题')
    member = models.ForeignKey(User,verbose_name=u'成员')
    time = models.DateTimeField(u'投票时间')

    class Meta:
        verbose_name = u'投票'
        verbose_name_plural = u'投票'

class LiveMessage(models.Model):
    """
    某次活动中的一条直播消息,可能会被同时发送至微博或Twitter。
    """
    event = models.ForeignKey(Event,verbose_name=u'活动')
    text = models.CharField(u'消息',max_length=140)
    create_by = models.ForeignKey(User,verbose_name=u'作者',related_name="createdMessage")
    create_time = models.DateTimeField(u'发送时间',auto_now_add=True)
    update_by = models.ForeignKey(User,verbose_name=u'最后修改人',related_name="updatedMessage")
    update_time = models.DateTimeField(u'更新时间',auto_now=True)

    class Meta:
        verbose_name = u'直播消息'
        verbose_name_plural = u'直播消息'


