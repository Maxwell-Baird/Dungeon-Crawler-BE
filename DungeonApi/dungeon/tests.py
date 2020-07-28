from django.test import RequestFactory, TestCase
from rest_framework.test import APIRequestFactory

from .views import *
from .models import *

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        npc = Npc.objects.create(
            id = 100,
            name = "Squid",
            attack = 5,
            defense = 5,
            health = 10,
            description = "It is red and orange. 5000 feet tall and hates pineapples.",
            dialogue = [
            {
                "dialogue": "how are you",
                "response": "good",
                "choices": [1, 2, 3]
            },{
                "dialogue": "nice weather today",
                "response": "sure is!",
                "choices": [0, 2, 3]
            },{
                "dialogue": "what are you up to",
                "response": "fetching water",
                "choices": [4]
            },{
                "dialogue": "can you heal me?",
                "response": "yeah!",
                "action": "heal",
                "choices": [0, 1, 2]
            },{
                "dialogue": "can I help?",
                "response": "no, but wanna join my wizardry school?",
                "choices": [5, 6]
            },{
                "dialogue": "sure!",
                "response": "great!",
                "choices": [0, 1, 3]
            },{
                "dialogue": "not really!",
                "response": "aw, ok!",
                "choices": [0, 1, 3]
            }],
            options = [{"name": "Fight", "type": "aggressive"}, {"name": "Talk", "type": "passive"}],
            location = "Beach"
        )

    def test_npc_list_get(self):
        request = self.factory.get('/api/v1/npcs')

        response = npc_list(request)

        self.assertEqual(response.status_code, 200)



    def test_npc_list_post_fail(self):
      data = {
              "id": 2,
              "name": "Bear",
              "attack": 5,
              "defense": 5,
              "health": 10}
      request = self.factory.post('/api/v1/npcs', data, format='json')

      response = npc_list(request)

      self.assertEqual(response.status_code, 400)

    def test_npc_list_post(self):
        self.assertEqual(Npc.objects.count(), 1)
        data = {
          "id": 2,
          "name": "Bear",
          "attack": 5,
          "defense": 5,
          "health": 10,
          "description": "Oh, crap you woke a bear up from hibernation!!!!",
          "dialogue": [
            {
              "dialogue": "how are you",
              "response": "good",
              "choices": [1, 2, 3]
            },{
              "dialogue": "nice weather today",
              "response": "sure is!",
              "choices": [0, 2, 3]
            },{
              "dialogue": "what are you up to",
              "response": "fetching water",
              "choices": [4]
            },{
              "dialogue": "can you heal me?",
              "response": "yeah!",
              "action": "heal",
              "choices": [0, 1, 2]
            },{
              "dialogue": "can I help?",
              "response": "no, but wanna join my wizardry school?",
              "choices": [5, 6]
            },{
              "dialogue": "sure!",
              "response": "great!",
              "choices": [0, 1, 3]
            },{
              "dialogue": "not really!",
              "response": "aw, ok!",
              "choices": [0, 1, 3]
            }
          ],
          "options": [{"name": "Fight", "type": "aggressive"}, {"name": "Talk", "type": "passive"}],
          "location": "Forest"
        }
        request = self.factory.post('/api/v1/npcs', data, format='json')

        response = npc_list(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Npc.objects.count(), 2)

    def test_npc_detail_get(self):

        request = self.factory.get('/api/v1/npcs/100')

        response = npc_detail(request, 100)

        self.assertEqual(response.status_code, 200)

    def test_npc_detail_get_fail(self):
        request = self.factory.get('/api/v1/npcs/5')

        response = npc_detail(request, 5)

        self.assertEqual(response.status_code, 404)

    def test_npc_detail_put(self):
        data = {
            	"name": "squid",
            	"dialogue": [{"text": "text"}],
            	"options": [{"text": "text"}]
                }
        request = self.factory.put('/api/v1/npcs/100', data, format='json')

        response = npc_detail(request, 100)

        self.assertEqual(response.status_code, 202)

    def test_npc_detail_put_fail(self):
        data = {
            	"name": "squid"
                }

        request = self.factory.put('/api/v1/npcs/100', data, format='json')
        response = npc_detail(request, 100)

        self.assertEqual(response.status_code, 400)

    def test_npc_detail_delete(self):
        self.assertEqual(Npc.objects.count(), 1)

        request = self.factory.delete('/api/v1/npcs/100')

        response = npc_detail(request, 100)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Npc.objects.count(), 0)

    def test_npc_list_get_delete(self):
        self.assertEqual(Npc.objects.count(), 1)

        request = self.factory.delete('/api/v1/npcs')

        response = npc_list(request)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Npc.objects.count(), 0)
