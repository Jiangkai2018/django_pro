from django.shortcuts import render
from django.http import HttpResponse
from Users.models import Users
# Create your views here.
def index(request):
    latest_users_list = Users.objects.all().order_by('-username')[:5]
    return render(request,"index.html",{'latest_users_list':latest_users_list})
def friends(request):
    #
    userInfoes = [
        {"name":"小明", "age":22, "sex":"男", "address":"河南省杞县"},
        {"name":"小明2", "age":22, "sex":"男", "address":"河南省杞县"},
        {"name":"小明3", "age":22, "sex":"男", "address":"河南省杞县"},
        {"name":"小明4", "age":22, "sex":"男", "address":"河南省杞县"},
    ]
    return render(request,"friends_record.html",{"userInfoes":userInfoes})

def home(request):
    htmlStr = '''
    <html><head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>kevin_home</title>
        <style type="text/css">
          body{
            font-family:黑体;
            font-size:30px;
          }</style>
        </head><body>welcome the kevin home</body></html>
     '''
    return HttpResponse(htmlStr)
