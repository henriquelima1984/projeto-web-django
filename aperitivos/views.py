from django.shortcuts import get_object_or_404, render
from aperitivos.models import Video


def indice(request):
    dict_videos = Video.objects.order_by('creation').all()
    return render(request, 'aperitivos/indice.html', context={'dict_videos': dict_videos})


def videos(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
