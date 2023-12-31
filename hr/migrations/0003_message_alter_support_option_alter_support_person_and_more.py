# Generated by Django 4.2.4 on 2023-10-18 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('situation', models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='support',
            name='option',
            field=models.CharField(choices=[('I lost my account', 'I lost my account'), ('Update resume', 'Update resume'), ('Others', 'Others'), ('My password does not world', 'My password does not world')], max_length=50),
        ),
        migrations.AlterField(
            model_name='support',
            name='person',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Candidate', 'Candidate')], max_length=50),
        ),
        migrations.AlterField(
            model_name='support',
            name='situation',
            field=models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True),
        ),
    ]
