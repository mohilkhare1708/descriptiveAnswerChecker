from django import forms
from evaluate.models import Tests

class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Tests
        fields = ('test_name', 'total_marks', 'passing_marks', 'no_of_ans', 'model_answer_key', 'response_sheet', )