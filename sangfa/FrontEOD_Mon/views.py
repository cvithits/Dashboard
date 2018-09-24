from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Host,Tool

def index(request):
    user_id = request.user.id
    current_user = request.user
    return HttpResponse("Welcome: " + str(current_user))


def show_hostlist(request):
    host_list = list(Host.objects.filter(user_id=request.user.id).order_by('hostname'))
    respond = ""
    for host in host_list:
        respond = respond + str(host) + "<BR>"
    return HttpResponse(respond)

    """
    if request.user.is_authenticated():
        host_list = list(Host.objects.filter(user_id=request.user.id).order_by('hostname'))
        return HttpResponse(str(host_list))
        # return render(request, 'dsesite/home.html', {'site_list':site_list,'device_list':device_list})
    else:
        return HttpResponseRedirect('/')
    """


def show_tools(request, hostname):
    hostid = Host.objects.get(hostname=hostname)
    tool_list = list(Tool.objects.filter(host=hostid).order_by('tool_name'))
    respond = ""
    for toolobj in tool_list:
        respond = respond + str(toolobj.tool_name) + "<BR>"
    return HttpResponse(respond)


def show_toolsinfo(request, hostname):
    hostid = Host.objects.get(hostname=hostname)
    tool_list = list(Tool.objects.filter(host=hostid).order_by('tool_name'))
    respond = ""
    for toolobj in tool_list:
        respond = respond + str(toolobj.log_info) + "<BR>"
    return HttpResponse(respond)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


"""
def home(request):
    # user_id = request.user.id
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        site_list = list(Site.objects.filter(user_id=request.user.id).order_by('site_name'))
        device_list = Device.objects.none()
        for site in site_list:
            device_list = device_list | (Device.objects.filter(site_id=site.id))
        return render(request, 'dsesite/home.html', {'site_list':site_list,'device_list':device_list})

def site(request, site_id_in):
    user_id = request.user.id
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        site_ = Site.objects.get(pk=site_id_in)
        site_list = list(Site.objects.filter(user_id=request.user.id).order_by('site_name'))
        device_list = Device.objects.none()
        for site in site_list:
            device_list = device_list | (Device.objects.filter(site_id=site.id))
        return render(request, 'dsesite/site.html', {'site_':site_, 'site_list':site_list, 'device_list':device_list})

def device(request, site_id_in, device_id_in):
    user_id = request.user.id
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if checkPiId(request, device_id_in) is True:
            site = Site.objects.get(pk=site_id_in)
            device = Device.objects.get(pk=device_id_in)
            return render(request, 'dsesite/device.html', {'site':site, 'device':device})
        else:
            #site = Site.objects.get(pk=site_id_in)
            #device = Device.objects.get(pk=device_id_in)
            #return render(request, 'dsesite/device.html', {'site':site, 'device':device})
            return HttpResponseRedirect('/')
"""