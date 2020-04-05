from django.contrib import admin
from comments.models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	list_display = ('content_type', 'content_object', 'user', 'timestamp')
	list_filter = ['timestamp']

	class Meta:
		model = Comment

	def get_queryset(self, request):
		queryset = super(CommentAdmin, self).get_queryset(request)
		queryset = queryset.order_by('-timestamp')
		return queryset

# Register your models here.
admin.site.register(Comment, CommentAdmin)