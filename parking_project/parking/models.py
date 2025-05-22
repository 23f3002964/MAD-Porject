from django.db import models

class ParkingSpot(models.Model):
    SPOT_SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    spot_number = models.CharField(max_length=10, primary_key=True, help_text="Unique identifier for the parking spot (e.g., A101)")
    location_description = models.TextField(help_text="Description of the spot's location (e.g., Level 2, near elevator)")
    size = models.CharField(
        max_length=1,
        choices=SPOT_SIZE_CHOICES,
        default='M',
        help_text="Size of the parking spot"
    )
    is_available = models.BooleanField(default=True, help_text="Is the spot currently available?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.spot_number} ({self.get_size_display()}) - {'Available' if self.is_available else 'Occupied'}"

    class Meta:
        ordering = ['spot_number']
