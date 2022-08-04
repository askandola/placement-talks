# Generated by Django 4.0.6 on 2022-08-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('isAccepted', models.BooleanField(blank=True, default=None, null=True)),
                ('channelName', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
