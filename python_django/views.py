from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
import MySQLdb

class users:
    u_id = ''
    name = ''
    username = ''
    subject = ''
    dept = ''
    password = ''
    role = ''
    
    data = {
        'id': u_id,
        'name': name,
        'username': username,
        'subject': subject,
        'dept': dept,
        'password': password,
        'role': role
    }

    

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="Achyuth")
cursor = db.cursor()

def welcome(request):
    return HttpResponse("<h1> Hello, World!</h1>")

def check_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = users()
    
    cursor.execute("select * from users where username='%s' and password='%s'" % (username,password))
    data = cursor.fetchone()
    
    if data:
        user.username = data[0]
        user.name = data[1]
        user.u_id = data[2]
        user.subject = data[3]
        user.role = data[4]
        user.dept = data[5]
        user.password = data[6]
        
        data1 = {
            'username': user.username,
            'name': user.name,
            'id': user.u_id,
            'subject': user.subject,
            'role': user.role,
            'dept': user.dept,
        }
        
        return render(request, "dashboard.html", data1 )
        #return HttpResponse(data.username)
    else:
        return HttpResponse("<h1> Not Success </h1>")

def check_register(request):
    user = users()
    user.name = request.POST.get('Name', '')
    user.u_id = request.POST.get('Id', '')
    user.subject = request.POST.get('Subject', '')
    user.role = request.POST.get('Role', '')
    user.dept = request.POST.get('Dept', '')
    user.username = request.POST.get('Uname_Email', '')
    user.password = request.POST.get('Password', '')
    user.cpassqord = request.POST.get('Confirm', '')

    if user.password != user.cpassqord:
        return HttpResponse("<h1> Not Success </h1>")
    else:
        try:
            cursor.execute("insert into users(username,name,id,subject,role,dept,password) values('%s','%s','%s','%s','%s','%s','%s')" % (user.username, user.name, user.u_id, user.subject, user.role, user.dept, user.password))
            db.commit()
            return render(request, "dashboard.html", {"hello":"hii"})
        except:
            return HttpResponse("<h1> User Not Created")

def dashboard(request):
    user = users()
    return render(request, "dashboard.html", {"hello":"hii"})