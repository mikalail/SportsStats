from django.shortcuts import render

def post_list(request):
    return render(request, 'sports/post_list.html', {})
