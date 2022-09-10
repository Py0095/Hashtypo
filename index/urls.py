from django.urls import path
from . import views

urlpatterns = [
    path("www..pam-dekonekte/", views.dekonekte,name='url_dekonekte'),
    
    path("www.hashtypo.pam-Enskri/",views.inskri,name='url_inskri'),
    
    path("",views.akey,name='url_home'),
    
    path("www.hashtypo.pam-konekte/",views.konekte,name='url_konekte'),
    
    path("www.hashtypo.pam-continue/",views.continue1,name='url_continue1'),
    
    path("www.hashtypo.pam-encryptfile/",views.encryptfile,name='url_encryptfile'),
    
    path("www.hashtypo.pam-encryptfolder/",views.encryptfolder,name='url_encryptfolder'),
    
    path("www.hashtypo.pam-about/",views.about,name='url_about'),
   
    
    
    
    
    
    
    #path("https://www.blogsosyal.pam-atik-yo/",views.Atikyo,name='url_lis-atik'),
    
    #path("https://www.blogsosyal.pam-atikpaw/",views.ekriatikpaw,name='url_ekriAtik-paw'),
    
    #path("https://www.blogsosyal.pam-atikpawdjangoform/",views.ekriatikpawdjangoform,name='url_kreye-atik'),
    
    #path("https://www.blogsosyal.pam-<str:slug>/",views.Atiklekti,name='url_li-atik'),

]