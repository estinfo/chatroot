import time
from django.shortcuts import render


def home(request):
    num = request.GET.get('num')
    ip = request.META.get("REMOTE_ADDR") + "\t" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\n"
    with open("ip.txt", mode="a") as f:
        f.write(ip)
    return render(request, "home.html", {"num": num})
