from django import forms
from .models import BPEntry, BPJournal

class BPEntryForm(forms.ModelForm):
    class Meta:
        model = BPEntry
        fields = ['recorded_date', 'time_of_day', 'systolic', 'diastolic', 'pulse', 'note',]

        widgets= {
            'recorded_date': forms.DateInput(attrs={'type':'date'}),
            'note': forms.TextInput(attrs={'rows': 3}),
        }

class BPJournalForm(forms.ModelForm):
    class Meta:
        model = BPJournal
        fields = ['recorded_date', 'subject', 'journal', 'mood',]

        widgets= {
            'recorded_date': forms.DateInput(attrs={'type':'date'}),
            'journal': forms.Textarea(attrs={'rows': 3}),
        }
  