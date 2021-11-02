# Django
from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Register the post model in the admin panel."""
    list_display = ('pk', 'title', 'photo', 'user')
    list_display_links = ('pk', 'user')
    list_editable = ('title',)

    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'title')
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'profile')),
        }),
        ('Post', {
            'fields': (
                ('title',),
                ('photo'),
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified')
