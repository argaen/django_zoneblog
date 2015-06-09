class TaggedObjectMixinView(object):

    def get_queryset(self):
        queryset = super(TaggedObjectMixinView, self).get_queryset()
        if "tag" in self.kwargs:
            queryset = queryset.filter(tags__name__in=[self.kwargs["tag"]])

        return queryset


class DateObjectMixinView(object):
    def get_queryset(self):
        queryset = super(DateObjectMixinView, self).get_queryset()
        if "year" in self.kwargs and "month" in self.kwargs:
            queryset = queryset.filter(published_on__year=self.kwargs["year"], published_on__month=self.kwargs["month"])

        return queryset


class DraftObjectMixinView(object):
    def get_queryset(self):
        queryset = super(DraftObjectMixinView, self).get_queryset()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(is_published=True)

        return queryset
