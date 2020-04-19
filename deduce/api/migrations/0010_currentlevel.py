# Generated by Django 3.0.4 on 2020-04-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200418_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='current_level', to='api.Level')),
            ],
        ),
    ]
