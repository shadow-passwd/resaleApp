from django.shortcuts import render,redirect
from django.contrib import messages
from . import forms

# Create your views here.


def item_post(request):
    if request.method == 'POST':
        form = forms.ItemPostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            messages.success(request,'new post is added!')
            return redirect('home_page')

    else:
        form = forms.ItemPostForm()

    return render(request, 'item_post/post-ad.html', {'form': form})
