# Generated by Django 4.0.2 on 2022-11-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
        ('Books', '0001_initial'),
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorlist',
            name='idbook',
            field=models.ForeignKey(db_column='idbook', on_delete=django.db.models.deletion.CASCADE, related_name='idbookdb', to='Books.book'),
        ),
        migrations.AlterField(
            model_name='authorlist',
            name='iduser',
            field=models.ForeignKey(db_column='iduser', on_delete=django.db.models.deletion.CASCADE, related_name='iduserdb', to='Users.user'),
        ),
    ]
