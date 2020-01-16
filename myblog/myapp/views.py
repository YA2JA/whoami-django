# from django.contrib.gis.geoip import GeoIP
from django.shortcuts import render
from random import randint


def index(request):
    user = Client(request)
    context = {
        "title": "hello",
        "word": user.ip,
        "content": user.browser,
    }
    return render(request, "myapp/index.html", context)

class Client():
    def __init__(self, request):
        self.META = request.META
        self.os = self.__get_os__()
        self.browser = self.__get_brower__()
        self.ip = self.__get_ip__()

    def __get_os__(self):
        info = self.META['HTTP_USER_AGENT']
        return info[info.find("(")+1:info.find(")")]

    def __get_browser__(self):
        browsers = ("Edge", "Opera", "OPR", "Chrome", "Trident","Firefox", "Safari")
        for i in browsers:
            if i in self.META['HTTP_USER_AGENT']:
                if i == "OPR": i = "Opera"
                if i == "Trident": i = "Intertet Explorer"
                return i
        return "Your browser's unknown"

    def __get_ip__(self): 
        return self.META.get('HTTP_X_FORWARDED_FOR') or self.META.get('REMOTE_ADDR')

    def __other_info__(self):
        pass
