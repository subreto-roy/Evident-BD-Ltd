from django.db import models
from django.contrib.auth.models import User

class InputHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    input_values = models.TextField()
