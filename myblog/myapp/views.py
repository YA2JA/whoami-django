# from django.contrib.gis.geoip import GeoIP
from django.shortcuts import render
from random import randint
import re

def index(request):
    user = Client(request)
    context = {
        "title": "hello",
        "word": user.ip,
        "info": (user.os, user.browser),
    }
    return render(request, "myapp/index.html", context)

class Client():
    def __init__(self, request):
        self.META = request.META
        self.os = self._get_os()
        self.browser = self._get_browser()
        self.ip = self._get_ip()

    def _get_os(self):
        os_name = {
            "Android":'Android',
            "Windows NT 10.0":"Windows 10",
            "Windows NT 6.3":"Windows 8.1",
            "Windows NT 6.2":"Windows 8",
            "Windows NT 6.1":"Windows 7",
            "Linux":"Linux",
            ("Mac" or "Hello"):"Mac OS"}#():"hi"

        for i in os_name.keys():
            if i in self.META['HTTP_USER_AGENT']:
                return os_name[i]
        return "unknown"

    def _get_browser(self):
        browsers = ("Edge", "Opera", "OPR", "Chrome", "Trident","Firefox", "Safari")
        for i in browsers:
            if i in self.META['HTTP_USER_AGENT']:
                if i == "OPR": i = "Opera"
                if i == "Trident": i = "Intertet Explorer"
                return i
        return "unknown"

    def _get_ip(self): 
        return self.META.get('HTTP_X_FORWARDED_FOR') or self.META.get('REMOTE_ADDR')

    def _other_info(self):
        pass
        #https://ipapi.com/ip_api.php?ip=