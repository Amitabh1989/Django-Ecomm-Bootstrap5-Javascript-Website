from django.contrib import admin
from shop.models import Product, Order

# Register your models here.

admin.site.site_header = "Nebula Ecom Site"
admin.site.site_title = "Nebula Mart"
admin.site.index_title = "Manage Nebula Mart"

# To display the field we want to see in admin panel
class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = "Default category"
    list_display = ('title', 'category', 'price', 'discounted_price',)
    search_fields = ('title', 'category', 'price', 'description',)
    actions = ('change_category_to_default',)
    fields = ('title', 'category', 'price', 'description',)  # Can only edit these fields
    list_editable = ('category', 'price', 'discounted_price',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)