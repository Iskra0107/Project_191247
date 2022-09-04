from django.contrib import admin
from .models import Glucose
# Register your models here.

# class MyUserAdmin(admin.ModelAdmin):

# 	def has_change_permission(self, request, obj=None):
# 		return False

# 	def has_delete_permission(self,request,obj=None):
# 		return False
# admin.site.register(MyUser, MyUserAdmin)



# class GlucoseUserAdmin(admin.StackedInline):
# 	model = GlucoseUser
# 	extra = 0


# class GlucoseAdmin(admin.ModelAdmin):
# 	inlines = [GlucoseUserAdmin,]
# admin.site.register(Glucose, GlucoseAdmin)


class GlucoseAdmin(admin.ModelAdmin):
	pass 
admin.site.register(Glucose, GlucoseAdmin)
