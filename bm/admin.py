# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from bm.models import *


# Register your models here.
admin.site.register(Bank),
admin.site.register(Account),
admin.site.register(Transaction),
admin.site.register(UserPermission)
