from rest_framework import serializers
from dungeon.models import Npc


class NpcSerializer(serializers.ModelSerializer):

    class Meta:
        model = Npc
        fields = ('id',
                  'name',
                  'attack',
                  'defense',
                  'health',
                  'dialogue',
                  'options',
                  'location')
