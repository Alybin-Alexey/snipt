from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):

    EDITOR_CHOICES = (
        ('C', 'CodeMirror'),
        ('T', 'Textarea'),
    )

    THEME_CHOICES = (
        ('D', 'Default'),
        ('A', 'Pro Adams'),
    )

    user            = models.ForeignKey(User, unique=True)
    is_pro          = models.BooleanField(default=False)
    stripe_id       = models.CharField(max_length=100, null=True, blank=True)

    blog_title      = models.CharField(max_length=250, null=True, blank=True)
    blog_theme      = models.CharField(max_length=1,   null=False, blank=False, default='D', choices=THEME_CHOICES)
    blog_domain     = models.CharField(max_length=250, null=True, blank=True)
    default_editor  = models.CharField(max_length=250, null=False, blank=False, default='C', choices=EDITOR_CHOICES)

    gittip_username  = models.CharField(max_length=250, null=True, blank=True)
    disqus_shortname = models.CharField(max_length=250, null=True, blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
