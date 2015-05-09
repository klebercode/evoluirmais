from django.contrib import admin

from evoluirmais.subscriptions.models import Subscription


# class SubscriptionAdmin(admin.ModelAdmin):
#     list_display = ('email', 'type')
#     list_filter = ['created_at']
#     date_hierarchy = 'created_at'
#     search_fields = ('email',)


admin.site.register(Subscription)
