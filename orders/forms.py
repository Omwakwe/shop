from django import forms
from orders.models import Orders

SIZE_CHOICES = (
    ('', '-----------------------'),
    ("S", 'S',),
    ("M", 'M',),
    ("L", 'L',),
)


class OrdersForm(forms.ModelForm):
    '''
    a form for ordering
    '''
    location = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Customer location', 'class': "form-control input-sm", }))
    size = forms.ChoiceField(required=True, choices=SIZE_CHOICES, widget=forms.Select(
        attrs={'placeholder': 'size', 'class': "form-control input-sm", }))

    class Meta:
        model = Orders
        fields = ['location', 'size', ]
