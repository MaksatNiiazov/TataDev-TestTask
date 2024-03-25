from django.contrib import admin
from .models import Restaurant, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    fields = ('user', 'rating', 'comment', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'description', 'latitude', 'longitude')
    search_fields = ('name', 'address')
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'rating', 'created_at')
    list_filter = ('created_at', 'rating')
    search_fields = ('comment', 'restaurant__name', 'user__username')
    readonly_fields = ('created_at',)
