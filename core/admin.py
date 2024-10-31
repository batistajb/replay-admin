from django.contrib import admin
from .models import Client, Quatrain, Partner, Media, PlanPartner, Address

admin.site.register(Client)
admin.site.register(Quatrain)
admin.site.register(Partner)
admin.site.register(Media)
admin.site.register(Address)
