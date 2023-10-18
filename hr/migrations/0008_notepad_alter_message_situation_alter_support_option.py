# Generated by Django 4.2.4 on 2023-10-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_alter_message_situation_alter_support_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notepad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='situation',
            field=models.CharField(choices=[('Read', 'Read'), ('Unread', 'Unread')], default='Unread', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='option',
            field=models.CharField(choices=[('Update resume', 'Update resume'), ('My password does not world', 'My password does not world'), ('I lost my account', 'I lost my account'), ('Others', 'Others')], max_length=50),
        ),
    ]
