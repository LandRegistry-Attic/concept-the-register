from django.conf.urls import url, patterns, include
from concept_the_register import Titles
from rest_framework import viewsets, routers

# ViewSets define the view behavior.
class TitlesViewSet(viewsets.ModelViewSet):
    model = Titles

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'titles', TitlesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
