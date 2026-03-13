from rest_framework import generics, permissions
from .models import BPEntry, BPJournal
from .serializers import BPEntrySerializer, BPJournalSerializer

class BPEntryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BPEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPEntry.objects.filter( user=self.request.user).order_by('-recorded_date')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BPEntryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BPEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPEntry.objects.filter(user=self.request.user).order_by('-recorded_date')
    
class BPJournalListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BPJournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPJournal.objects.filter(user=self.request.user).order_by('-recorded_date')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BPJournalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BPJournalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BPJournal.objects.filter(user=self.request.user).order_by('-recorded_date')