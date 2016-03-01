from django import forms

from feature_request.request.models import FeatureRequest


class FeatureRequestForm(forms.ModelForm):

    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority',
                  'product_area', 'target_date', 'ticket_url']

    def save(self, commit=True):
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate." % (
                    self.instance._meta.object_name,
                    'created' if self.instance._state.adding else 'changed',
                )
            )
        if commit:
            # All other instance fields are set elsewhere. Make sure
            # client_priority is set to None initially so that it will be
            # updated when we call self.instance.to()
            self.instance.client_priority = None
            self.instance.save()

            # Set this feature request's client_priority field and moves all
            # other feature requests (if necessary)
            self.instance.to(self.cleaned_data['client_priority'])

        return self.instance
