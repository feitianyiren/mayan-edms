from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Workflow, State, Transition, WorkflowState


class WorkflowSetupForm(forms.ModelForm):
    class Meta:
        model = Workflow


class StateSetupForm(forms.ModelForm):
    class Meta:
        model = State


class WorkflowStateSetupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        workflow = kwargs.pop('workflow')
        super(WorkflowStateSetupForm, self).__init__(*args, **kwargs)
        self.fields['workflow'].initial = workflow
        self.fields['workflow'].widget = forms.widgets.HiddenInput()
    
    class Meta:
        model = WorkflowState


class TransitionSetupForm(forms.ModelForm):
    class Meta:
        model = Transition
