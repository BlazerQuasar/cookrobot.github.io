from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    """ AuthMiddleware """

    def process_request(self, request):
        # 0. 排除那些不需要登录就能访问的页面
        # request.path_info 获取当前用户请求URL /login/
        if request.path_info in ["/login/", "/register/", "/image/code/"]:
            return
        # 1. 读取当前访问记用户的session信息，如果能读得到，说明已经登录过，就可以继续向后走
        info_dict = request.session.get("info")
        # print(info_dict)
        if info_dict:
            return
        # 2. 没有登录过,重新回到登录页面
        return redirect('/login/')

        # 如果方法中没有返回值（返回none）
        # 如果有返回值，HttpResponse, render, redirect.
        # print("AuthMiddleware.process_request")
        # return HttpResponse("无权访问")

    # def process_response(self, request, response):
    #     print("M1.process_response")
    #     return response
