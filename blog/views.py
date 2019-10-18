from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
posts=[{
        "author":"chandra",
        "title":"intro django",
        "content posted":"first",
        "date published":"24 august 2019"

    },
{                                            "author":"nath",                       "title":"wwlcome to django",                   "content posted":"second",
        "date published":"24 september 2019"

        }]


def home(request):
    context={
        "posts":Post.objects.all()
            }
    return render(request,"blog/home.html"
,context)

def about(request):
    return render(request,"blog/about.html")

# Create your views here.
