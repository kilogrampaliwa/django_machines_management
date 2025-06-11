from django.shortcuts import render




def register(request):
    """
    Render the login page.
    """
    return render(request, 'accounts/register.html')