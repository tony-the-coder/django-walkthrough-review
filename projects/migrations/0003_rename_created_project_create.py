# Generated by Django 5.1.5 on 2025-02-05 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='created',
            new_name='create',
        ),
    ]
