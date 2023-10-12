from rest_framework import serializers
from.models import user_query



class userSerializer(serializers.ModelSerializer):
   class Meta:
      model = user_query
      fields = ['name', 'email','desc','status']