from pathlib import Path

from django.core.files import File
from django.test import TestCase

from .models import Category, Entry


class ModelTestCase(TestCase):
    def test_create(self):
        test_file = Path(__file__).parent / "static" / "apple-touch-icon.png"
        category = Category.objects.create(name="Test", slug="test")
        with open(test_file, "rb") as handle:
            entry = Entry.objects.create(
                title="Test Content",
                slug="test-content",
                category=category,
                summary="Summary",
                body="Content",
                image=File(handle, name="test.png"),
            )

        self.assertIsNotNone(entry.image.filters.watermark.thumbnail["800x800"])
