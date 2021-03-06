# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 13:40
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0005_remove_medicinespagesection_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinespagesection',
            name='section',
            field=wagtail.wagtailcore.fields.StreamField((('medicine_section', wagtail.wagtailcore.blocks.StructBlock((('section_title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('section_paragraph', wagtail.wagtailcore.blocks.TextBlock(classname='full', icon='placeholder'))))),), blank=True, null=True),
        ),
    ]
