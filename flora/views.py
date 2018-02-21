from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from collections import OrderedDict

def pagina_inicial(request):
    return render(request, 'flora/home.html')


def project(request):
    return render(request, 'flora/project.html')


def campus(request):
    return render(request, 'flora/campus.html')


def hrcb(request):
    return render(request, 'flora/hrcb.html')


def fabiula(request):
    nome='Fabiula'
    return render(request, 'flora/fabiula.html',{'euzinha':nome})


def species_categories(request):
    return render(request, 'flora/species_categories.html')


def list_species_by_name(request):
    species = Post.objects.all().order_by('title')
    return render(request, 'flora/list_species.html', {'species': species, 'view': 'Nome'})


def list_species_by_family(request):
    all_species = Post.objects.all().order_by('familia')
    # order familie keys by OrderedDict
    species_by_family = OrderedDict()

    # get all species and put in a list ordering by family
    for some_specie in all_species:
        if not some_specie.familia in species_by_family.keys():
            species_by_family[some_specie.familia] = []
        species_by_family[some_specie.familia].append(some_specie)

    # order items inside of the list
    for ordered_specie in species_by_family.values():
        ordered_specie.sort(key=lambda x: x.genero)

    return render(request, 'flora/list_species_by_family.html', {'species_by_family': species_by_family, 'view': 'Família'})


def list_species_by_vernacular(request):
    species = Post.objects.all().order_by('vernacular')
    return render(request, 'flora/vernacular.html', {'species': species, 'view': 'Nome Popular'})


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


