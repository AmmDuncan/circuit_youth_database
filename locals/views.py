from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  UpdateView)

from .models import Local, Executive, Member
from .forms import LocalForm, MemberForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = True
        return context


class LocalsListView(ListView):
    model = Local
    template_name = "locals.html"
    context_object_name = "locals"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['localspage'] = True
        return context


class CreateLocalView(CreateView):
    model = Local
    template_name = "local_add.html"
    success_url = reverse_lazy("locals:locals-list")
    form_class = LocalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['localspage'] = True
        return context


class UpdateLocalView(UpdateView):
    model = Local
    template_name = "local_add.html"
    success_url = reverse_lazy("locals:locals-list")
    form_class = LocalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['localspage'] = True
        context['update'] = True
        return context


def local_detail_view(request, pk):
    local = get_object_or_404(Local, pk=pk)
    executives = local.executives.all()
    members = local.members.all()

    context = {
        "local": local,
        "executives": executives,
        "members": members,
    }

    return render(request, "local_detail.html", context=context)


def add_member_view(request, pk):
    local = get_object_or_404(Local, pk=pk)
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.local = local
            instance.save()
            messages.success(request, f"{instance.name} successfully added")
            return redirect('locals:locals-detail', pk=pk)

    context = {
        "local": local,
        "form": form,
        "memberspage": True,
    }

    return render(request, "member_add.html", context=context)


def update_member_view(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(instance=member)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            instance = form.save()

            messages.success(request, f"{instance.name} successfully updated")
            return redirect('locals:locals-detail', pk=pk)

    context = {
        "local": local,
        "form": form,
        "memberspage": True,
    }

    return render(request, "member_add.html", context=context)