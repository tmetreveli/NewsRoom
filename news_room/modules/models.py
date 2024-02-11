from django.db import models
from content.models import Category, Article


class Menu(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Block(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    visual_selection = models.CharField(max_length=50)
    block_position = models.CharField(max_length=50)
    block_row = models.IntegerField()
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title