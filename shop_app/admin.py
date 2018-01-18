from django.contrib import admin

from .models import Goods_Variation, Good, Order, Category, Cart


class Admin_Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]


class Admin_Good(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ['name', 'category',]


class Admin_Goods_Variation(admin.ModelAdmin):
    list_display = ('__str__', 'parent', 'variation_name', 'cost',)
    search_fields = ['variation_name', 'get_parent_name', 'cost',]

    def get_parent_name(self, obj):
        return obj.parent.name


class Admin_Cart(admin.ModelAdmin):
    list_display = ('customer_name', 'good_count',)
    search_fields = ['customer',]

    def customer_id(self,obj):
        return obj.customer.username

    def good_count(self, obj):
        return obj.goods.count()

    good_count.short_description = "Count of goods"


class Admin_Order(admin.ModelAdmin):
    list_display = ()

admin.site.register(Category, Admin_Category)
admin.site.register(Good, Admin_Good)
admin.site.register(Goods_Variation, Admin_Goods_Variation)
admin.site.register(Cart, Admin_Cart)
admin.site.register(Order)