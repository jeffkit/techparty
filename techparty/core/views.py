#encoding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from core.models import Event, Topic, Enroll, Vote, Photo


def index(request):
    """
    网站首页视图
    """
    return render_to_response('core/index.html',
                              context_instance=RequestContext(request))


def events(request):
    """
    活动列表面
    """
    events = Event.objects.all().order_by('-start_time')
    return render_to_response('core/events.html',
                              {'events': events},
                              context_instance=RequestContext(request))


def event(request, id):
    """
    活动详情面页视图
    """
    event = get_object_or_404(Event, pk=id)
    topics = Topic.objects.filter(event=event)
    enrolls = Enroll.objects.select_related('user')\
              .filter(event=event).order_by('-time')[:20]
    photos = Photo.objects.select_related('add_by')\
             .filter(event=event).order_by('-add_time')[:5]

    is_enroll = False
    if request.user.is_authenticated():
        for enroll in enrolls:
            # 如果用户已登录并已参加，则把标志高置为True
            if request.user == enroll.user:
                is_enroll = True

    return render_to_response('core/event.html', {'event': event,
                                                 'topics': topics,
                                                 'enrolls': enrolls,
                                                 'photos': photos,
                                                 'is_enroll': is_enroll},
                              context_instance=RequestContext(request))


@login_required
def enroll(request, eid):
    """
    用户参与指定的沙龙活动
    """
    enrolls = Enroll.objects.filter(user=request.user,
                                    event__pk=eid)

    if not enrolls:
        event = get_object_or_404(Event, pk=eid)
        comment = request.POST.get('comment', ' ')
        enroll = Enroll(user=request.user, event=event,
                        comment=comment)
        enroll.save()

    return HttpResponseRedirect('/event/%s/' % eid)


def topics(request):
    """返回所有的话题
    Arguments:
    - `request`:
    """
    tps = Topic.objects.filter().select_related(depth=1).order_by('-add_time')
    return render_to_response('core/topics.html', {'topics', tps},
                              context_instance=RequestContext(request))


def topic(request, id):
    """
    主题页面视图
    """
    tp = get_object_or_404(Topic, pk=id)
    return render_to_response('core/topic.html', {'topic': tp},
                              context_instance=RequestContext(request))


@login_required
def vote(request, tid):
    """
    用户给某个主题投票
    """
    tp = get_object_or_404(Topic, pk=tid)
    comment = request.POST.get('comment', ' ')
    try:
        Vote.objects.get(topic=tp, member=request.user)
    except Vote.DoesNotExist:
        vote = Vote(topic=tp, member=request.user, comment=comment)
        vote.save()

    return HttpResponseRedirect('/topic/%s/' % tid)


def member(request, id):
    """
    成员页面视图
    """
    member = get_object_or_404(User, pk=id)

    return render_to_response('core/member.html', {'member': member},
                              context_instance=RequestContext(request))
