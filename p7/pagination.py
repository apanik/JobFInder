from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination, PageLink, _get_displayed_page_numbers, _get_page_links
from rest_framework.response import Response
from rest_framework.utils.urls import remove_query_param, replace_query_param


class P7Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_next_link(self):
        if not self.page.has_next():
            return None
        url = self.request.get_full_path()

        page_number = self.page.next_page_number()
        return replace_query_param(url, self.page_query_param, page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        url = self.request.get_full_path()
        page_number = self.page.previous_page_number()
        if page_number == 1:
            return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)

    def get_html_context(self):
        base_url = self.request.get_full_path()
        def page_number_to_url(page_number):
            if page_number == 1:
                return remove_query_param(base_url, self.page_query_param)
            else:
                return replace_query_param(base_url, self.page_query_param, page_number)

        current = self.page.number
        final = self.page.paginator.num_pages
        page_numbers = _get_displayed_page_numbers(current, final)
        page_links = _get_page_links(page_numbers, current, page_number_to_url)
        return {
            'previous_url': self.get_previous_link(),
            'next_url': self.get_next_link(),
            'page_links': page_links
        }


    def get_paginated_response(self, data, **kwargs):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('start_index', self.page.start_index()),
            ('end_index', self.page.end_index()),
            ('page_number', self.page.number),
            ('page_size', self.page_size),
            ('page_count', self.page.paginator.num_pages),
            ('page_data_count', len(data)),
            ('pages', self.get_html_context()),
            ('results', data)
        ]))


