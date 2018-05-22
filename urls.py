from django.conf.urls import url,include
from .import views




urlpatterns =[
        url(r'^pharjinny_registration_form/$', views.pharjinny_registration_form),
        url(r'pharjinny_login/$', views.pharjinny_login),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'search/',views.search),
        url(r'fetchlikes/',views.update_like),
        url(r'storelikes/',views.post_like),
        url(r'masspost/',views.posts),
        url(r'fetch/',views.fetch_post),
        url(r'wiki/',views.wikiapi),
        url(r'kuch/',views.code)



              ]
