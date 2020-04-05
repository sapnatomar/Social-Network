from django.contrib import admin
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('user', 'created', 'post')
	list_filter = ['updated', 'created']
	search_fields = ['user__username', 'post']

	class Meta:
		model = Post

	def get_queryset(self, request):
		queryset = super(PostAdmin, self).get_queryset(request)
		queryset = queryset.order_by('-created')
		return queryset

# Register your models here.
admin.site.register(Post, PostAdmin)
