from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=50)
    condition = models.TextField(max_length=1500)
    answer = models.FloatField()
    theme = models.CharField(max_length=20)

    def __str__(self):
        return self.title + ' ' + str(self.answer)


class Answer(models.Model):
    answer = models.FloatField()


class ProblemTest(models.Model):
    title = models.CharField(max_length=40)
    condition = models.TextField(max_length=400)
    answer = models.FloatField()


class Theme(models.Model):
    theme_name = models.CharField(max_length=50)
    theme_link = models.CharField(max_length=30)
    user_id = models.FloatField()
