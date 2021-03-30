# Generated by Django 3.1.6 on 2021-03-30 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('model_answer_key', models.FileField(upload_to='modelAns/')),
                ('response_sheet', models.FileField(upload_to='studentAns/')),
                ('no_of_ans', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('passing_marks', models.IntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]