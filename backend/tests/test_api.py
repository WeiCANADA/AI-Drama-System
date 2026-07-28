from rest_framework import status
from rest_framework.test import APITestCase

from apps.production.models import Scene, Shot
from apps.projects.models import Project
from apps.stories.models import Episode, Story
from common.models import ProductionStatus


class FoundationAPITests(APITestCase):
    def setUp(self) -> None:
        self.project = Project.objects.create(code="PRJ-001", title="Pilot Production")
        self.story = Story.objects.create(
            project=self.project,
            code="STORY-001",
            order=1,
            title="Season One Arc",
        )
        self.episode = Episode.objects.create(
            story=self.story,
            code="EP-001",
            order=1,
            title="Episode One",
        )
        self.scene = Scene.objects.create(
            episode=self.episode,
            code="SC-001",
            order=1,
            title="Opening Scene",
        )
        self.shot = Shot.objects.create(
            scene=self.scene,
            code="SH-001",
            order=1,
            title="Establishing Shot",
            status=ProductionStatus.DRAFT,
        )

    def test_project_crud(self) -> None:
        create_response = self.client.post(
            "/api/projects/",
            {"code": "PRJ-002", "title": "Second Project", "description": "Production sandbox"},
            format="json",
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        project_id = create_response.data["id"]
        detail_response = self.client.get(f"/api/projects/{project_id}/")
        self.assertEqual(detail_response.status_code, status.HTTP_200_OK)
        self.assertEqual(detail_response.data["code"], "PRJ-002")

        update_response = self.client.patch(
            f"/api/projects/{project_id}/",
            {"title": "Updated Project"},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["title"], "Updated Project")

        delete_response = self.client.delete(f"/api/projects/{project_id}/")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_hierarchy_endpoints_create_and_list(self) -> None:
        story_response = self.client.post(
            "/api/stories/",
            {
                "project": str(self.project.id),
                "code": "STORY-002",
                "order": 2,
                "title": "B Story",
                "synopsis": "Secondary plotline",
            },
            format="json",
        )
        self.assertEqual(story_response.status_code, status.HTTP_201_CREATED)

        episode_response = self.client.post(
            "/api/episodes/",
            {
                "story": str(self.story.id),
                "code": "EP-002",
                "order": 2,
                "title": "Episode Two",
            },
            format="json",
        )
        self.assertEqual(episode_response.status_code, status.HTTP_201_CREATED)

        scene_response = self.client.post(
            "/api/scenes/",
            {
                "episode": str(self.episode.id),
                "code": "SC-002",
                "order": 2,
                "title": "Second Scene",
            },
            format="json",
        )
        self.assertEqual(scene_response.status_code, status.HTTP_201_CREATED)

        shot_response = self.client.post(
            "/api/shots/",
            {
                "scene": str(self.scene.id),
                "code": "SH-002",
                "order": 2,
                "title": "Close-up",
                "duration_seconds": 5,
                "status": ProductionStatus.READY,
            },
            format="json",
        )
        self.assertEqual(shot_response.status_code, status.HTTP_201_CREATED)

        shot_list_response = self.client.get("/api/shots/")
        self.assertEqual(shot_list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(shot_list_response.data["count"], 2)
