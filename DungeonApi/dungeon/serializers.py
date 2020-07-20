from rest_framework import serializers
from dungeon.models import Encounter


class DungeonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encounter
        fields = ('id',
                  'title',
                  'description',
                  'image')
