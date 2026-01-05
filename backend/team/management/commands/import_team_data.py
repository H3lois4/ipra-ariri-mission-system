import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from team.models import TeamMember, MedicalInfo

User = get_user_model()


def map_gender(value):
    if not value:
        return 'N'
    value = value.lower()
    if 'fem' in value:
        return 'F'
    if 'masc' in value:
        return 'M'
    return 'N'


class Command(BaseCommand):
    help = 'Importa dados da equipe a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                email = row['Email'].strip().lower()
                name = row['Nome Completo'].strip()

                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={'name': name}
                )

                if created:
                    user.set_unusable_password()
                    user.save()

                team_member, _ = TeamMember.objects.get_or_create(user=user)

                team_member.full_name = name
                team_member.phone = row.get('Telefone ', '')
                team_member.rg = row.get('RG', '')
                team_member.cpf = row.get('CPF', '')
                team_member.profession = row.get('Profissão', '')
                team_member.gender = map_gender(row.get('Sexo', ''))

                birth_date = row.get('Data de Nascimento', '').strip()
                if birth_date:
                    try:
                        team_member.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
                    except ValueError:
                        team_member.birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()


                # Endereço completo (temporário em street)
                team_member.street = row.get('Endereço completo', '')
                team_member.save()

                medical_info, _ = MedicalInfo.objects.get_or_create(
                    team_member=team_member
                )
                medical_info.medical_conditions = row.get('Dados médicos', '')

                medical_info.save()

                self.stdout.write(
                    self.style.SUCCESS(f'Importado: {name} ({email})')
                )
