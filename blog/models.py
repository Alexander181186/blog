from django.db import models


class Tag(models.Model):
    slug = models.CharField('Тег', max_length=100, unique=True)

    def __str__(self):
        return self.slug
        
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField('Текст')
    add_tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True)
    author = models.CharField('Автор', max_length=30)
    text = models.TextField('Текст')
    created_date = models.DateField(auto_now_add=True)   
    
    def __str__(self):
        return self.text   
