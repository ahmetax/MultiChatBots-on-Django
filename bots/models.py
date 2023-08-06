from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

DEFAULT_CATEGORY=1

# 'title', 'content', 'keywords', 'link', 'local', 'counter', 'category', 'notes', 'image'
class Bot(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title', blank=True, null=True)
    content = models.TextField(verbose_name='Content', blank=True, null=True)
    keywords = models.CharField(max_length=250, verbose_name='Keywords', blank=True, null=True)
    link = models.CharField(max_length=250, verbose_name='Link', blank=True, null=True)
    local = models.CharField(max_length=250, verbose_name='LocalLink', blank=True, null=True)
    counter = models.IntegerField(verbose_name='Counter', default=0)
    category = models.ForeignKey(Category, default=DEFAULT_CATEGORY, on_delete=models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(verbose_name='Notes', blank=True, null=True)
    image = models.ImageField(verbose_name='Image', blank=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Bot, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-counter",'-id']
        
    def __str__(self):
        return self.title

# 'title', 'content', 'keywords', 'link', 'local', 'counter', 'category', 'notes', 'image'
class BotFilter(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=20, blank=True, null=True)
    keywords = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=20, blank=True, null=True)
    link = models.CharField(max_length=20, blank=True, null=True)
    local = models.CharField(max_length=20, blank=True, null=True)
    # user = models.CharField(max_length=20, blank=True, null=True)
