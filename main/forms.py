from django.utils import timezone  
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Reservation

class ReservationForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'DD.MM.YYYY', 'data-inputmask': "'mask': '99.99.9999'", 'autocomplete': 'off'}),
        label=_('Date'),
        input_formats=['%d.%m.%Y'],
    )

    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'num_persons', 'date', 'time']

    def clean_date(self):
        date_obj = self.cleaned_data.get('date')

        # Check if the date is in the past (you can adjust this logic as needed)
        if date_obj and date_obj < timezone.now().date():
            raise ValidationError(_('Date cannot be in the past.'))

        return date_obj
