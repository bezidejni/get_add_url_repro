from wagtail.admin.utils import set_query_params
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import (
    IndexView,
    SnippetViewSet,
)


from .models import Child, Parent

class PrefilledParentIndexView(IndexView):

    def get_add_url(self):
        add_url = super().get_add_url()
        if self.filters.data.get("parent"):
            add_url = set_query_params(
                add_url, {"parent": self.filters.data["parent"]}
            )
        return add_url


class ParentViewSet(SnippetViewSet):
    model = Parent

class ChildViewSet(SnippetViewSet):
    model = Child
    list_filter = ["parent"]
    index_view_class = PrefilledParentIndexView


register_snippet(ChildViewSet)
register_snippet(ParentViewSet)
