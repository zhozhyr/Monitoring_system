from django.contrib import admin
from .models import *

# Регистрируем модели в админке

admin.site.register(Info)
admin.site.register(UserRole)
admin.site.register(Administrator)
admin.site.register(UserSetting)
admin.site.register(UsersList)
admin.site.register(StructuralUnitTree)
admin.site.register(Position)
admin.site.register(Appointment)
admin.site.register(TypeOPO)
admin.site.register(OPO)
admin.site.register(HazardClass)
admin.site.register(Manufacturer)
admin.site.register(NameTU)
admin.site.register(KindTU)
admin.site.register(TypeTU)
admin.site.register(TU)
admin.site.register(Certificate)
admin.site.register(ControlNote)
admin.site.register(EPBJournal)
admin.site.register(InspectionJournal)
admin.site.register(Setup)
