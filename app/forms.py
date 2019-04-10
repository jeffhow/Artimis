from django import forms
from .models import LessonPlan, SafetyObjective, TechnicalObjective, EmployabilityObjective, ManagementObjective, TechnologyObjective

class LessonPlanForm(forms.ModelForm):
    safety_objectives = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=SafetyObjective.objects.all()
    )
    technical_objectives = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        queryset=TechnicalObjective.objects.all()
    )
    employability_objectives = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        queryset=EmployabilityObjective.objects.all()
    )
    management_objectives = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        queryset=ManagementObjective.objects.all()
    )
    technology_objectives = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, 
        queryset=TechnologyObjective.objects.all()
    )

    class Meta:
        model = LessonPlan
        fields= '__all__'