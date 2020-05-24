from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from .forms import PageForm

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.conf import settings

from django.contrib.auth.decorators import login_required


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

@login_required
def create(request):

    if request.method == "GET":
        form = PageForm()
    elif request.method == "POST":
        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'page/edit.html', ctx)