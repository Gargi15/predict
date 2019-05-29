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
from .util import Trie, Node, OurRepo
from boltons.setutils import IndexedSet

# Create your views here.

MAX_COUNT =25


class SuggestViewSet(ViewSet):

    permission_classes = [AllowAny, ]
    authentication_classes = []

    @action(methods=['get'], detail=False)
    def autocomplete(self, request):
        key = request.query_params.get('key', None)
        trie = OurRepo.getInstance().our_trie_root
        comp = trie.all_suggestions(key)
        if comp == 1:
            response = trie.words
            print(' 1: The type of response is: ' + str(type(response)))
            grand_response = []
            for element in response:
                grand_response.append(element.get("word"))

            print(grand_response)
            count = response.__len__()
            response_ = None
            if response.__len__() < MAX_COUNT:
                print('Reached here')
                response_ = trie.search_with_typo(2, key)
                response_ = list(dict(response_).keys())

            if response_ is not None:
                for key in response_:
                    if count == MAX_COUNT:
                        break
                    grand_response.append(key)
                    count += 1
        else:
            print("2:: ")
            length = 1
            count = 0
            grand_response = []
            while grand_response.__len__() < MAX_COUNT:
                response = None
                while response is None:
                    response = trie.search_with_typo(length, key)
                    length += 1

                response = list(dict(response).keys())
                for element in response:
                    if count == MAX_COUNT:
                        break
                    grand_response.append(element)
                    count += 1

            for result in response:
                print(result)
        response__ = list(IndexedSet(grand_response))
        return Response(response__, status=status.HTTP_200_OK)


