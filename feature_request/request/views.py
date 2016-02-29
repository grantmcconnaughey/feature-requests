from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, \
    DetailView

from feature_request.request.forms import FeatureRequestForm
from feature_request.request.models import FeatureRequest


class FeatureRequestListView(ListView):

    model = FeatureRequest
    context_object_name = 'feature_requests'
    template_name = 'request/list.html'
    paginate_by = 10


class FeatureRequestDetailView(DetailView):

    model = FeatureRequest
    template_name = 'request/detail.html'
    context_object_name = 'feature_request'


class FeatureRequestCreateView(CreateView):

    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'request/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Your feature request was created.')
        return super(FeatureRequestCreateView, self).form_valid(form)


class FeatureRequestUpdateView(UpdateView):

    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'request/update.html'
    context_object_name = 'feature_request'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Your feature request was updated.')
        return super(FeatureRequestUpdateView, self).form_valid(form)


class FeatureRequestDeleteView(DeleteView):

    model = FeatureRequest
    template_name = 'request/delete.html'
    context_object_name = 'feature_request'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your feature request was deleted.')
        return super(FeatureRequestDeleteView, self).delete(
            request, *args, **kwargs)
