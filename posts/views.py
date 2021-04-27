from django.shortcuts import get_object_or_404
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.edit import FormView

from .forms import ContactForm
from .models import Category, Entry


class ArchiveView(ArchiveIndexView):
    model = Entry
    date_field = "date"
    paginate_by = 20


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
