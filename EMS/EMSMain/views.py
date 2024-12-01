from django.shortcuts import render
from EMSMain.templates import *

# Create your views here.
def index(httpreq):
    return render(httpreq,"index.html")
