from django.contrib import admin
from .models import BPEntry, BPJournal
# Register your models here.
admin.site.register(BPEntry)
admin.site.register(BPJournal)