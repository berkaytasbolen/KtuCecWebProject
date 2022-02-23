# Generated by Django 4.0.2 on 2022-02-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_user_profilmodel_isim_profilmodel_hakkinda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitapmodel',
            name='icerik',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='kitapmodel',
            name='sayfa_sayisi',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profilmodel',
            name='hes_kod',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profilmodel',
            name='katki',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profilmodel',
            name='kayit_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='kitapmodel',
            name='durum',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
