from django import forms
from .models import HealthRecord

class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['student_id', 'date', 'health_status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'health_status': forms.Select(choices=HealthRecord.HEALTH_STATUS_CHOICES)
        }