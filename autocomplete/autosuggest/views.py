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
from .util import Trie, Node, read_file, OurRepo

# Create your views here.


class SuggestViewSet(ViewSet):

    permission_classes = [AllowAny, ]
    authentication_classes = []

    @action(methods=['get'], detail=False)
    def autocomplete(self, request):
        key = request.query_params.get('key', None)

        trie = OurRepo.getInstance().our_trie_root
        comp = trie.AllSuggestions(key)


        # if comp == -1 or comp ==0:
        #     print('Here 1')
        #     OurRepo.getInstance().our_map.suggestion(key)
        #     response = OurRepo.getInstance().our_map.words
        if comp == 1:
            print('Here 2')
            response = trie.words
        else:
            print('Here3')
            response = trie.search_with_typo(key, 1)
            print("\n\n\n")
            for result in response:
                print(result)

        response_status = status.HTTP_200_OK

        return Response(response, status=response_status)
