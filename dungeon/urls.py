from django.conf.urls import url
from dungeon import views

urlpatterns = [
    url(r'^api/v1/npcs$', views.npc_list),
    url(r'^api/v1/npcs/(?P<pk>[0-9]+)$', views.npc_detail)
]
