from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UuidGeneratorSerializer
from .models import UuidGenerator
import uuid
from rest_framework.response import Response
from collections import ChainMap, OrderedDict
from functools import reduce

# Create your views here.
class Uuid(APIView):

	def get(self, request, format=None):

        # create a new uuid on request
		UuidGenerator.objects.create(uuid=uuid.uuid4())

		#get previous uuid(s)
		uuids = UuidGenerator.objects.all().order_by("-timestamp")

		# serialize uuid(s)
		serializer  = UuidGeneratorSerializer(uuids, many=True)

        # re-structure the response
		data = serializer.data
		#output = OrderedDict(ChainMap(*a))
		output = reduce(lambda a, b: {**a, **b}, data)

		return Response(output)

