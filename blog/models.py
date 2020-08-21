from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Categories"
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ['created_at']
        # verbose_name_plural= "Categories"
