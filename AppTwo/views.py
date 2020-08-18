from django.shortcuts import render
from AppTwo.models import User


# Create your views here.
def index(request):
    """Renders the AppTwp/index/html file."""
    return render(request, 'AppTwo/index.html')


def users(request):
    """
    Renders the users.html page from templates/AppTwo.

    Queries the database for the User list, and produces a dictionary
    of User data.

    Returns the request, the template file and the dictionary as context.
    """
    # Query for Users
    user_list = User.objects.order_by('email')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)