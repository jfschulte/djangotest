from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
            return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class RedditUserName(models.Model):
    username = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.username

class UserFavorites(models.Model):
    redditUserName = models.ForeignKey(RedditUserName)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.redditUserName.username

class FavRedditor(models.Model):
    userFavorites = models.ForeignKey(UserFavorites)
    favRedditor = models.CharField(max_length=30)
    redditorImage = models.CharField(max_length=50)
    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.userFavorites.redditUserName.username + ' ' + self.favRedditor

