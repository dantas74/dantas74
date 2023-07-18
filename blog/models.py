from django.core.validators import MinLengthValidator
from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    caption = models.CharField(max_length=24)

    def __str__(self):
        return self.caption


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=60)
    excerpt = models.CharField(max_length=255)
    content = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to='posts/images', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)

    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return f'{self.title}, {self.excerpt[0:11]}...'


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(max_length=480)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user_name}, {self.text[0:11]}...'
