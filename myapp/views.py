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
    x = History()
    x.add_ip(user.ip)
    return render(request, "myapp/index.html", context)


class History():
    def __init__(self):
        self.data_base = Last_User.objects
        self.ip_list = [i["ip"] for i in self.data_base.all().values()]

    def _add_new_ip(self, user_ip, _id = 1):
        new_user = self.data_base.get(id = _id)
        new_user.ip =  user_ip
        new_user.save()

    def _moove_cell(self, _start:int = None):
        start = _start or len(self.ip_list)

        if not isinstance(_start, type(None)):
            update = self.data_base.get(id = 1)
            update.ip = self.data_base.get(id = start).ip

        for i in range(start, 1, -1):
            val = self.data_base.get(id = i)
            val.ip = self.data_base.get(id = i-1).ip
            val.save()

        if not isinstance(_start, type(None)):
            update.save()

    def add_ip(self, user_ip):
        if user_ip not in self.ip_list and isinstance(user_ip, str):
            self._moove_cell()
            self._add_new_ip(user_ip)
        else:
            ip_id = self.ip_list.index(user_ip)+1
            self._moove_cell(ip_id)

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
        if False:#isinstance(self.ip, str):
            return json.loads(requests.get("http://api.db-ip.com/v2/free/%s"%self.ip).text)
        return {"countryName": "Not found", "city" : "Not found"}
        #also can be use https://ipapi.com/ip_api.php?ip=