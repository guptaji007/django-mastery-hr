# Generated by Django 4.2.4 on 2023-10-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_message_situation_alter_support_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='situation',
            field=models.CharField(choices=[('Unread', 'Unread'), ('Read', 'Read')], default='Unread', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='option',
            field=models.CharField(choices=[('My password does not world', 'My password does not world'), ('Others', 'Others'), ('I lost my account', 'I lost my account'), ('Update resume', 'Update resume')], max_length=50),
        ),
        migrations.AlterField(
            model_name='support',
            name='situation',
            field=models.CharField(choices=[('Done', 'Done'), ('Pending', 'Pending')], default='Pending', max_length=50, null=True),
        ),
    ]
