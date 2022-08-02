from django.shortcuts import render, HttpResponse, redirect
from django import forms
from app01.models import Admin
from app01 import models
from app01.utils.bootstrap import BootStrapForm
from app01.utils.encrypt import md5
from app01.utils.code import check_code
from io import BytesIO
from app01.utils.bootstrap import BootStrapModelForm
from django.core.exceptions import ValidationError


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True),

        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("The password is different")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="Verification code",
        widget=forms.TextInput,
        required=True
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def regist(request):
    title = "Register your account"
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'regist.html', {"form": form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return redirect("/login/")

    return render(request, 'regist.html', {"form": form, "title": title})


def login(request):
    """ Login """

    form = LoginForm(data=request.POST)
    if form.is_valid():

        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "Verification code is wrong")
            return render(request, 'login.html', {"form": form})

        # admin_object = models.Admin.objects.filter(username=form.cleaned_data["username"], password=form.cleaned_data["password"]).first()
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "Username or password is wrong!")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}
        # session 可以保存7天， 7天之内不需要登录。7 天之后 session失效，要重新登录。
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/main/')

    return render(request, 'login.html', {"form": form})


def image_code(request):
    """ Generate vertification code """
    # 调用含pillow函数的文件,生成图片
    img, code_string = check_code()

    # print(code_string)
    # 写入到自己的cookie中，以便后续中获取验证码在进行校验
    request.session['image_code'] = code_string
    # 给Session设置一个60秒超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')
    stream.getvalue()

    return HttpResponse(stream.getvalue())


def logout(request):
    """ Logout """
    request.session.clear()

    return redirect('/login/')


def person(request):
    return render(request, 'personal.html')