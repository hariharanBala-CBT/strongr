# Generated by Django 5.0.3 on 2024-04-03 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0007_organizationlocationgametype_number_of_courts'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('days', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=10)),
                ('is_booked', models.BooleanField(default=False)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.court')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.organizationlocation')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('organization_booking', models.BooleanField(default=False)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('payment_status', models.CharField(choices=[('YET_TO_BEGIN', 'Yet to Begin'), ('INITIATED', 'Initiated'), ('IN_PROGRESS', 'In Progress'), ('SUCCESS', 'Success'), ('FAILED', 'Cancelled')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('tax_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('total_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.court')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('slot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.slot')),
            ],
        ),
    ]