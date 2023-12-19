# Generated by Django 4.2.7 on 2023-12-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_services', '0005_alter_customer_address_delete_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
