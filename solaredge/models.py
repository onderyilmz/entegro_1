from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django_utils.choices import Choice, Choices

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f" {self.name} {self.phone} "

    class Meta:
        verbose_name = 'Müşteri'
        verbose_name_plural = 'Müşteriler'


class Questions(models.Model):
    question = models.CharField(max_length=150)
    carpan = models.IntegerField()

    def __str__(self):
        return f" {self.question} ->  {self.carpan}"

    class Meta:
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'


class QuestionChoice(models.Model):
    score = models.IntegerField(
            default='0',
            )

    def __str__(self):
        return f" {self.score}"

    class Meta:
        verbose_name = 'Soru Puanı'
        verbose_name_plural = 'Soru Puanlar'


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
    score = models.ForeignKey(
            QuestionChoice,
            on_delete=models.CASCADE,
            null=True,
            )
    note = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f" {self.score} {self.customer} {self.question}"

    class Meta:
        verbose_name = 'Toplam Puan'
        verbose_name_plural = 'Toplam Puanlar'



class Questions2(models.Model):
    question = models.CharField(max_length=150)
    options1 = models.IntegerField()
    options2 = models.IntegerField()
    options3 = models.IntegerField()
    options4 = models.IntegerField()

    carpan = models.IntegerField()

    def __str__(self):
        return f" {self.question} ->  {self.carpan}"

    class Meta:
        db_table = "sorular"
        verbose_name = 'Sorularrrr'
        verbose_name_plural = 'Sorularrrrr'



class Scoring2(models.Model):
    customer = models.CharField(max_length=150)
    note = models.CharField(max_length=250)
    def __str__(self):
        return f" {self.customer}"

    class Meta:
        verbose_name = 'Toplam Puan2'
        verbose_name_plural = 'Toplam Puanlar2'


class EmergencyNumbers(models.Model):
    name = models.TextField(max_length=50)
    number = models.TextField(max_length=10)
