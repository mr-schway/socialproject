from django.shortcuts import render
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_create(request):
  if request.method == 'POST':
    form = PostCreateForm(data = request.POST, files= request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
  else:
    form = PostCreateForm(data = request.GET)
  return render(request, 'posts/create.html', {'form': form})

