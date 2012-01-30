from django.template.defaultfilters import slugify
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from taggit.managers import TaggableManager

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import md5


site = Site.objects.all()[0]

class Snipt(models.Model):
    """An individual Snipt."""

    user     = models.ForeignKey(User, blank=True, null=True)

    title    = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug     = models.SlugField(max_length=255, blank=True)
    tags     = TaggableManager()

    lexer    = models.CharField(max_length=50)
    code     = models.TextField()
    stylized = models.TextField(blank=True, null=True)
    line_count = models.IntegerField(blank=True, null=True, default=None)

    key      = models.CharField(max_length=100, blank=True, null=True)
    public   = models.BooleanField(default=False)
    
    created  = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):

        if not self.key:
            self.key = md5.new(self.slug).hexdigest()

        if not self.slug:
            self.slug = slugify(self.title)[:50]

        self.stylized = highlight(self.code,
                                  get_lexer_by_name(self.lexer, encoding='UTF-8'),
                                  HtmlFormatter())
        self.line_count = len(self.code.split('\n'))

        return super(Snipt, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/" % (self.user.username, self.slug)

    def get_full_absolute_url(self):
        if settings.DEBUG:
            root = 'http://snipt.localhost'
        else:
            if settings.USE_HTTPS:
                root = 'https://snipt.net'
            else:
                root = 'http://snipt.net'
        return "%s/%s/%s/" % (root, self.user.username, self.slug)

    def get_embed_url(self):
        return 'http%s://%s/embed/%s/' % ('s' if settings.USE_HTTPS else '',
                                          site.domain,
                                          self.key)

    @property
    def sorted_tags(self):
        return self.tags.all().order_by('name')

    @property
    def lexer_name(self):
        return get_lexer_by_name(self.lexer).name
