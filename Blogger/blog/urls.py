from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('myprofile/', views.my_profile, name = "my_profile"),
    path('create-blog/', views.create_blog, name="create blog"),
    path('delete-blog/<id>', views.delete_blog, name="delete blog"),
    path('all-detailed-blog/<id>', views.all_detailed_blog, name="all detailed blog"),
    path('my-detailed-blog/<id>', views.my_detailed_blog, name="my detailed blog"),
    path('update-blog/<id>', views.update_blog, name="Update Blog"),
    path('other-blogger/<id>/<blog_id>',views.other_blogger, name="Other_Blog" )
]