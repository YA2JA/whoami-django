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
    "location":("Contry: "+user.location.get("countryName"), "City: "+user.location.get("city")),
    "last_users":last_users_list(),
    }
    Add_ip(user.ip)
    return render(request, "myapp/index.html", context)

def last_users_list():
    return [i["ip"] for i in Last_User.objects.all().values()]

class Add_ip():
    def __init__(self, user_ip):
        self.data_base = Last_User.objects
        self.ip_list = last_users_list()

        tomoove = self.ip_list.index(user_ip)+1 if user_ip in self.ip_list else len(self.ip_list)
        self._moove_cell(tomoove)
        self._add_new_ip(user_ip)

    def _add_new_ip(self, user_ip, _id = 1):
        new_user = self.data_base.get(id = _id)
        new_user.ip =  user_ip
        new_user.save()

    def _moove_cell(self, start):
        update = self.data_base.get(id = 1)
        update.ip = self.data_base.get(id = start).ip

        for i in range(start, 1, -1):
            val = self.data_base.get(id = i)
            val.ip = self.data_base.get(id = i-1).ip
            val.save()

        update.save()

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
        return self.META.get('HTTP_X_FORWARDED_FOR') or "121.73.193.134"#"{0}.{1}.{2}.{3}".format(*(randint(0,255) for i in range(4)))

    def _about_ip(self) -> str:
        if isinstance(self.ip, str):
            return json.loads(requests.get("http://api.db-ip.com/v2/free/%s"%self.ip).text)
        return {"countryName": "Not found", "city" : "Not found"}
        #also can be use https://ipapi.com/ip_api.php?ip=