from .models import Problem, Answer, ProblemTest
from django.forms import ModelForm, NumberInput


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = ['answer']

        widgets = {
            'answer': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ответ'
            })
        }


