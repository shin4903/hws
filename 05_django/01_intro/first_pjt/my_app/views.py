from django.shortcuts import render

# Create your views here.
def hello(request):
    # articles/templates/articles
    return render(request, 'my_app/hello.html', )