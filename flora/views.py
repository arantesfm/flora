from django.shortcuts import render

def post_list(request):
    return render(request, 'flora/post_list.html', {})