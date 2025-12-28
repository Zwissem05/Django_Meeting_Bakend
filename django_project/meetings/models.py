
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Meeting(models.Model):
    MEETING_CHOICES=[
            ('planned', 'Planned'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled')
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # lien vers l'utilisateur
    date = models.DateField(auto_now_add=True)                # date par défaut = aujourd'hui
    title = models.CharField(max_length=200)                 # titre ou description
    notes = models.TextField(blank=True)                     # notes optionnelles
    status = models.CharField(
        max_length=20,
        choices=MEETING_CHOICES,
        default='planned'
    )
    