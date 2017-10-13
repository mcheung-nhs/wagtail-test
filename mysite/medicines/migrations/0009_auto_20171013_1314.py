# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 13:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0008_auto_20171012_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinespagesection',
            name='section',
            field=wagtail.wagtailcore.fields.StreamField((('title', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')),))), ('content', wagtail.wagtailcore.blocks.StructBlock((('content', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')),))), ('callout_alert', wagtail.wagtailcore.blocks.StructBlock((('content_', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')),))), ('callout_information', wagtail.wagtailcore.blocks.StructBlock((('content_', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')),))), ('callout_emergency', wagtail.wagtailcore.blocks.StructBlock((('content_', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')),)))), blank=True, null=True),
        ),
    ]
