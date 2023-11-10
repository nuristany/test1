from django import forms
from .models import Donor




class DonorForm(forms.ModelForm):

    class Meta:
        model = Donor

        fields = '__all__'

    def clean_monthly_contribution(self):
        monthly_contribution = self.cleaned_data.get('monthly_contribution')
        if monthly_contribution < 1:
            raise forms.ValidationError("Monthly contribution must be at least 1.")
        return monthly_contribution

    def clean_donation_duration_months(self):
        donation_duration_months = self.cleaned_data.get('donation_duration_months')
        if donation_duration_months is not None and donation_duration_months < 1:
            raise forms.ValidationError("Donation duration must be at least 1 month.")
        return donation_duration_months
