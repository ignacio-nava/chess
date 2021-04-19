from django.db import models
from django.utils.text import slugify
from django.conf import settings

from ckeditor.fields import RichTextField

class Article(models.Model):
    image_show = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=200)
    body = RichTextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_unique_slug(self):
        unique_slug = slugify(self.title)
        count = 1
        while Article.objects.filter(slug=unique_slug).exists():
            count += 1
            unique_slug = f"{unique_slug}{count}"
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
