from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='team/photos/', null=True, blank=True)

    rg = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, blank=True)


    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ('F', 'Feminino'),
            ('M', 'Masculino'),
        ],
    )

    profession = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class MedicalInfo(models.Model):
    team_member = models.OneToOneField(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='medical_info'
    )

    blood_type = models.CharField(max_length=3, blank=True)
    allergies = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    medical_conditions = models.TextField(blank=True)

    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return f'Dados médicos - {self.team_member.full_name}'


class Document(models.Model):
    team_member = models.ForeignKey(
        TeamMember,
        on_delete=models.CASCADE,
        related_name='documents'
    )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='team/documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
