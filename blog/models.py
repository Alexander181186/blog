from django.db import models

# Create your models here.


class Tag(models.Model):
#    slug = models.SlugField(max_length=100, unique=True)
    slug = models.CharField('Тег', max_length=100, unique=True)
    
#    def save_tag(self):
#        self.save()

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField('Текст')
    tags = []
    add_tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True) #, null=True)
    tags.append(add_tags)
    
#    def get_last_tag(self):
#        return self.tags
    
#    def save_post(self):
#        self.save()
    
    def __str__(self):
        return self.title
    
    
