from django.conf.urls import url
from dungeon import views

urlpatterns = [
    url(r'^api/v1/encounters$', views.encounter_list),
    url(r'^api/v1/encounters/(?P<pk>[0-9]+)$', views.encounter_detail),
]
