from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Interview(models.Model):
    
    name = models.CharField(verbose_name='Название', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=255)
    date_start = models.DateTimeField(verbose_name='Дата начала', blank=False)
    date_end = models.DateTimeField(verbose_name='Дата конца', blank=False)
    
    class Meta:
        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'
    
    def __str__(self):
        return self.name


class Question(models.Model):
    
    text = models.TextField(verbose_name='Текст')
    type = models.IntegerField(verbose_name='Тип', default=1)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="question", verbose_name='Опрос')
    user = models.ManyToManyField(User, verbose_name='Пользователь', blank=True, related_name="question", through='QuestionReply')
    
    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.text


class Variant(models.Model):
    
    uid = models.CharField(blank=False, max_length=10, default=1, verbose_name='Индекс варианта ответа')
    text = models.TextField(verbose_name='Описание варианта ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="variant", verbose_name='Вопрос')
    
    class Meta:
        verbose_name = 'Варианты ответа'
        verbose_name_plural = 'Варианты ответа'
    
    def __str__(self):
        return self.text


class QuestionReply(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = JSONField()
    
    class Meta:
        verbose_name = 'Ответы'
        verbose_name_plural = 'Ответы'
    
    def __str__(self):
        return self.question.text
