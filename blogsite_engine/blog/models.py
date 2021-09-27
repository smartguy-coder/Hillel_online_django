from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    user_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username', ]


class Tag(models.Model):
    tag_category = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_category

    class Meta:
        ordering = ['tag_category', ]



class Post(models.Model):
    post_title = models.CharField(max_length=200, blank=False, unique=True)
    post_text = models.TextField(max_length=1000, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    post_publish_time = models.DateTimeField('time published', auto_now_add=True)
    post_amend_time = models.DateTimeField('time amended', auto_now=True)
    post_published = models.BooleanField(default=True)
    category = models.ForeignKey(Tag, on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return f'"TITLE": {self.post_title}, "POST_TEXT": {self.post_text[0:50]+"..."}, "AUTHOR": {self.author}'

    class Meta:
        ordering = ['-post_publish_time', 'post_title']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    comment_time = models.DateTimeField('comment time published', auto_now_add=True)
    comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)

    class Meta:
        # new first
        ordering = ['-comment_time', ]

    def __str__(self):
        return self.comment_text
