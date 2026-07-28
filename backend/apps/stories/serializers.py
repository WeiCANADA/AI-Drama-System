from rest_framework import serializers

from apps.stories.models import Episode, Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            "id",
            "project",
            "code",
            "order",
            "title",
            "synopsis",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = (
            "id",
            "story",
            "code",
            "order",
            "title",
            "synopsis",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
