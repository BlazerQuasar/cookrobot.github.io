from django.shortcuts import render, redirect

from app01 import models
from app01.utils.pagination import Pagination
from django import forms
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrypt import md5


def admin_list(request):
    """ Admin list """


    # 搜索
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    # 根据搜索条件去数据库获取
    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成的页码
        "search_data": search_data,
    }

    return render(request, 'admin_list.html', context)


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']  # 只可以修改username


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True),
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        # 去数据库校验一下，当前密码，与数据库密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与当前的一样")

        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


def admin_add(request):
    """ 添加管理员 """
    title = "新建管理员"
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/admin/list")

    return render(request, 'change.html', {"form": form, "title": title})


def admin_edit(request, nid):
    """ 编辑管理员 """
    # 对象/None
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        # return render(request, 'error.html', {"msg": "数据不存在"})
        return redirect(('/admin/list/'))
    title = "编辑管理员"
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row_object)  # 默认值
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    else:
        return render(request, 'change.html', {"form": form, "title": title})


def admin_delete(request, nid):
    """ 删除管理员 """
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")


def admin_reset(request, nid):
    """ 重置密码 """
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect(('/admin/list/'))
    title = "重置密码 - {}".format(row_object.username)
    if request.method == 'GET':
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    else:
        return render(request, 'change.html', {"form": form, "title": title})
