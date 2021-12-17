from django.db import models
from config import settings
from config.utils import create_short_code
from .validators import validate_url, validate_dot_com


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class ShortenerManager(models.Manager):

    @staticmethod
    def refresh_short_codes():
        refreshed_code = 0
        qs = Shortener.objects.filter(pk__gte=1)
        for q in qs:
            q.short_code = None
            q.save()
            refreshed_code += 1
        return f'Made new {refreshed_code} code'


class Shortener(models.Model):

    original_url = models.URLField(max_length=250, blank=False, null=False)
    short_code = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == '':
            self.short_code = create_short_code(self)
        if 'http://' not in self.original_url:
            self.original_url = 'http://' + self.original_url
        super(Shortener, self).save(*args, **kwargs)

    def __str__(self):
        return self.original_url

    def __unicode__(self):
        return str(self.original_url)
