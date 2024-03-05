from django.shortcuts import render, redirect
from django.views.generic import FormView,CreateView
from .forms import RegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Posts,Like
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .models import UserAccounts
from django.contrib.auth.models import User
# Create your views here.

def send_transaction_email(user, subject, template):
     
        token = default_token_generator.make_token(user)
        print("token ", token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        print("uid ", uid)
        confirm_link = f"http://127.0.0.1:8000/accounts/active/{uid}/{token}"
        message = render_to_string(template, {
            'user' : user,
            'meet_link': confirm_link
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

class UserSignupView(FormView):
    template_name = 'user_signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        
        user = form.save()

        login(self.request,user)
        print(user)
        messages.success(
            self.request,
            f'Signup Successfully .Please check your email for conformation link'
        )
        user.is_active = False
        send_transaction_email(self.request.user, 'Register Confirm','login_email.html')
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Login successfully. Welcome Back !')
        
        return super().form_valid(form)
    
def UserLogout(request):
    logout(request)
    messages.info(request, 'Logout successfully.!')
    return redirect('home')


@login_required
def profile(request):
    posts = Posts.objects.all()
    like_history = Like.objects.filter(user=request.user)
    return render(request,'profile.html', {'like_history':like_history,'posts':posts})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         profile_form = forms.ChangeUserData(request.POST, instance = request.user)
#         if profile_form.is_valid():
#             messages.success(request,'Profile Updated Successfuly')
#             profile_form.save()
#             return redirect('profile')
#     else:   
#         profile_form = forms.ChangeUserData(instance = request.user)
#     return render(request,'edit_profile.html',{'form':profile_form })

