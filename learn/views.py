# coding:utf-8
from django.http import HttpResponse


def index(request):
	return HttpResponse(u"您好，这个是django项目")
