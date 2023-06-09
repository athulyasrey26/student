# Generated by Django 4.1.7 on 2023-03-25 09:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_rename_department_application_departname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='departname',
            new_name='department',
        ),
        migrations.RemoveField(
            model_name='application',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='application',
            name='departname',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course',
        ),
        migrations.RemoveField(
            model_name='department',
            name='departname',
        ),
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='studentapp.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='studentapp.course'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='application',
            name='purpose',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='studentapp.purpose'),
            preserve_default=False,
        ),
    ]
