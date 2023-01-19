#admin,py
class PostAdmin(admin.ModelAdmin):
    list_display  = ('id','title','publish_date')
    search_fields = ['title','content']
    date_hierarchy = 'publish_date'

________________________________________________-
static _ media :

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static/')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')