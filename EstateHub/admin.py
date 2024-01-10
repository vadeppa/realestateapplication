# from django.contrib import admin
# from .models import CustomUser, PropertyUnit, Tenant, Lease

# class PropertyUnitAdmin(admin.ModelAdmin):
#     list_display = ('property_name', 'property_address', 'property_location', 'rent_cost', 'bedroom_type')
#     list_filter = ('bedroom_type')

# class TenantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'address', 'document_proofs')
#     list_filter = ('document_proofs')

# class LeaseAdmin(admin.ModelAdmin):
#     list_display = ('tenant_id', 'property_unit', 'agreement_end_date', 'monthly_rent_date')

# # Register your models with the custom admin classes
# admin.site.register(CustomUser)
# admin.site.register(PropertyUnit, PropertyUnitAdmin)
# admin.site.register(Tenant, TenantAdmin)
# admin.site.register(Lease, LeaseAdmin)
