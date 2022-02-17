from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


dict_videos = [
    Video('motivacao', 'Vídeo Aperitivo: Motivação', 677826562),
    Video('instalacao-windows', 'Instalação Windows', 678404725),
]

videos_dict = {v.slug: v for v in dict_videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'dict_videos': dict_videos})


def videos(request, slug):
    video = videos_dict[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
