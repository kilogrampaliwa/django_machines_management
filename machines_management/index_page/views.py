from django.shortcuts import render


def index(request):
    """
    Render the index page.
    """
    return render(request, 'index_page/index.html')