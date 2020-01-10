from django.shortcuts import render
from random import choice

def index(request):
    base = "1234567890AZERTYUIOPQSDFGHJKLMWXCVBN?!:@azertyuiopqsdfghjklmwxcvbn."
    word = "".join(choice(base) for i in range(15))
    title = get_client_ip(request)
    content  =  about_os(request) #get_meta(request)
    context = {
        "title": title,
        "word": word,
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

def get_meta(request):
    for i in request.META.keys():
        if i == "HTTP_USER_AGEN":
            text += "%s:%s\n"%(i,request.META.get(i).split(",")[-1])
        else:
            text += "%s:%s\n"%(i,request.META.get(i))
    return text

def about_os(request):
    info = request.META['HTTP_USER_AGENT']
    return info[info.find("(")+1:info.find(")")]

def six(request):
    base = "1234567890"
    word = "".join(choice(base) for i in range(15))
    context = {
        "title": word[0:5],
        "word": word
    }
    return render(request, "myapp/index.html", context)