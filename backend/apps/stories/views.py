from rest_framework.viewsets import ModelViewSet

from apps.stories.models import Episode, Story
from apps.stories.serializers import EpisodeSerializer, StorySerializer


class StoryViewSet(ModelViewSet):
    queryset = Story.objects.select_related("project").all()
    serializer_class = StorySerializer


class EpisodeViewSet(ModelViewSet):
    queryset = Episode.objects.select_related("story", "story__project").all()
    serializer_class = EpisodeSerializer

# Create your views here.
