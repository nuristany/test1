from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Donor(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'US Dollar'),
        ('AFG', 'Afghan Afghani'),
    )
    DONATION_CHOICES = (
        ('monthly', 'Monthly'),
        ('onetime', 'One-time'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    donation_type = models.CharField(max_length=10, choices=DONATION_CHOICES)
    monthly_contribution = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    donation_duration_months = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.first_name
