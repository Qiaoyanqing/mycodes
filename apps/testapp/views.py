

import content as content
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import datetime
def current_datetime(request):
 now = datetime.datetime.now()
 html = "<html><body><h1>It is now %s.<h1></body></html>" % now
 return HttpResponse(html)

def test_template(request):
 string = '杰普软件'
 course_list = ['Python','Web前端','JAVA','⼤数据','物联⽹']
 student_info = {'name':'briup','QQ':'123456','age':'20'}
 NumList = map(str, range(100))
 content = {}
 content['string'] = string
 content['course_list'] = course_list
 content['student_info'] = student_info
 content['NumList'] = NumList
 return render(request,'test_template.html',context=content)
