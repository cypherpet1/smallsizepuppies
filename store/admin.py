from django.contrib import admin
from .models import Puppy, PuppyImage, AdoptionRequest, Contact, CustomerReview
from django.utils.html import format_html

class PuppyImageInline(admin.TabularInline):
    model = PuppyImage
    extra = 1

@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'price', 'age', 'gender', 'is_adopted', 'created_at')
    search_fields = ('name', 'breed')
    list_filter = ('breed', 'gender', 'is_adopted')
    inlines = [PuppyImageInline]

@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'puppy', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview', 'star_rating', 'created_at')
    readonly_fields = ('photo_preview',)
    search_fields = ('name', 'review')
    list_filter = ('rating', 'created_at')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;">', obj.photo.url)
        return "-"
    photo_preview.short_description = 'Photo'

    def star_rating(self, obj):
        return format_html('★' * obj.rating + '☆' * (5 - obj.rating))
    star_rating.short_description = 'Rating'
