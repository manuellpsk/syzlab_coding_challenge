from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from core.models import DrawingPage, User


def home(request):
    """
    Home page view - accessible to everyone.
    Shows a welcome message and login status.
    """
    return render(request, 'core/home.html')


@login_required
def profile(request, username):
    """
    User profile view - requires authentication.
    Displays any user's information based on the username parameter.
    """
    user = get_object_or_404(User, username=username)
    return render(request, 'core/profile.html', {
        'user': user,
        'is_own_profile': request.user.username == username
    })


@login_required
def profiles(request):
    """
    Profiles list view - requires authentication.
    Displays a list of all users.
    """
    users = User.objects.all().order_by('username')
    return render(request, 'core/profiles.html', {
        'users': users
    })


@login_required
def create_drawing(request, user_id: int):
    """
    View to create a new drawing - requires authentication.
    Displays a form to upload a new drawing.
    """
    if request.method == 'POST':
        DrawingPage.objects.create(user_id=user_id, title='New Drawing Page')

    return redirect('core:profile', username=request.user.username)
