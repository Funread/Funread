# Generated by Django 4.0.2 on 2024-10-19 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0003_alter_user_email_alter_user_password'),
        ('Badges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Badges.badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
