from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.core.context_processors import csrf
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Achyuth")
cursor = db.cursor()

def welcome(request):
    return HttpResponse("<h1> Hello, World!</h1>")

def check_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    cursor.execute("select * from users where name='%s' and password='%s'" % (username,password))
    data = cursor.fetchone()
    if data:
        return HttpResponse("<h1> Hello, World!</h1>")
    else:
        return HttpResponse("<h1>Not Success</h1>")

def check_register(request):
    name = request.POST.get('Name', '')
    u_id = request.POST.get('Id', '')
    subject = request.POST.get('Subject', '')
    role = request.POST.get('Role', '')
    dept = request.POST.get('Dept', '')
    username = request.POST.get('Uname_Email', '')
    password = request.POST.get('Password', '')
    cpassqord = request.POST.get('Confirm', '')

    if password != cpassqord:
        return HttpResponse("<h1> Not Success </h1>")
    else:
        try:
            cursor.execute("insert into users(username,name,id,subject,role,dept,password) values('%s','%s','%s','%s','%s','%s','%s')" % (username,name,u_id,subject,role,dept,password))
            status = db.commit()
            return HttpResponse("<h1> User Created</h1>")
        except:
            return HttpResponse("<h1> User Not Created")
