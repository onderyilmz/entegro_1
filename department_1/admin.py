from django.contrib import admin

# Register your models here.
from department_1.models import (
    Customer,
    Scoring,
    Questions,

    )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone',)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question',)


class ScoringAdmin(admin.ModelAdmin):
    list_display = ('customer', 'question', 'score', 'note',)



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Scoring, ScoringAdmin)

