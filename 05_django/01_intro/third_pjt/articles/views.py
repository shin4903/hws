from django.shortcuts import render

# Create your views here.
# view함수는 한가지 특이한 점이 있다.
# 첫번째 인자는 반드시 request를 받도록 되어있다.

def index(request):
    # articles/templates/articles
    context = {'num':30}
    return render(request, 'articles/index.html', context)