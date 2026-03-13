from rest_framework import serializers
from .models import BPEntry, BPJournal

class BPEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BPEntry
        fields = [
            'id',
            'recorded_date',
            'time_of_day',
            'systolic',
            'diastolic',
            'pulse',
            'note',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

class BPJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BPJournal
        fields = [
            'id',
            'recorded_date',
            'subject',
            'mood',
            'journal',
            'created_at',
        ]
        read_only_fields =['id', 'created_at']