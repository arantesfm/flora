from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def project(request):
    return render(request, 'flora/project.html')


def campus(request):
    return render(request, 'flora/campus.html')


def hrcb(request):
    return render(request, 'flora/hrcb.html')


def species_categories(request):
    return render(request, 'flora/species_categories.html')


def list_species_by_name(request):
    species = Post.objects.all().order_by('title')
    return render(request, 'flora/list_species.html', {'species': species, 'view': 'Nome'})


def list_species_by_family(request):
    species = Post.objects.all().order_by('familia')
    return render(request, 'flora/list_species.html', {'species': species, 'view': 'Família'})


def list_species_by_genre(request):
    species = Post.objects.all().order_by('genero')
    return render(request, 'flora/list_species.html', {'species': species, 'view': 'Gênero'})


def list_species_by_specie(request):
    species = Post.objects.all().order_by('especie')
    return render(request, 'flora/list_species.html', {'species': species, 'view': 'Espécie'})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'flora/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'flora/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'flora/post_edit.html', {'form': form})
