from django.contrib import admin
from .models import Register    # from posts.models import Register  (posts--appname)
from .models import signUp

# Register your models here.

class RegisterModelAdmin(admin.ModelAdmin):
    list_display=('name','email','telephone','state','timestamp','updated') # list will display like this
    search_fields=['name']  #This is for searching purpose
    list_filter=['updated','timestamp'] # For filtering purpose like Today,anyday,like this way.
    ordering=['updated']
    class Meta:
        model=Register


    
    
admin.site.register(Register,RegisterModelAdmin)


class signUpModelAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','timestamp','updated')
    search_fields=['first_name','last_name'] # searching purpose
    list_filter=['updated','timestamp']  # For filtering purpose like Today,anyday,like this way.
    ordering=['updated']
    
    class Meta:
        model=signUp
        
admin.site.register(signUp,signUpModelAdmin)


from .models import Category
from .models import  Article
from .models import LikeArticle
from .models import LikeCategory
from .models import UserProfile



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'likes')
    
admin.site.register(Article, ArticleAdmin)    
    

class LikeArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')
    
admin.site.register(LikeArticle, LikeArticleAdmin)    

class LikeCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'category')
    
admin.site.register(LikeCategory, LikeCategoryAdmin)    

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'isOutsider', 'profession','dept','year')
    
admin.site.register(UserProfile, UserProfileAdmin)







