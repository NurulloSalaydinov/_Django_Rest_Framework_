from rest_framework.pagination import PageNumberPagination  

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'limit'
