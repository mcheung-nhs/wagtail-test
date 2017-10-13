from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey


# --- Start medicines index page ---

class MedicinesIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

# --- End medicines index page ---


# --- Start section blocks ---

class MedicinesPageSectionTitle(blocks.StructBlock):
    title = blocks.CharBlock(classname="full", icon="title")

    class Meta:
        template = 'blocks/title.html'
        icon = 'title'


class MedicinesPageSectionContent(blocks.StructBlock):
    content = blocks.CharBlock(classname="full", icon="title")

    class Meta:
        template = 'blocks/content.html'
        icon = 'doc-full'


class MedicinesPageSectionCalloutAlert(blocks.StructBlock):
#    content = blocks.CharBlock(classname="full", icon="title")
    content = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/callout-alert.html'
        icon = 'placeholder'


class MedicinesPageSectionCalloutInformation(blocks.StructBlock):
    content = blocks.CharBlock(classname="full", icon="title")

    class Meta:
        template = 'blocks/callout-information.html'
        icon = 'placeholder'


class MedicinesPageSectionCalloutEmergency(blocks.StructBlock):
    content = blocks.CharBlock(classname="full", icon="title")

    class Meta:
        template = 'blocks/callout-emergency.html'
        icon = 'warning'

# --- End section blocks ---


class MedicinesPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('sections', label="Sections"),
    ]


class MedicinesPageSection(Orderable):
    page = ParentalKey(MedicinesPage, related_name='sections')
    section = StreamField([
        ('title', MedicinesPageSectionTitle()),
        ('content', MedicinesPageSectionContent()),
        ('callout_alert', MedicinesPageSectionCalloutAlert()),
        ('callout_information', MedicinesPageSectionCalloutInformation()),
        ('callout_emergency', MedicinesPageSectionCalloutEmergency()),
    ], null=True, blank=True)

    panels = [
        StreamFieldPanel('section'),
    ]
