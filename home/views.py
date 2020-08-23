from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
	response = """<html>
					<body><p>Hello world DJ4E in HTML</p>
    					<p>This sample code is available at
    					<a href="https://github.com/csev/dj4e-samples">
    					https://github.com/csev/dj4e-samples</a></p>
    				</body>
    			   </html>"""
	return HttpResponse(response)

def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('dj4e_cookie', none)
    resp = HttpResponse('view count'+str(oldval))
    if oldval : 
        resp.set_cookie('dj4e_cookie', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('dj4e_cookie', 1) # No expired date = until browser close
    resp.set_cookie('dj4e_cookie', '42', max_age=1000) # seconds until expire
    return resp
	
def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count='+str(num_visits))
    