from django.contrib import admin
from . models import Post

# class workAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model=Work


admin.site.register(Post)