from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404

from posts.views import (
    index,
    search,
    blog,
    post,
    partners,
    # post_list,
    # post_detail,
    post_create,
    post_update,
    post_delete,
    # IndexView,
    # PostListView,
    # PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('waegahhadcaweg234dfsef/', post_create, name='post-create'),
    path('post/<id>/', post, name='post-detail'),
    path('post/<id>/wdaegahha_=ddcaweg23j4d$fsef/', post_update, name='post-update'),
    path('post/<id>/waegahhadcada2weg234dfsef/', post_delete, name='post-delete'),
    path('partners/', partners, name='partners'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),

    # path('error/', page_404, name='page_404'),
]

handler404 = 'posts.views.error_404_view'


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)