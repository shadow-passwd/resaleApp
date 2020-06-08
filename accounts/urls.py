from django.urls import path
from . views import register
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('register/' , register , name='register') , 
    
    # path('password_change/' , auth_views.PasswordChangeView.as_view(template_name='password_change_form.html') , name='password_change') , 
    # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html') , name='password_change_done') , 
    # path('password_reset/' , auth_views.PasswordResetView.as_view(template_name='password_reset_form.html') , name='password_reset') , 
    # path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html') , name='password_reset_done') , 


# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

]