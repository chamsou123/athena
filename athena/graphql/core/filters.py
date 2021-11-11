import django_filters


class EnumFilter(django_filters.CharFilter):
    def __init__(self, input_class, *args, **kwargs):
        assert kwargs.get(
            "method"
        ), "Providing exact filter method is required for EnumFilter"
        self.input_class = input_class
        super().__init__(*args, **kwargs)
