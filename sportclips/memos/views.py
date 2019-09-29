from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render)
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView)
from users.models import User

from .forms import CommentForm
from .models import Memo


# Memo home page view
class MemoListView(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memos/memos.html'
    context_object_name = 'memos'
    ordering = ['-date_time']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the memos
        context['memo_list'] = Memo.objects.all()
        return context


# Memo list view by user
class UserMemoListView(LoginRequiredMixin, ListView):
    model = Memo
    template_name = 'memos/user_memos.html'
    context_object_name = 'memos'
    ordering = ['-date_time']
    paginate_by = 4

    def get_queryset(self):
        # get object or 404 on the user within the database
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Memo.objects.filter(author=user).order_by('-date_time')


# Single memo 'detail' view
class MemoDetailView(DetailView):
    model = Memo

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['memo_list'] = Memo.objects.all()
        return context


# View to create a memo
class MemoCreateView(LoginRequiredMixin, CreateView):
    model = Memo
    fields = ['title', 'content']

    def form_valid(self, form):
        # set the author as logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


# View to update memos
class MemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Memo
    fields = ['title', 'content']

    def form_valid(self, form):
        # set the author as logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # test if user is the one who created the memo
        memo = self.get_object()
        if self.request.user == memo.author:
            return True
        return False


# View to delete memos
class MemoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Memo
    success_url = '/memos'

    def test_func(self):
        # test if user is the one who created the memo
        memo = self.get_object()
        if self.request.user == memo.author:
            return True
        return False


def add_comment_to_memo(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    author = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = author
            comment.memo = memo
            comment.save()
            return redirect('memos-detail', pk=memo.pk)
    else:
        form = CommentForm()
    return render(request, 'memos/add_comment_to_memo.html', {'form': form})
