from django import forms
from solaredge.models import Scoring, Questions2, EmergencyNumbers, Customer



class ReadForm(forms.ModelForm):

    class Meta:
        model = Scoring
        fields = [
            'customer', 'question', 'score', 'note'
            ]


# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = EmergencyNumbers
        fields = ('name', 'number',)



# create a ModelForm
class QForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Customer
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        super(QForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget = forms.RadioSelect()


NUMS= [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ]

class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))
    model_choice = forms.ModelChoiceField(
            queryset=Customer.objects.all(),
            initial=0
            )