# Generated by Django 3.2.23 on 2023-11-29 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='lastconsultation',
            field=models.DateTimeField(blank=True, db_column='LastConsultation', null=True),
        ),
    ]
