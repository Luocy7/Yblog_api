from django.urls import reverse
from django.conf import settings

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def post_reverse(viewname, args=None, kwargs=None, **extra):
    url = reverse(viewname, args=args, kwargs=kwargs, **extra)
    if url:
        return '{0}{1}'.format(settings.YBLOG_DOMAIN, url)


class NormalResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page': self.page.number,
            'num_pages': self.page.paginator.num_pages,
            'page_size': self.page.paginator.per_page,
            'results': data
        })