# Generated by Django 4.2.7 on 2024-03-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('meta', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('thumbnail_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('thumbnail_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(default='uncategorized', max_length=255)),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]