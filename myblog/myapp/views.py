# from django.contrib.gis.geoip import GeoIP
from django.shortcuts import render
from random import randint


def index(request):
    user = Client(request)
    base = "1234567890AZERTYUIOPQSDFGHJKLMWXCVBN?!:@azertyuiopqsdfghjklmwxcvbn."
    word = "Hello " + request.META.get("USERNAME")+"\n%s"%randint(0,10**6)
    title = get_client_ip(request)+"\n%s"%word
    content  = user.get_web_agent()
    context = {
        "title": title,
        "word": title,
        "content": content
    }
    return render(request, "myapp/index.html", context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_all_meta(request, text=""):
    for i in request.META.keys():
        if i == "HTTP_USER_AGEN":
            text += "%s:%s\n"%(i,request.META.get(i).split(",")[-1])
        else:
            text += "%s:%s\n"%(i,request.META.get(i))
    return text

def get_client_os(request):
    info = request.META['HTTP_USER_AGENT']
    return info[info.find("(")+1:info.find(")")]

class Client():
    def __init__(self, request):
        self.request = request

    def get_os(self):
        info = self.request.META['HTTP_USER_AGENT']
        return info[info.find("(")+1:info.find(")")]

    def get_web_agent(self):
        return self.request.META['HTTP_USER_AGENT']