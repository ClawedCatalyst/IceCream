# Generated by Django 3.2.4 on 2023-04-17 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_remove_registration_behance_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.year'),
        ),
    ]