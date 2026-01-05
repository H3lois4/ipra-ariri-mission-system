import csv
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from team.models import TeamMember, MedicalInfo

User = get_user_model()


class Command(BaseCommand):
    help = 'Importa dados da equipe a partir de um arquivo CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                email = row['Email'].strip().lower()
                name = row['Nome completo'].strip()

                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={'name': name}
                )

                if created:
                    user.set_password(User.objects.make_random_password())
                    user.save()

                team_member, _ = TeamMember.objects.get_or_create(user=user)

                # Dados pessoais
                team_member.full_name = name
                team_member.phone = row.get('Telefone', '')
                team_member.rg = row.get('RG', '')
                team_member.cpf = row.get('CPF', '')
                team_member.profession = row.get('Profissão', '')
                team_member.city = row.get('Cidade', '')
                team_member.state = row.get('Estado', '')
                team_member.save()

                # Dados médicos
                medical_info, _ = MedicalInfo.objects.get_or_create(team_member=team_member)

                medical_info.blood_type = row.get('Tipo sanguíneo', '')
                medical_info.allergies = row.get('Alergias', '')
                medical_info.medications = row.get('Medicamentos', '')
                medical_info.medical_conditions = row.get('Condições médicas', '')
                medical_info.emergency_contact_name = row.get('Contato de emergência', '')
                medical_info.emergency_contact_phone = row.get('Telefone emergência', '')
                medical_info.save()

                self.stdout.write(self.style.SUCCESS(
                    f'Importado: {name} ({email})'
                ))
