# Generated by Django 3.1.7 on 2021-04-08 12:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='CATEGORY')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreateDate')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('text', models.TextField(verbose_name='Content')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreateDate')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myblog.category', verbose_name='CATEGORY')),
            ],
        ),
    ]
