from django.shortcuts import render
from django.http import HttpResponse
from .models import Page

from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'page/index.html')

def detail(request, pk):
    photo = get_object_or_404(Page, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )

    return HttpResponse('\n'.join(messages))