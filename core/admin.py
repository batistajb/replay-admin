from django.contrib import admin
from .models import Client, Quatrain, Partner, Media, PlanPartner

admin.site.register(Client)
admin.site.register(Quatrain)
admin.site.register(Partner)
admin.site.register(Media)
admin.site.register(PlanPartner)
