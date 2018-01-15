import xadmin
from .models import TestApp, TestTable, TestKey

@xadmin.sites.register(TestApp)
class TestAppAdmin(object):
    list_display = ("name", "upfile")
    list_display_links = ("name",)
    list_per_page = 20
    search_fields = ["name"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True

@xadmin.sites.register(TestTable)
class TestTableAdmin(object):
    list_display = ("name",)
    list_display_links = ("name",)
    list_per_page = 20
    search_fields = ["name"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True

@xadmin.sites.register(TestKey)
class TestKeyAdmin(object):
    list_display = ("name", "test")
    list_display_links = ("name",)
    list_per_page = 20
    search_fields = ["name"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True
