from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
        <h1>Home Page</h1>
        <a href="/">Back</a> <br /> 
        <a href="posts/">Posts</a>
    """
    return HttpResponse(html)

def posts(request):
    html = """
        <h1>Posts</h1>
        <a href="/home">Back</a>
        
        <p>Hello Posts</p>
    """
    return HttpResponse(html)
