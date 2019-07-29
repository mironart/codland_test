from django.db import models

class Article(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    title = models.CharField(max_length=500, verbose_name='Название поста')
    body = models.TextField(verbose_name='Текст поста')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return '({0}) Пост: {1}, от {2}'.format(self.id, self.title, self.date_created.strftime('%d-%m-%y %H:%M'))



