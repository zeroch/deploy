# Generated by Django 2.2.6 on 2019-10-06 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0003_auto_20191006_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='kind',
            field=models.CharField(choices=[('N', 'New Patient'), ('F', 'Follow-up')], default='N', max_length=1),
        ),
    ]
