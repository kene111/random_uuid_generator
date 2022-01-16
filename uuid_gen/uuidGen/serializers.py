from rest_framework import serializers
from . models import UuidGenerator
from collections import OrderedDict
import json
from functools import reduce
class UuidGeneratorSerializer(serializers.ModelSerializer):

	timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S.%f")


	class Meta:
		model = UuidGenerator
		fields = ['timestamp','uuid'] 



    # restructure the output
	def to_representation(self, uuidgenerator):
		res = OrderedDict()
		res[str(uuidgenerator.timestamp).split('+')[0]] = uuidgenerator.uuid
	
		return res
            