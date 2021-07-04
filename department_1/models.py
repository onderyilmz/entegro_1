from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
QUESTION_VALUE = (
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    )


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f" {self.name} {self.phone} "

    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteriler'


class Questions(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'


class Scoring(models.Model):
    customer = models.ForeignKey(
            Customer,
            on_delete=models.CASCADE,
            null=True,
            )
    question = models.ForeignKey(
            Questions,
            on_delete=models.CASCADE,
            null=True,
            )
    score = models.IntegerField(choices=QUESTION_VALUE)
    note = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f" {self.score} {self.customer} {self.question}"

    class Meta:
        verbose_name = 'Toplam Puan'
        verbose_name_plural = 'Toplam Puanlar'



class Ques(models.Model):
    question = models.CharField(max_length=50)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Sor'
        verbose_name_plural = 'Sorlar'