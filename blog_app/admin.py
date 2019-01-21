from django.contrib import admin
from .models import author
from .models import category
from .models import Post

# Register your models here.
admin.site.register(author)
admin.site.register(category)
admin.site.register(Post)
