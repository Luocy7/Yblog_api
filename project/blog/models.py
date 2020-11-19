from django.db import models
from django.conf import settings
from blog.utils import post_reverse
from core.utils import generate_rich_content

from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Category"), max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


def get_default_cate():
    return Category.objects.get_or_create(name='Default')[0]


class Tag(models.Model):
    name = models.CharField(_("Tag"), max_length=100)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    # 文章标题
    title = models.CharField(_("Title"), max_length=70)

    # 文章的正文来使用 TextField 来存储大段文本。
    markdown = models.TextField(_("Post Markdown"))

    html = models.TextField(_("Html"), blank=True)

    # 文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField(_("Datetime Created"), auto_now_add=True)
    modified_time = models.DateTimeField(_("Datetime Modified"), auto_now=True)

    # 文章摘要，指定 CharField 的 blank=True 参数值后就可以允许空值了。
    excerpt = models.CharField(_("Excerpt"), max_length=200, blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 且自 django 2.0 以后，ForeignKey 必须传入一个 on_delete 参数用来指定当关联的数据被删除时，被关联的数据的行为，
    # 我们这里假定当某个分类被删除时，该分类下全部文章设置为默认分类，因此使用 models.SET()
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        on_delete=models.SET(get_default_cate),
        related_name='related_posts'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_("Tag"),
        blank=True,
        related_name='related_posts'
    )

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name='related_posts'
    )

    # 新增 post_views 字段记录阅读量
    post_views = models.PositiveIntegerField(_("Post Views"), default=0, editable=False)

    def rich_content(self):
        return generate_rich_content(self.markdown)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    def api_url(self):
        return post_reverse("post-detail", kwargs={"pk": self.pk})

    def detail_url(self):
        return post_reverse("detail", kwargs={"pk": self.pk})

    def increase_views(self):
        self.post_views += 1
        self.save(update_fields=["post_views"])

    def save(self, *args, **kwargs):
        if not self.category:
            self.category = get_default_cate()
        if not self.html:
            self.html = generate_rich_content(self.markdown)
        super(Post, self).save(*args, **kwargs)


class FriendLink(models.Model):
    link_avatar = models.CharField(_("Link Avatar"), max_length=200, blank=True)
    link_name = models.CharField(_("Link Name"), max_length=200)
    link_url = models.CharField(_("Link Url"), max_length=200)
    link_order = models.IntegerField(_("Link Order"))

    class Meta:
        verbose_name = _("Friend Link")
        verbose_name_plural = verbose_name
        ordering = ["link_order"]

    def save(self, *args, **kwargs):
        if not self.link_order:
            try:
                last = FriendLink.objects.order_by("-link_order")[0]
                self.link_order = last.link_order + 1
            except IndexError:
                self.link_order = 0
        if 'update_fields' in kwargs and 'link_order' not in kwargs['update_fields']:
            kwargs['update_fields'].append('link_order')
        super(FriendLink, self).save(*args, **kwargs)
