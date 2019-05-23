from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import *
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from django.apps import apps
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .util import Trie, Node, read_file, OurTrie

# Create your views here.


class SuggestViewSet(ViewSet):

    permission_classes = [AllowAny ]
    authentication_classes = [ ]

    @action(methods=['get'], detail=False)
    def autocomplete(self, request, **kwargs):
        key = request.query_params.get('key', None)

        print('key is : ' + str(key)  + "\n\n\n\n\n")

        t0 = OurTrie.getInstance().our_trie_root

        # comp = t0.AllSuggestions(key)
        comp = -1
        if comp == -1 or comp ==0:
            print('Here 1')
            OurTrie.getInstance().our_map.suggestion(key)
            response = OurTrie.getInstance().our_map.words
        else:
            print('Here 2')
            response = t0.words

        response_status = status.HTTP_200_OK

        return Response(response, status=response_status)
