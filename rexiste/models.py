from django.db import models
from django.db.models import signals
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin

# Create your models here.

class Post(models.Model, HitCountMixin):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=140)
    text = RichTextUploadingField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True)
    cover = models.ImageField(upload_to='Media', null=False, blank=False, default="Media/atom.png")

    hit_count_generic = GenericRelation(
        HitCount, object_id_field = 'object_pk',
        related_query_name = 'hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk, 'slug': self.slug})

    def article_pre_save(signal, instance, sender, **kwargs):
        instance.slug = slugify(instance.title)

    signals.pre_save.connect(article_pre_save, sender="rexiste.Post")



