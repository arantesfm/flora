from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^projeto/', views.project),
    url(r'^campus/', views.campus),
    url(r'^hrcb/', views.hrcb),

    url(r'^categorias/', views.species_categories),
    url(r'^especies/categoria/nome/', views.list_species_by_name),
    url(r'^especies/categoria/familia/', views.list_species_by_family),
    url(r'^especies/categoria/genero/', views.list_species_by_genre),
    url(r'^especies/categoria/especie/', views.list_species_by_specie),

    url(r'^$', RedirectView.as_view(url='/especies/categoria/nome/')),
]
