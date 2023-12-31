# Generated by Django 4.1.5 on 2023-01-28 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuretatCivile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_betat', models.CharField(max_length=200, verbose_name="Bureau d'etat Civil")),
            ],
            options={
                'ordering': ['libelle_betat'],
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomC', models.CharField(max_length=50, verbose_name='Commune de Naissance')),
                ('CodePostalC', models.CharField(max_length=5, verbose_name='Code Postal')),
            ],
            options={
                'ordering': ['NomC'],
            },
        ),
        migrations.CreateModel(
            name='Femme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom la Femme')),
                ('prenoms', models.CharField(max_length=30, verbose_name='Prenoms de la Femme')),
                ('date_naiss', models.DateField(verbose_name='Date de Naissance')),
            ],
            options={
                'verbose_name': 'Femme',
                'verbose_name_plural': 'Femme',
            },
        ),
        migrations.CreateModel(
            name='Homme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, verbose_name='Nom l homme')),
                ('prenoms', models.CharField(max_length=30, verbose_name='Prenoms de homme')),
                ('date_naiss', models.DateField(verbose_name='Date de Naissance')),
            ],
            options={
                'verbose_name': 'Homme',
                'verbose_name_plural': 'Homme',
            },
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomW', models.CharField(max_length=50, verbose_name='Wilaya ')),
                ('CodePostalW', models.CharField(max_length=5, verbose_name='Code Postal')),
            ],
            options={
                'ordering': ['NomW'],
            },
        ),
        migrations.CreateModel(
            name='Persone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, verbose_name='Nom')),
                ('prenoms', models.CharField(max_length=250, verbose_name='Prenoms')),
                ('sexe', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=150, verbose_name='sexe')),
                ('date_naiss', models.DateField(verbose_name='Date de Naissance')),
                ('heure_naiss', models.TimeField(verbose_name='Heure de Naissance')),
                ('BuretatCivile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.buretatcivile', verbose_name='Bureau d etat Civil')),
                ('lieun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.commune', verbose_name='Lieu de Naissance')),
                ('mere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meres', to='app1.persone', verbose_name='Nom et Prénoms du Mere')),
                ('pere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peres', to='app1.persone', verbose_name='Nom et Prénoms du Pere')),
                ('pere_mere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meres_mere', to='app1.persone', verbose_name='Nom et Prénoms du Pere du Mere')),
                ('pere_pere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peres_pere', to='app1.persone', verbose_name='Nom et Prénoms du Pere du Pere')),
            ],
            options={
                'verbose_name': 'Acte de naissance',
                'verbose_name_plural': 'Personne',
                'ordering': ['nom', 'prenoms'],
            },
        ),
        migrations.CreateModel(
            name='Mariage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_marie', models.CharField(max_length=50, verbose_name='Profession du Marie(e)')),
                ('domicile', models.CharField(max_length=50, verbose_name='Lieu de Domicile du Marie(e)')),
                ('profession_mariee', models.CharField(max_length=50, verbose_name='Profession du CONJOINT(E)')),
                ('date_mariage', models.DateField(verbose_name='Date du Mariage')),
                ('heure_mariage', models.TimeField(verbose_name='Heure du Mariage')),
                ('lieu_mariage', models.CharField(max_length=50, verbose_name='Lieu de Celebartion du Mariage')),
                ('BuretatCivile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.buretatcivile', verbose_name='Bureau d etat Civil')),
                ('marie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marie', to='app1.homme', verbose_name='Nom et Prenoms du Marie(e)')),
                ('mariee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conjoint', to='app1.femme', verbose_name='Nom et Prenoms du CONJOINT(E)')),
                ('temoine1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temoin1', to='app1.homme', verbose_name='Nom et Prenoms du Temoin 1')),
                ('temoine2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temoin2', to='app1.homme', verbose_name='Nom et Prenoms du Temoin 2')),
            ],
            options={
                'verbose_name': 'Acte de Mariage',
                'verbose_name_plural': 'Actes de Mariage',
            },
        ),
        migrations.CreateModel(
            name='Deces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_deces', models.DateField(verbose_name='Date du Deces')),
                ('heure_deces', models.TimeField(verbose_name='Heure du Deces')),
                ('lieu_deces', models.CharField(max_length=500, verbose_name='Lieu du Deces')),
                ('cause_deces', models.CharField(max_length=500, verbose_name='Cause du Deces')),
                ('annonceur', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='annonceur', to='app1.persone', verbose_name='Nom et Prenoms d')),
                ('personedeces', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='deces', to='app1.persone', verbose_name='Nom et Prenoms du Decede')),
            ],
            options={
                'verbose_name': 'Acte de Deces',
                'verbose_name_plural': 'Actes de Deces',
            },
        ),
        migrations.CreateModel(
            name='Daira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomD', models.CharField(max_length=50, verbose_name='Daira de Naissance')),
                ('CodePostalD', models.CharField(max_length=5, verbose_name='Code Postal')),
                ('Wilaya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.wilaya', verbose_name='Wilaya')),
            ],
            options={
                'ordering': ['NomD'],
            },
        ),
        migrations.AddField(
            model_name='commune',
            name='Daira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.daira', verbose_name='Daira'),
        ),
        migrations.AddField(
            model_name='buretatcivile',
            name='Commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.commune', verbose_name='Commune'),
        ),
    ]
