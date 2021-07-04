from django.contrib import admin

# Register your models here.
from solaredge.models import (
    Customer,
    Scoring,
    Questions,
    QuestionChoice,
    Questions2,
    Scoring2,
    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone',)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'carpan')


class ScoringAdmin(admin.ModelAdmin):
    list_display = ('customer', 'question', 'score', 'note',)


class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = ('score',)

class Questions2Admin(admin.ModelAdmin):
    list_display = ('question', 'options1', 'options2', 'options3', 'options4', 'carpan')



class Scoring2Admin(admin.ModelAdmin):
    list_display = ('customer',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Scoring, ScoringAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)
admin.site.register(Questions2, Questions2Admin)
admin.site.register(Scoring2, Scoring2Admin)

