from django.contrib import admin
from .models import Puppy, PuppyImage, AdoptionRequest, Contact
#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
# Customizing the Admin site
admin.site.site_header = "Small Size Puppies Admin"  # Custom header text
admin.site.site_title = "Small Size Puppies Admin Dashboard"  # Title displayed in the browser's title bar
admin.site.index_title = "Welcome to the Puppy Adoption Admin Panel"  # Index page title

class PuppyImageInline(admin.TabularInline):
    model = PuppyImage
    extra = 1

@admin.register(Puppy)
class PuppyAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'price', 'is_adopted')
    list_filter = ('is_adopted', 'breed')
    inlines = [PuppyImageInline]
    
@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'puppy', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'puppy__name')
    list_filter = ('submitted_at',)

# Registering the Contact model
admin.site.register(Contact)
