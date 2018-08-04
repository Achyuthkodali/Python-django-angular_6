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
    
    cursor.execute("select * from acchu where name='%s' and password='%s'" % (username,password))
    return HttpResponse("<h1> Hello, World!</h1>")