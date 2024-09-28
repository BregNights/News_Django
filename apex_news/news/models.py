from django.db import models

IMAGE_URL = 'https://www.infomoney.com.br/wp-content/uploads/2019/06/hacker.jpg?fit=900%2C507&quality=50&strip=all'

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class News(models.Model):
    tittle = models.CharField(max_length=200)
    subtittle = models.CharField(max_length=200)
    maintext = models.TextField()
    subtext = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, blank=True, null=True, default=IMAGE_URL)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tittle} {self.created_at}"

class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    tittle = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    email = models.CharField(max_length=60, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.tittle} {self.created_at}"

