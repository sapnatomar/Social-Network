from django.contrib import admin

from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'description')
	search_fields = ['user__username']

	# def user_info(self, obj):
	# 	return obj.description

	def get_queryset(self, request):
		queryset = super(UserProfileAdmin, self).get_queryset(request)
		queryset = queryset.order_by('user')
		return queryset

# Register your models here.

admin.site.register(UserProfile, UserProfileAdmin)