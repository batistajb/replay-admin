from django.contrib import admin
from .models import Client, Quatrain, Partner, Media, Address

class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register(Client)
admin.site.register(Quatrain)
admin.site.register(Partner)
admin.site.register(Media)
admin.site.register(Address, HiddenModelAdmin)
