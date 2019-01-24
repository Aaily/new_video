#!/usr/bin/env python
import os
import sys



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CNW2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
#
# from CNW2.urls import urlpatterns
# from django.urls.resolvers import  RegexURLPattern
#
# def get_all_urls(patterns, pre_fix, is_firt_time=False,result=[]):
#     if is_firt_time:
#         result.clear()
#
#     for item in patterns:
#         # print(item ,type(item))
#         part = item._regex.strip('^$')
#         if isinstance(item, RegexURLPattern):
#             result.append(pre_fix + part)
#         else:
#             pass
#             # .get_all_urls( item.urlconf_name, pre_fix + part)
#
#     return result
# get_all_urls(urlpatterns, pre_fix='/', is_firt_time=True)