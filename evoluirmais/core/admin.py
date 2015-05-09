from django.contrib import admin


from evoluirmais.core.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'type', 'created_at')
    list_filter = ['type']
    search_fields = ['email']


admin.site.register(Subscription, SubscriptionAdmin)
