from django.template.defaulttags import url
from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('about_us/credit_union/', credit_union, name='credit_union'),
    path('about_us/structure/', structure, name='structure'),
    path('about_us/contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('information/', information, name='information'),
    path('documents/charter/', charter, name='charter'),
    path('documents/agreements/', agreements, name='agreements'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    # path('cats/<slug:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
