from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Like,User,PostView
from .forms import PostForm, CommentForm,CustomUserCreationForm,AvatarForm,UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

        
class PostHomeView(View):
    def get(self,request,*args,**kwargs):
        context={
            
        }
        return render(request,'home.html',context)
    
     
class PostListView(ListView):
    model= Post
    def get_context_data(self,**kwargs):
        """este medoto pasa el contexto"""
        context=super().get_context_data(**kwargs)
        context.update({'view':'List View'})
        return context


class PostDetailView(DetailView):
    model= Post
    template_name='post_detail.html'
    
    def post(self,*args,**kwargs):
        form=CommentForm(self.request.POST)
        if form.is_valid():
            post=self.get_object()
            comment=form.instance
            comment.user=self.request.user
            comment.post=post
            comment.save()
            return redirect('detail',slug=post.slug)
       
        return redirect('detail', slug=self.get_object().slug())
            
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({'view':'Detail','form':CommentForm()})
        return context
    
    def get_object(self, **kwargs):
        object=super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user,post=object)
            return object


class PostCreateView(CreateView):
    form_class=PostForm
    model= Post    
    success_url='/'
           
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({'view_type':'create'})
        return context


class PostUpdateView(UpdateView):
    class_form=PostForm
    model= Post
    fields=['title','content','thumbnail','author','slug']
    success_url='/'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context.update({
            'view_type':'update',
            'form':self.get_form(),
            'object':self.get_object(),
        })
        return context
            

class PostDeleteView(DeleteView):
    model= Post
    template_name='post_delete.html'
    success_url='/'


class PostRegisterView(CreateView):
    model= User
    form_class=CustomUserCreationForm
    template_name='post_register.html'

    def form_valid(self,form):
        form.save()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password1')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(self.request,user)
            return redirect('home')
        else:
            return self.form_invalid(form)


class UploadAvatarView(CreateView):
    model= User
    form_class=AvatarForm
    #template_name='post_upload_avatar.html'
    success_url='/profile/'
    
    def form_valid(self,form):
        form.save(commit=False)
        form.instance.user=self.request.user
        form.save()
        return super().form_valid(form)


def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    if request.method=='POST':
        my_form=UserEditForm(request.POST,instance=user)
        
        if my_form.is_valid():
            my_form.save()
            return redirect('profile')
    else:
        my_form=UserEditForm(instance=user)
    context={
        'my_form':my_form,
        'user':user
    }
    return render(request,'post_update_profile.html',context)

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None,'Wrong user or password')
    else:
        form=AuthenticationForm()
    context={'form':form}
    return render(request,'post_login.html',context)


@login_required
def profile_view(request):
    user= request.user
    if user.user_avatar:
        avatar_url=user.user_avatar.image.url
    else:
        avatar_url=None
        total_likes=Like.objects.filter(user=user).count()
        total_posts=Post.objects.filter(author=user).count()
    context={
        'user':user,
        'avatar_url':avatar_url,
        'total_likes':total_likes,
        'total_posts':total_posts,
    }            
    return render(request,'post_profile.html',context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def like(request,slug):
    post = get_object_or_404(Post,slug=slug)
    like_qs=Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail',slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail',slug=slug)

