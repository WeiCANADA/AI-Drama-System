from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.production.views import SceneViewSet, ShotViewSet
from apps.projects.views import ProjectViewSet
from apps.stories.views import EpisodeViewSet, StoryViewSet


router = DefaultRouter()
router.register("projects", ProjectViewSet)
router.register("stories", StoryViewSet)
router.register("episodes", EpisodeViewSet)
router.register("scenes", SceneViewSet)
router.register("shots", ShotViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
