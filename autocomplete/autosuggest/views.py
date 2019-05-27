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

# Create your views here.


class SuggestViewSet(ViewSet):

    permission_classes = [AllowAny, ]
    authentication_classes = []

    @action(methods=['get'], detail=False)
    def autocomplete(self, request):
        key = request.query_params.get('key', None)
        trie = OurRepo.getInstance().our_trie_root
        comp = trie.AllSuggestions(key)

        if comp == 1:
            response = trie.words
            print(' 1: The type of response is: ' + str(type(response)))
            grand_response = []
            for element in response:
                grand_response.append(element.get("word"))

            print(grand_response)
            count = response.__len__()
            response2 = None
            if response.__len__() < 25:
                print('Reached here')
                response2 = trie.search_with_typo(key, 1)
                response2 = list(dict(response2).keys())

            if response2 is not None:
                for key in response2:
                    if count == 25:
                        break
                    grand_response.append(key)
                    count = count+1

        else:
            print("2:: ")
            length = 1
            count = 0
            grand_response = []
            while grand_response.__len__() < 25 and length < 4:
                response = None
                while response is None:
                    response = trie.search_with_typo(key, length)
                    length = length + 1

                response = list(dict(response).keys())
                for element in response:
                    if count ==25:
                        break
                    grand_response.append(element)
                    count = count +1

            for result in response:
                print(result)

        response_status = status.HTTP_200_OK

        return Response(grand_response, status=response_status)

    @action(methods=['get'], detail=False)
    def autocomplete2(self, request):
        key = request.query_params.get('key', None)

        trie = OurRepo.getInstance().our_trie_root
        comp = trie.AllSuggestions(key)


        # if comp == -1 or comp ==0:
        #     print('Here 1')
        #     OurRepo.getInstance().our_map.suggestion(key)
        #     response = OurRepo.getInstance().our_map.words

        grand_response = []
        if comp == 1:
            print('Here 2')
            response = trie.words
            print('The type of response is: ' + str(type(response)))
            grand_response = set()
            for element in response:

                grand_response.add(element.get("word"))

            print(grand_response)
            count = response.__len__()
            response2 = None
            if response.__len__() < 25:
                print('Reached here')
                response2 = trie.search_with_typo(key, 1)
                response2 = list(dict(response2).keys())

            if response2 is not None:
                for key  in response2:
                    grand_response.add(key)

                # print(response2)
                # print('type of response2 is: ' + str(type(response2)))

        else:
            print('Here3')
            length = 1
            grand_response = []
            while grand_response.__len__() < 25 and length < 5:
                response = None
                while response is None:
                    response = trie.search_with_typo(key, length)
                    length = length + 1

                response = list(dict(response).keys())
                for element in response:
                    grand_response.append(element)

            for result in response:
                print(result)

        response_status = status.HTTP_200_OK

        return Response(grand_response, status=response_status)
