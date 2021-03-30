from django.db import models
from django.contrib.auth.models import User

class Tests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    model_answer_key = models.FileField(upload_to='modelAns/')
    response_sheet = models.FileField(upload_to='studentAns/')
    no_of_ans = models.IntegerField()
    total_marks = models.IntegerField()
    passing_marks = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
