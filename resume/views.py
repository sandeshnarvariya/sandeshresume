from django.shortcuts import render
from resume.models import contact
# Create your views here.
def index(request):
    return render(request, ('resume/index.html'))

def submit(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']
        con = contact (username=username,email=email,message=message)
        con.save()
    return render(request, ('resume/index.html'))

