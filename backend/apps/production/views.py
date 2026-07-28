from rest_framework.viewsets import ModelViewSet

from apps.production.models import Scene, Shot
from apps.production.serializers import SceneSerializer, ShotSerializer


class SceneViewSet(ModelViewSet):
    queryset = Scene.objects.select_related("episode", "episode__story", "episode__story__project").all()
    serializer_class = SceneSerializer


class ShotViewSet(ModelViewSet):
    queryset = Shot.objects.select_related(
        "scene",
        "scene__episode",
        "scene__episode__story",
        "scene__episode__story__project",
    ).all()
    serializer_class = ShotSerializer

# Create your views here.
