from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView
)
from accounts.models import Role, Team
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issue, Priority, Status
from django.utils import timezone


class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'issues/new.html'
    model = Issue
    fields = ['summary', 'body', 'assignee', 'status', 'priority']

    def test_func(self):
        po_role = Role.objects.get(name="product owner")
        return self.request.user.role == po_role

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)


class IssueDetailView(LoginRequiredMixin, DetailView):
    template_name = 'issues/detail.html'
    model = Issue


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'issues/edit.html'
    model = Issue
    fields = ['summary', 'body', 'assignee', 'status', 'priority']

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user

    def form_valid(self, form):
        form.instance.updated_on = timezone.now()
        return super().form_valid(form)


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy('list')

    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_list'] = Issue.objects.order_by('priority').reverse()

        return context
