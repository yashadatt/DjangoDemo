from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return ("<h1> welcome to Gallery<h2>")

def detail(request, video_id):
    return ("<h1> welcome to Gallery"+video_id+"</h1>")