from django.shortcuts import get_object_or_404
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Category, Entry

ON_EACH_SIDE = 3
ON_ENDS = 2
DOT = "."


def get_page_range(page_obj):
    paginator = page_obj.paginator
    page_num = page_obj.number - 1
    num_pages = paginator.num_pages

    # If there are 10 or fewer pages, display links to every page.
    # Otherwise, do some fancy
    if num_pages <= 10:
        page_range = range(num_pages)
    else:
        # Insert "smart" pagination links, so that there are always ON_ENDS
        # links at either end of the list of pages, and there are always
        # ON_EACH_SIDE links at either end of the "current page" link.
        page_range = []
        if page_num > (ON_EACH_SIDE + ON_ENDS):
            page_range += [
                *range(0, ON_ENDS),
                DOT,
                *range(page_num - ON_EACH_SIDE, page_num + 1),
            ]
        else:
            page_range.extend(range(0, page_num + 1))
        if page_num < (num_pages - ON_EACH_SIDE - ON_ENDS - 1):
            page_range += [
                *range(page_num + 1, page_num + ON_EACH_SIDE + 1),
                DOT,
                *range(num_pages - ON_ENDS, num_pages),
            ]
        else:
            page_range.extend(range(page_num + 1, num_pages))
    return [page + 1 if isinstance(page, int) else page for page in page_range]


class ArchiveView(ArchiveIndexView):
    model = Entry
    date_field = "date"
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().prefetch_related("category")

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result["page_range"] = get_page_range(result["page_obj"])
        return result


class CategoryView(ArchiveView):
    template_name = "posts/entry_category.html"

    def get(self, request, slug, **kwargs):
        self.kwargs["category"] = get_object_or_404(Category, slug=slug)
        return super().get(request, kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(category=self.kwargs["category"])

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result["category"] = self.kwargs["category"]
        return result


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/kontakt/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
