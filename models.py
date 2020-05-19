from django.db import models
from django.utils import timezone

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery')

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return 'Category {0} Id {1}'.format(self.category, self.id)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='gallery')
    cat = models.ManyToManyField(Category)

    def __str__(self):
        return 'Post Subject {0} Date {1} Cat {2}'.format(self.subject, self.date, self.cat)

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 200)

    def __str__(self):
        return 'username: {0}'.format(self.username)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return 'Comment: {0} by {1}'.format(self.comment, self.username)