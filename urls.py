router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories', views.categories, name='categories'),
    path('posts/<int:category_id>', views.posts, name='posts'),
    path('article/<int:post_id>', views.article, name='article'),
    path('comments', views.comments, name='comments'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    #path('', views.login, name='login'),
    path('portfolio', portfolioviews.get_portfolio, name='portfolio')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)