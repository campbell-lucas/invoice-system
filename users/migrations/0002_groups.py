
import os


from django.db import migrations


def create_groups(apps, scheme_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name=os.environ.get('DJ_GROUP_COLLECTORS'))
    Group.objects.create(name=os.environ.get('DJ_GROUP_SALESMANAGERS'))
    Group.objects.create(name=os.environ.get('DJ_GROUP_CUSTOMERS'))


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
