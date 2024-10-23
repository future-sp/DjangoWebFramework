from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    text =  """
  <h1 style =    "font-family: Poppins, sans-serif;  
  color: #333; 
   font-size: 48px;
   text-align: center;
   border: 3px solid #3498db;  
   padding: 10px;   
   border-radius: 10px;
   background-color: #f0f4f8;  
   box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);"  >Welcome to Little Lemon! </h1>
  """
            
    return HttpResponse(text)