from django.db import models

# Create your models here.
time_choices= [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening')
]
class BPEntry(models.Model):
    recorded_date = models.DateField()
    time_of_day = models.CharField(max_length=20, choices= time_choices)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    pulse = models.IntegerField(null=True, blank= True)
    note = models.TextField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recorded_date}-{self.systolic}/{self.diastolic}"


