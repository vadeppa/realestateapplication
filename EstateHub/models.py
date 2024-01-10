from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models





class PropertyUnit(models.Model):
    property_name = models.CharField(max_length=255, verbose_name="property owner")
    property_address = models.TextField()
    property_location = models.CharField(max_length=255)
    property_features = models.TextField()
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    bedroom_type = models.CharField(max_length=10, choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK')])

    def clean(self):
        if self.rent_cost <= 0:
            raise ValidationError("Rent cost must be a positive number")

    def __str__(self):
        return f"{self.property_name} - {self.bedroom_type}"

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    
    DOCUMENT_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('pancard', 'PAN Card'),
        ('passport', 'Passport'),
    ]

    document_proofs = models.CharField(max_length=10, choices=DOCUMENT_CHOICES)
    document_image = models.FileField(null=True, upload_to='tenant_documents/')

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    property_unit = models.ForeignKey(PropertyUnit, on_delete=models.PROTECT)
    agreement_end_date = models.DateField()

    def clean(self):
        # Validation 1: Ensure agreement_end_date is in the future
        if self.agreement_end_date and self.agreement_end_date <= timezone.now().date():
            raise ValidationError("Agreement end date must be in the future.")

    monthly_rent_date = models.PositiveIntegerField()

    # Validation 2: Ensure monthly_rent_date is between 1 and 31
    def clean_monthly_rent_date(self):
        if not (1 <= self.monthly_rent_date <= 31):
            raise ValidationError("Monthly rent date must be between 1 and 31.")

    def __str__(self):
        return f"{self.tenant_id.name}'s Lease"

