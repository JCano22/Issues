# Generated by Django 4.2.2 on 2023-06-09 00:33

from django.db import migrations


def populate_role(apps, schemaeditor):
    entries = {
        "developer": "Team members who build the software",
        "scrum master":  "The software development team's coach",
        "product owner": "The person who has ownership over what the team develops"
    }
    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role = Role(name=key, description=value)
        role.save()


def populate_team(apps, schemaeditor):
    entries = {
        "alpha": "The A team",
        "bravo": "The B team",
        "charlie": "The C team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team = Team(name=key, description=value)
        team.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team)
    ]
