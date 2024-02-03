from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, DateFromToRangeFilter

from advertisements.models import Advertisement


class FilterAdv(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateTimeFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at']

