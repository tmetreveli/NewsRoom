from django.db import models
from django.contrib.auth import get_user_model
from treebeard.mp_tree import MP_Node

User = get_user_model()

class Category(MP_Node):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='category_logos/')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    depth = models.IntegerField(default=0)
    path = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=320)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    publication_datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    main_image = models.ImageField(upload_to='article_images/')
    publishing = models.BooleanField(default=False)

    def __str__(self):
        return self.title