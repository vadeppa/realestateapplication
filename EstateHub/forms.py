from django import forms

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PropertyUnit, Tenant, Lease

from django.utils import timezone
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {'email': 'Email'}




class PropertyUnitForm(forms.ModelForm):
    class Meta:
        model = PropertyUnit
        fields = ['property_name', 'property_address', 'property_location', 'property_features', 'rent_cost', 'bedroom_type']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs', 'document_image']

class LeaseForm(forms.ModelForm):
    agreement_end_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), required=True)

    
    class Meta:
        model = Lease
        fields = ['tenant_id', 'property_unit', 'agreement_end_date', 'monthly_rent_date']

    def clean(self):
        cleaned_data = super().clean()
        agreement_end_date = cleaned_data.get('agreement_end_date')
        monthly_rent_date = cleaned_data.get('monthly_rent_date')

        # Validation 1: Ensure agreement_end_date is in the future
        if agreement_end_date and agreement_end_date <= timezone.now().date():
            raise forms.ValidationError("Agreement end date must be in the future.")

        # Validation 2: Ensure monthly_rent_date is between 1 and 31
        if not (1 <= monthly_rent_date <= 31):
            raise forms.ValidationError("Monthly rent date must be between 1 and 31.")
