from django.db import models


class Text(models.Model):
    text_snippet = models.CharField(max_length=256)

    def get_absolute_url(self):
        return "/api/output/%i/" % self.id

