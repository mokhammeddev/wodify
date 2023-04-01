from django.db import models
from profile.models import User


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey("profile.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class View(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view = models.IntegerField(default=1)

    def __str__(self):
        return self.view


class Comment(models.Model):
    author = models.ForeignKey("profile.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name() == "":
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.username}'s comment"


class SubContent(models.Model):
    content = models.TextField(null=True, blank=True)
    article = models.OneToOneField(Article, on_delete=models.CASCADE)


class SubContentImage(models.Model):
    sub_content = models.ForeignKey(SubContent, on_delete=models.CASCADE, related_name='subimage')
    image = models.ImageField()
    is_wide = models.BooleanField(default=False)

