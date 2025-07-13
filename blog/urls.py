from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('myprofile/', views.my_profile, name = "my_profile"),
    path('contact/', views.contact_view, name='contact'),
    path('create-blog/', views.create_blog, name="create blog"),
    path('delete-blog/<id>', views.delete_blog, name="delete blog"),
    path('all-detailed-blog/<id>', views.all_detailed_blog, name="all detailed blog"),
    path('my-detailed-blog/<id>', views.my_detailed_blog, name="my detailed blog"),
    path('update-blog/<id>', views.update_blog, name="Update Blog"),
    path('upload-image/<int:blog_id>/', views.create_blog, name='upload_image'),
    path('other-blogger/<id>/<blog_id>',views.other_blogger, name="Other_Blog" )
    
]