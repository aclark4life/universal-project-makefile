# Generated by Django 5.1.1 on 2024-09-19 00:48

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Home Page'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='marketing_blocks',
            field=wagtail.fields.StreamField([('marketing_block', 8)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the block title', 'required': False}), 1: ('wagtail.blocks.RichTextBlock', (), {'help_text': 'Enter the block content', 'required': False}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': False}), 3: ('wagtail.blocks.ListBlock', (2,), {'help_text': 'Select one or two images for column display. Select three or more images for carousel display.'}), 4: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Select one image for background display.', 'required': False}), 5: ('wagtail.blocks.CharBlock', (), {'default': 'vh-100 bg-secondary', 'form_classname': 'full title', 'help_text': 'Enter a CSS class for styling the marketing block', 'required': False}), 6: ('wagtail.blocks.CharBlock', (), {'default': 'img-thumbnail p-5', 'form_classname': 'full title', 'help_text': 'Enter a CSS class for styling the column display image(s)', 'required': False}), 7: ('wagtail.blocks.CharBlock', (), {'default': 'd-flex flex-row', 'form_classname': 'full title', 'help_text': 'Enter a CSS class for styling the layout.', 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('title', 0), ('content', 1), ('images', 3), ('image', 4), ('block_class', 5), ('image_class', 6), ('layout_class', 7)]], {})}, null=True),
        ),
    ]
