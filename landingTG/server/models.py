from enum import verify

from django.db import models

class Faq(models.Model):
    class Meta:
        verbose_name = 'Вопрос/Ответ'
        verbose_name_plural = 'Вопросы/Ответы'

    title = models.CharField(verbose_name='Вопрос', max_length=155)
    ask = models.CharField(verbose_name='Ответ', max_length=700)

    def __str__(self):
        return self.title


class Price(models.Model):
    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы'

    name = models.CharField(verbose_name='Наименование продукта', max_length=155)
    price = models.IntegerField(verbose_name='Цена продукта')
    is_done = models.BooleanField(verbose_name='Важный?')
    dsc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name


class SendMessage(models.Model):
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    name_user = models.CharField(verbose_name='Имя пользователя', max_length=255)
    email = models.EmailField(verbose_name='Почта пользователя', max_length=155)
    ask = models.TextField(verbose_name='Вопрос пользователя')


class Reviews(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    dsc = models.CharField(verbose_name='Отзыв', max_length=600)
    user = models.CharField(verbose_name='От кого (имя пользователя)', max_length=155)

