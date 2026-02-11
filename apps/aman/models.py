from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название сайта')
    logo = models.ImageField(upload_to='logo', verbose_name='Логотип')
    icon = models.ImageField(upload_to='icon', verbose_name='Иконка')
    descriptions = models.TextField(verbose_name='Описание сайта')
    phone_number = models.CharField(max_length=25, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    locate = models.URLField(verbose_name='Ссылка на карту')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

# Create your models here.
