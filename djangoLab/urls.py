from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from moviesapp.views import home, movie_list, actor_list, genre_list, category_list

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('movies/', movie_list, name='movie_list'),
    path('actors/', actor_list, name='actor_list'),
    path('genres/', genre_list, name='genre_list'),
    path('categories/', category_list, name='category_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
