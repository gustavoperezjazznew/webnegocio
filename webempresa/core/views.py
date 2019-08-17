from django.shortcuts import render

# Create your views here.
#HttpResponse se utiliza cuando no vamos a trabajar con dinamismo de paginas 



def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")
    
def home(request):
    return render(request, "core/home.html")

