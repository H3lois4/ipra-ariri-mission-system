from django.contrib import admin
from .models import TeamMember, MedicalInfo, Document

admin.site.register(TeamMember)
admin.site.register(MedicalInfo)
admin.site.register(Document)
