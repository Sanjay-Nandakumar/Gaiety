from django.shortcuts import render  
from django.template import loader  
from django.http import HttpResponseBadRequest, HttpResponse
import pandas as pd
import numpy as np
import requests
from django.shortcuts import render  
import subprocess
import multiprocessing
import time   

#Create your views here  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  

def index(request):
    return render(request,"index2.html")  

def test(request):
        subprocess.call(["python", "myproject\happiness.py"])


def outputeda(request):
    print('EDA')
    

    p = multiprocessing.Process(target=test, name="test", args=(10,))
    p.start()

    # Wait 10 seconds for foo
    time.sleep(10)

    if p.is_alive():
        print("foo is running... let's kill it...")
        p.terminate()
        p.join()


    from django.http import HttpResponse
    return HttpResponse(status=204)




