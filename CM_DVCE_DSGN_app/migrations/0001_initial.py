# Generated by Django 3.1 on 2020-10-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmDvceDsgn',
            fields=[
                ('dsgn_cde', models.IntegerField(db_column='Dsgn_cde', primary_key=True, serialize=False)),
                ('dsgn_exp_date', models.DateField()),
                ('design_desc', models.TextField()),
                ('material_type', models.TextField()),
            ],
            options={
                'db_table': 'CM_DVCE_DSGN',
                'managed': False,
            },
        ),
    ]
