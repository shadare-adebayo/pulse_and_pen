from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError 

# Create your models here.
time_choices= [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening')
]

mood_choices= [
    ('super_good', 'Super Good'),
    ('fine', 'Fine'),
    ('tired', 'Tired'),
    ('stressed', 'Stressed'),
    ('sad', 'Sad')
]
class BPEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='bp_entries',
    )
    recorded_date = models.DateField()
    time_of_day = models.CharField(max_length=20, choices= time_choices)
    systolic = models.IntegerField(
        validators=[MinValueValidator(70), MaxValueValidator(250)]
    )
    diastolic = models.IntegerField(
        validators=[MinValueValidator(40), MaxValueValidator(150)]
    )
    pulse = models.IntegerField(null=True, blank= True)
    note = models.TextField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recorded_date}-{self.systolic}/{self.diastolic}"
    
    def clean(self):
        super().clean()
        if self.systolic is not None and self.diastolic is not None:
            if self.systolic <= self.diastolic:
                raise ValidationError("Systolic must be greater than diastolic")
    
    def save(self,*args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class BPJournal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name= 'bp_journals',
    )
    recorded_date = models.DateField()
    subject = models.CharField(max_length=200)
    journal = models.TextField()
    mood = models.CharField(max_length=20, choices=mood_choices)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recorded_date}-{self.subject}- feeling {self.mood}"