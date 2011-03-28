#encoding=utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from core.models import Event,Topic,Enroll,Vote,Photo

def index(request):
    """
    网站首页视图
    """
    pass

def events(request):
    """
    活动列表面
    """
    events = Event.objects.all().order_by('-start_time')
    return render_to_response('core/events.html',{'events':events},context_instance=RequestContext(request))

def event(request,id):
    """
    活动详情面页视图
    """
    event = get_object_or_404(Event,pk=id)
    topics = Topic.objects.filter(event=event)
    enrolls = Enroll.objects.select_related(depth=1).filter(event=event).order_by('-time')[:20]
    photos = Photo.objects.select_related(depth=1).filter(event=event).order_by('-add_time')[:5]
    return render_to_response('core/event.html',{'event':event,'topics':topics,'enrolls':enrolls,'photos':photos},
            context_instance=RequestContext(request))

def enroll(request,eid):
    """
    用户参与指定的沙龙活动
    """
    pass

def topic(request,id):
    """
    主题页面视图
    """
    pass

def vote(request,tid):
    """
    用户给某个主题投票
    """
    pass

def member(request,id):
    """
    成员页面视图
    """
    pass

