# Generated by Django 5.2.1 on 2025-05-25 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('priority', models.CharField(max_length=20, verbose_name='Priority')),
                ('preconditions', models.TextField(verbose_name='Preconditions')),
                ('input_data', models.TextField(verbose_name='Input Data')),
                ('steps', models.TextField(verbose_name='Steps')),
                ('expected_result', models.TextField(verbose_name='Expected Result')),
                ('actual_result', models.TextField(verbose_name='Actual Result')),
                ('test_status', models.CharField(max_length=20, verbose_name='Test Status')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now_add=True, verbose_name='Updated At')),
                ('id_us', models.IntegerField(verbose_name='User Storie')),
            ],
            options={
                'verbose_name': 'Test Case',
                'verbose_name_plural': 'Test Cases',
                'ordering': ['-created_at'],
            },
        ),
    ]
