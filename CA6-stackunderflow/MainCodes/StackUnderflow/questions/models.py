from django.db import models
from django.urls import reverse
from users.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100,null=True)
    body = models.TextField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions',null=True)
    tags = models.ManyToManyField('Tag',blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    upvoters = models.ManyToManyField(User,related_name="upvoted_questions" , blank = True)
    downvoters = models.ManyToManyField(User,related_name="downvoted_questions" , blank= True)


    @property
    def votes(self):
        up_counts = self.upvoters.count()
        dwon_count = self.downvoters.count()
        return up_counts - dwon_count



class Tag(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE , related_name='answers' , null=True )
    body = models.TextField(null=True)
    upvoters = models.ManyToManyField(User, related_name="upvoted_answers",blank=True)
    downvoters = models.ManyToManyField(User,related_name="downvoted_answers",blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers',null=True)

    @property
    def votes(self):
        up_count = self.upvoters.count()
        down_count = self.downvoters.count()
        return up_count - down_count
