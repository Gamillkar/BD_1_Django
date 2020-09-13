from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):

    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.TextField()
    price = models.CharField(max_length=15)
    release_date = models.CharField(max_length=10)
    lte_exists = models.CharField(max_length=2)
    slug = models.SlugField()

    def title_slug(self):
        return slugify(self.name)