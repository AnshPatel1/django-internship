# Generated by Django 4.0.5 on 2022-10-02 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_course_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('P', 'Practical'), ('T', 'Theory')], max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.classroomtype')),
            ],
        ),
    ]
