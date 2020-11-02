import datetime
from .forms import RegisterForm
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect
from django.template import Template, Context, RequestContext

def get_user(request):
 '''
 获取用户信息列表
 :param request:
 :return:
 '''
 is_superuser = request.GET.get('is_superuser')
 print('get superuser:',is_superuser)
 if is_superuser is not None:
  users = User.objects.filter(is_superuser = is_superuser)
 else:
  users = User.objects.all()

 text = "用户信息：\n"
 userlist = []
 for user in users:
  userinfo = {
   'id':user.id,
   'username':user.username,
   'firstname':user.first_name,
   'lastname':user.last_name,
  }
  userlist.append(userinfo)
 text += str(userlist)
 return HttpResponse(text)

def get_userinfo(request, id):
 user = User.objects.get(id=id)
 name = user.username
 return HttpResponse("Hello " + name)

def current_datetime(request):
 now = datetime.datetime.now()
 html = "<html><body><h1>It is now %s.<h1></body></html>" % now
 return HttpResponse(html)

def add2num(request):
 a = request.GET['a']
 b = request.GET['b']
 result = float(a) + float(b)
 return HttpResponse("<html><body>{} + {} = {} </body></html>".format(a,b,result))

def login(request):
 # print(vars(request))
 # print(request.META.get('CSRF_COOKIE'))
 if request.method == 'GET':
  text = """
  <form action="/users/login" method="post">
  {% csrf_token %}
  <p>username: <input type="text" name="username" /></p>
  <p>password: <input type="password" name="password" /></p>
  <input type="submit" value="Submit" />
  </form>
  """
  t = Template(text)
  context = {
  "csrf_token":
  request.META.get('CSRF_COOKIE')
  }
  c = Context(context) # csrftoken
  return HttpResponse(t.render(c))
 else:
  username = request.POST['username']
  password = request.POST['password']
  user = User.objects.get(username=username)
  if user.check_password(password):
   text = '登录成功，欢迎 ' + user.last_name + user.first_name
   return HttpResponse(text)
  return redirect(reverse("users:current_time"))

def login_register(request):
 register_form = RegisterForm()
 print(register_form)
 context = {
  'register_form': register_form,
 }
 return render(request, 'myshop/login-register.html', context)

def register(request):
 if request.method == 'GET':
  return redirect(reverse("users:login_register"))
 user_form = RegisterForm(request.POST)
 if user_form.is_valid():
  new_user = user_form.save(commit=False)
  new_user.set_password(user_form.cleaned_data['password'])
  new_user.save()
  context = {
   'register_result': '注册成功',
   'register_form': RegisterForm()
  }
  return render(request, 'myshop/login-register.html', context)
 else:
  print(user_form)
  context = {
   'register_result': '注册失败',
   'register_form': user_form
  }
  return render(request, 'myshop/login-register.html', context)

def login_index(request):
 global context
 if request.method == 'GET':
  return redirect(reverse('users:login_register'))
 try:
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.get(email=email)
  if user.check_password(password):
   auth.login(request,user)
   text = '登录成功，欢迎 ' + user.last_name + user.first_name
   return HttpResponse(text)
 except Exception as e:
  login_result = str(e)
 else:
  login_result = '邮箱或密码不正确'
  context = {
  'login_result': login_result
  }
 return render(request, 'myshop/login-register.html', context=context)


