from django.contrib import admin
from django.urls import path
from app01.views import admin, account, main, subpage1, lun, Ingre, home, category, favorite
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # Main page
    path('main/', main.home),

    path('meun/main/add/', main.main_menu_add),

    # home pages
    path('meun/<int:nid>/det/', home.meun_list),
    # path('meun/det1/', home.meun_list_cal),


    # Second menu

    path('meun/add/', main.add_meun),
    path('meun/<int:nid>/edit/', main.edit_meun),


    # my favorite

    path('meun/<int:nid>/list/', favorite.fav_meun),
    path('meun/<int:nid>/list2/', favorite.fav_cook),

    path('meun/list/', favorite.fav_list),
    path('meun/<int:nid>/delete/', favorite.fav_dele),


    # Subpage1
    path('subpage1/', subpage1.page),
    path('subpage2/', subpage1.page2),
    path('subpage3/', subpage1.page3),
    path('subpage4/', subpage1.page4),
    path('subpage5/', subpage1.page5),
    path('subpage6/', subpage1.page6),
    path('subpage7/', subpage1.page7),
    path('subpage8/', subpage1.page8),
    path('subpage9/', subpage1.page9),
    path('subpage10/', subpage1.page10),
    path('subpage11/', subpage1.page11),
    path('subpage12/', subpage1.page12),
    path('subpage13/', subpage1.page13),
    path('subpage14/', subpage1.page14),


    # Ingredient
    path('Ingredientm/', Ingre.meat),
    path('Ingredientm/add/', Ingre.madd),
    path('Ingredientv/', Ingre.veg),
    path('Ingredientv/add/', Ingre.vadd),
    path('Ingredienta/', Ingre.aux),
    path('Ingredienta/add/', Ingre.aadd),


    # Category
    path('category/list/', category.page),

    # lun bo figure
    path('det_lun1/', lun.page1),
    path('det_lun2/', lun.page2),
    path('det_lun3/', lun.page3),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # register
    path('register/', account.regist),

    # personal profile
    path('person/list', account.person)

]
