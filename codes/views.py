from django.shortcuts import render


def profile(request):
    author = request.user
    context = {
        "user": author
    }
    return render(request, 'profile.html', context)