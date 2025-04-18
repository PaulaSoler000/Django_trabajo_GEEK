# Generated by Django 5.1.7 on 2025-03-26 18:44

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0003_remove_inventario_foto'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='tags',
        ),
        migrations.AlterField(
            model_name='inventario',
            name='tipo_objeto',
            field=models.CharField(choices=[('libro', 'Libro'), ('manga', 'Manga'), ('comic', 'Cómic'), ('figura', 'Figura'), ('consola', 'Consola'), ('otro', 'Otro')], default='libro', max_length=12),
        ),
        migrations.AddField(
            model_name='inventario',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
