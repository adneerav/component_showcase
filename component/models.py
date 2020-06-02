from django.conf import settings
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from account.models import Profile
from language.models import Language
from technology.models import Technology
from django.utils.translation import gettext_lazy as _


class Component(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'


class Detail(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='components_detail',
                                  related_query_name='component_detail', null=False, blank=False)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="technologies")
    contributors = models.ManyToManyField(Profile, related_name="component_contributors",
                                          help_text="Developers who worked on component")
    language = models.ManyToManyField(Language, related_name="languages")
    banner_image = models.ImageField(upload_to='uploads/component/images/banner/', blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    git_url = models.URLField(null=True, verbose_name=_('github URL'))
    video_url = models.URLField(max_length=500, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, editable=True)
    updated_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.get_comp_with_tech()

    def get_comp_with_tech(self):
        return "{} - {}".format(self.component.name, self.get_technologies())

    def get_technologies(self):
        return self.technology

    def get_languages(self):
        return ",".join([str(t) for t in self.language.all()])

    def get_contributor_name(self):
        return self.contributors

    class Meta:
        verbose_name = 'Component Detail'
        verbose_name_plural = 'Component Details'


class DetailImage(models.Model):
    component_detail_image = models.ForeignKey(Detail, verbose_name=_('component'),
                                               on_delete=models.CASCADE,
                                               related_name='images', related_query_name='image')
    image_url = models.ImageField(upload_to='uploads/content/images/', blank=False, null=False)

    def image_tag(self):
        print(self.image_url)
        return mark_safe(
            '<a href="{}{}" target="_blank"><img src="{}{}" width="32" height="32" /></a>'.
                format(settings.MEDIA_URL, self.image_url, settings.MEDIA_URL, self.image_url))

    image_tag.allow_tags = True

    def __str__(self):
        return self.component_detail_image.component

    class Meta:
        verbose_name = 'Component Image'
        verbose_name_plural = 'Component Images'
