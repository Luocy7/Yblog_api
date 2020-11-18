from django.conf import settings
from django.db import models
from django.db.models import F
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from .utils import generate_rich_content


class AbstractEntry(TimeStampedModel):
    title = models.CharField(_("title"), max_length=255)
    body = models.TextField(_("body"))
    brief = models.TextField(_("brief"), blank=True)
    excerpt = models.TextField(_("excerpt"), blank=True)
    views = models.PositiveIntegerField(_("views"), default=0, editable=False)
    pub_date = models.DateTimeField(_("publication datetime"), blank=True, null=True)
    show_on_index = models.BooleanField(_("show on index"), default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("author"),
        on_delete=models.CASCADE
    )
    comment_enabled = models.BooleanField(_("comment enabled"), default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    @property
    def toc(self):
        return self.rich_content.get("toc", "")

    @property
    def body_html(self):
        return self.rich_content.get("content", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)

    @cached_property
    def num_words(self):
        # Todo: 使用更加精确的字数统计算法
        return len(strip_tags(self.body_html))

    def increase_views(self):
        self.__class__.objects.filter(pk=self.pk).update(views=F("views") + 1)
