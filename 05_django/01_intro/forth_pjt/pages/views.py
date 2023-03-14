from django.shortcuts import render

# Create your views here.
def index(request):
    # articles/templates/articles
    context = {'num':50}
    return render(request, 'pages/index.html', context)