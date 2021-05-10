from django import forms
from django.utils import timezone

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question Text:', max_length=100)
    pub_date = forms.DateTimeField(label="Date:", initial=timezone.now())