from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser


class MyAccount(AbstractUser):
    phone = models.CharField('电话', max_length=11)
    we_chat = models.CharField('微信', max_length=30)
    qq = models.CharField('QQ', max_length=30)
    avatar = ProcessedImageField(upload_to='avatar/%Y/%m/%d',
                                 verbose_name='头像',
                                 processors=[ResizeToFill(80, 80)]
                                 )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = verbose_name = '用户'



