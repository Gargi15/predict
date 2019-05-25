from django.conf.urls import include, url

from . import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .util import Trie, Node, OurRepo

app_name = "autosuggest"
router = DefaultRouter()


router.register('apis/v1', views.SuggestViewSet, base_name='autosuggest')

urlpatterns = [

    url(r'', include(router.urls)),
    ]


OurRepo()
OurRepo.getInstance().our_trie_root.create_trie_from_file()
print('Created our try')
# OurRepo.getInstance().our_map.insert()
# print('Created our part datastructure')


