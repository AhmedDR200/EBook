from rest_framework.pagination import PageNumberPagination


class SmallSet(PageNumberPagination):
    """
    10 items per page, 5 pages max
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50