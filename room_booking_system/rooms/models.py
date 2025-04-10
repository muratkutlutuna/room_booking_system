from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number}"
