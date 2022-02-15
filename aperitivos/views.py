from django.shortcuts import render # noqa


def videos(request, slug):
    return render(request, 'aperitivos/video.html')
