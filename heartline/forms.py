from django import forms
from .models import BPEntry

class BPEntryForm(forms.ModelForm):
    class Meta:
        model = BPEntry
        fields = ['recorded_date', 'time_of_day', 'systolic', 'diastolic', 'pulse', 'note',]

        widgets= {
            'recorded_date': forms.DateInput(attrs={'type':'date'}),
            'note': forms.TextInput(attrs={'rows': 3}),
        }