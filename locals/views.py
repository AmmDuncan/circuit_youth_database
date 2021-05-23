from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import decorators, mixins
from django.views.generic import (TemplateView, ListView, CreateView,
                                  UpdateView, DetailView)

from .models import Local, Executive, Member
from .forms import LocalForm, MemberForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = True
        return context


class LocalsListView(mixins.LoginRequiredMixin, ListView):
    model = Local
    template_name = "locals.html"
    context_object_name = "locals"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['localspage'] = True
        return context


# class CreateLocalView(mixins.LoginRequiredMixin, CreateView):
#     model = Local
#     template_name = "local_add.html"
#     success_url = reverse_lazy("locals:locals-list")
#     form_class = LocalForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['localspage'] = True
#         return context

def local_create_view(request):
    form = LocalForm()

    if request.method == "POST":
        form = LocalForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if not Local.objects.filter(name=instance.name).exists():
                instance.save()
                return redirect('locals:locals-list')
            else:
                return redirect('locals:locals-list')

    context = {
        "form": form,
        "localspage": True,
    }

    return render(request, "local_add.html", context=context)



class UpdateLocalView(mixins.LoginRequiredMixin, UpdateView):
    model = Local
    template_name = "local_add.html"
    success_url = reverse_lazy("locals:locals-list")
    form_class = LocalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['localspage'] = True
        context['update'] = True
        return context


@decorators.login_required
def local_detail_view(request, pk):
    local = get_object_or_404(Local, pk=pk)
    executives = local.executives.all()
    members = local.members.all()

    context = {
        "local": local,
        "localspage": True,
        "executives": executives,
        "members": members,
    }

    return render(request, "local_detail.html", context=context)


@decorators.login_required
def add_member_view(request, pk):
    local = get_object_or_404(Local, pk=pk)
    form = MemberForm()

    if request.method == "POST":
        form = MemberForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if not Member.objects.filter(name=instance.name).exists():
                instance.local = local
                instance.save()
                messages.success(request, f"{instance.name} successfully added")
                return redirect('locals:locals-detail', pk=pk)
            else:
                return redirect('locals:locals-detail', pk=pk)


    context = {
        "local": local,
        "form": form,
        "memberspage": True,
    }

    return render(request, "member_add.html", context=context)


@decorators.login_required
def update_member_view(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(instance=member)

    next = request.GET.get('next')

    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            instance = form.save()

            messages.success(request, f"{instance.name} successfully updated")
            if next:
                return HttpResponseRedirect(next)
            return redirect('locals:locals-detail', pk=instance.local.pk)

    context = {
        "form": form,
        "memberspage": True,
        "update": True
    }

    return render(request, "member_add.html", context=context)


class MemberListView(mixins.LoginRequiredMixin, ListView):
    template_name = "members_list.html"
    context_object_name = "members"

    def get_queryset(self):
        local_pk = self.request.GET.get('local', None)
        try:
            local = get_object_or_404(Local, pk=local_pk)
            members = local.members.all()
        except (ValueError, Http404):
            members = Member.objects.all()
        return members

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['memberspage'] = True
        try:
            context["active_local"] = int(
                self.request.GET.get("local", None)
            )
        except (ValueError, TypeError):
            pass
        context['locals'] = Local.objects.all()
        return context


class ExecutiveListView(MemberListView):
    template_name = "executives_list.html"

    def get_queryset(self):
        local_pk = self.request.GET.get('local', None)
        try:
            local = get_object_or_404(Local, pk=local_pk)
            members = local.executives.all()
        except (ValueError, Http404):
            members = Executive.objects.all()
        return members

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['executivespage'] = True
        context['memberspage'] = False
        try:
            context["active_local"] = int(
                self.request.GET.get("local", None)
            )
        except (ValueError, TypeError):
            pass
        context['locals'] = Local.objects.all()
        return context


class MemberDetailView(mixins.LoginRequiredMixin, DetailView):
    template_name = "member_detail.html"
    model = Member
    context_object_name = "member"


@decorators.login_required
def search_view(request):
    q = request.GET.get('q')

    if q:
        executives = Executive.objects.filter(
            Q(name__icontains=q)
        )
        members = Member.objects.filter(
            Q(name__icontains=q) |
            Q(occupation__icontains=q) |
            Q(address__icontains=q)
        )
    else:
        executives = []
        members = []

    context  = {
        "executives": executives,
        "members": members,
        "query": q or ""
    }

    return render(request, "search.html", context=context)

