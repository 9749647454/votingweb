# Generated by Django 5.0.3 on 2024-04-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlwebsite', '0003_candidate_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
    ]
