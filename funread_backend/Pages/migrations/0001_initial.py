# Generated by Django 4.0.2 on 2023-10-17 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('pageid', models.AutoField(db_column='PageId', primary_key=True, serialize=False)),
                ('type', models.IntegerField(db_column='Type')),
                ('template', models.IntegerField(db_column='Template')),
                ('elementorder', models.IntegerField(db_column='ElementOrder')),
                ('bookid', models.ForeignKey(blank=True, db_column='BookId', null=True, on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
            ],
            options={
                'db_table': 'pages',
            },
        ),
    ]
