from django.conf.urls import include, url

from . import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .util import Trie, Node, OurTrie

app_name = "autosuggest"
router = DefaultRouter()


router.register('apis/v1', views.SuggestViewSet, base_name='sautosuggest')

urlpatterns = [

    url(r'', include(router.urls)),
    ]


OurTrie()

OurTrie.getInstance().our_trie_root.create_trie_from_file()
print('Created our try')
OurTrie.getInstance().our_map.insert()
print('Created our part datastructure')


