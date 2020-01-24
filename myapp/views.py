from django.shortcuts import render
from .models import Last_User
from .forms import IpForm
from random import randint

import json
import re
import requests



def main(request):
    user = Client(request)
    context = {
    "title": "whoami",
    "user_ip": user.ip,
    "system_about": ("OS: "+user.os, "Browser: "+user.browser),
    "location":("Contry: "+user.location.get("countryName"), "City: "+user.location.get("city"))
    }
    add_to_history(user.ip)
    return render(request, "myapp/index.html", context)

def add_to_history(user_ip, _id = 1):
    if user_ip not in Last_User.objects.all() and isinstance(user_ip, str):
        new_user = Last_User.objects.get(id = _id)
        new_user.ip =  user_ip
        new_user.save()
        
class Client():
    def __init__(self, request):
        self.META = request.META
        self.os = self._get_os()
        self.browser = self._get_browser()
        self.ip = self._get_ip()
        self.location = self._about_ip()

    def _get_os(self)->str:

        mac_names = "Mac" or "Macintosh" or "Mac_PowerPC"
        linux_names = "Linux" or "X11"
        ios_names = "iPhone" or "iPad" or "iPod"

        os_name = {
            "Android":'Android',
            "CrOS":"Chrome OS",
            "Windows NT 10.0":"Windows 10",
            "Windows NT 6.3":"Windows 8.1",
            "Windows NT 6.2":"Windows 8",
            "Windows NT 6.1":"Windows 7",
            linux_names:"Linux",
            mac_names:"Mac OS",
            ios_names:"IOS",
            }

        for i in os_name.keys():
            if i in self.META['HTTP_USER_AGENT']:
                return os_name[i]
        return "unknown"

    def _get_browser(self) -> str:
        browsers = ("Edge", "Opera", "OPR", "Chrome", "Trident","Firefox", "Safari")
        for i in browsers:
            if i in self.META['HTTP_USER_AGENT']:
                if i == "OPR": i = "Opera"
                if i == "Trident": i = "Intertet Explorer"
                return i
        return "unknown"

    def _get_ip(self) -> str:
        return self.META.get('HTTP_X_FORWARDED_FOR') or "%s.%s.%s.%s"%(randint(0,255),randint(100,255), randint(1,255),randint(0,255))

    def _about_ip(self) -> str:
        responce = json.loads(requests.get("http://api.db-ip.com/v2/free/%s"%self.ip).text)
        if  None != responce.get("countryName"):
            return responce
        return {"countryName": "Not found", "city" : "Not found"}
        #also can be use https://ipapi.com/ip_api.php?ip=
