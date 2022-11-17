from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from . import models, forms

User = get_user_model()

class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    template_name: str = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'profile_form': forms.ProfileForm,
        })
        return ctx

    def form_valid(self, form):
        self.object = form.save()
        is_admin_user = self.request.POST.get('is_admin', False)
        if is_admin_user:
            self.object.is_staff = True
            self.object.save()
        else:
            profile_form = forms.ProfileForm(data=self.request.POST, files=self.request.FILES)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = self.object
                profile.save()
            else:
                self.object.delete()
                return self.render_to_response(self.get_context_data(profile_form=profile_form))
        return super().form_valid(form)

class SignInView(LoginView):
    template_name = 'signin.html'

class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name: str = 'user-home.html'

class AlumniListView(LoginRequiredMixin, ListView):
    template_name: str = 'alumni-list.html'
    queryset = User.objects.filter(is_staff=False)

    def post(self, request, *args, **kwargs):
        filter_field = request.POST.get('filter', None)
        input = request.POST.get('input', None)
        if filter_field == 'year':
            input = int(input)
        self.object_list = User.objects.none()
        if filter_field and input:
            data = {
                f'profile__{filter_field}': input
            }
            try:
                self.object_list = User.objects.filter(**data)
            except:
                self.object_list = User.objects.none()
        context = self.get_context_data()
        return self.render_to_response(context)

class NewsAddView(LoginRequiredMixin, CreateView):
    template_name = 'news-add.html'
    model = models.News
    fields = ('title', 'content', 'pic', )
    success_url = reverse_lazy('news-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'News added')
        return super().form_valid(form)

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    template_name: str = 'news-add.html'
    model = models.News
    fields = ('title', 'content', 'pic', )
    success_url = reverse_lazy('news-list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'update': True,
        })
        return ctx

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'News updated')
        return super().form_valid(form)

class NewsListView(LoginRequiredMixin, ListView):
    template_name: str = 'news-list.html'
    model = models.News

class EventAddView(LoginRequiredMixin, CreateView):
    template_name = 'event-add.html'
    model = models.Event
    fields = ('title', 'content', 'pic', 'mission', 'vission')
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Event added')
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'event-add.html'
    model = models.Event
    fields = ('title', 'content', 'pic', 'mission', 'vission')
    success_url = reverse_lazy('event-list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'update': True,
        })
        return ctx

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Event Updated')
        return super().form_valid(form)

class EventListView(LoginRequiredMixin, ListView):
    template_name: str = 'event-list.html'
    model = models.Event


class PhotoAddView(LoginRequiredMixin, CreateView):
    template_name = 'photo-add.html'
    model = models.Photo
    fields = ('pic', 'name', )
    success_url = reverse_lazy('photo-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Photo added')
        return super().form_valid(form)

class PhotoListView(LoginRequiredMixin, ListView):
    template_name: str = 'photo-list.html'
    model = models.Photo

class FeedbackAddView(LoginRequiredMixin, CreateView):
    template_name = 'feedback-add.html'
    model = models.FeedBack
    fields = ('feedback', )
    success_url = reverse_lazy('feedback-add')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'object_list': models.FeedBack.objects.filter(created_by=self.request.user)
        })
        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Feedback added')
        return super().form_valid(form)


class FeedbackListView(LoginRequiredMixin, ListView):
    template_name: str = 'feedback-list.html'
    model = models.FeedBack


class ResponseAddView(LoginRequiredMixin, CreateView):
    template_name = 'response-add.html'
    model = models.Response
    fields = ('response', )
    success_url = reverse_lazy('feedback-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        feedback = models.FeedBack.objects.get(id = self.kwargs.get('feed_id'))
        feedback.response = self.object
        feedback.save()
        messages.add_message(self.request, messages.SUCCESS, 'Response added')
        return super().form_valid(form)