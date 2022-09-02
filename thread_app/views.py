from concurrent.futures import thread
from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Comment
from .forms import ThreadForm, CommentForm

def top(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Thread.objects.create(thread_name=data['thread_name'])
            return redirect('top')
    form = ThreadForm
    thread = Thread.objects.filter(del_flag=False)

    ctx = {
        'thread': thread,
        'form': form
    }

    return render(request, 'top.html', ctx)


def thread_delete(request, thread_id):
    try:
        thread = Thread.objects.get(id=thread_id)
        thread.del_flag = True
        thread.save()
        return redirect('top')
    except Thread.DoesNotExist:
        return redirect('top')
    
        
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(thread=thread, content=data['content'])
            return redirect('thread_detail', thread.id)

    form = CommentForm
    comment = Comment.objects.filter(thread=thread_id)
    ctx = {
        'thread': thread,
        'comment': comment,
        'form': form,
    }
    return render(request, 'thread_detail.html', ctx)
