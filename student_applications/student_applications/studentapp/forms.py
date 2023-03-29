from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.CharField)
    password = forms.CharField(widget=forms.PasswordInput)
    
class ApplicationForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(queryset=Materials.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Application
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),

                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
        self.fields['department'].queryset = Department.objects.all()
        self.fields['purpose'].queryset = Purpose.objects.all()
        self.fields['materials'].queryset = Materials.objects.all()

        
        if 'department' in self.data:
            try:
                department_id = int(self.data['department'])
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


