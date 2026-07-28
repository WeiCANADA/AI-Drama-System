from rest_framework import serializers

from apps.production.models import Scene, Shot


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = (
            "id",
            "episode",
            "code",
            "order",
            "title",
            "summary",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        fields = (
            "id",
            "scene",
            "code",
            "order",
            "title",
            "duration_seconds",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
