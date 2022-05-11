from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import CustomUser
from .forms import (CustomUserRegistrationForm, CutomUserUpdateForm)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

					

class CustomUserProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
	model = CustomUser
	form_class = CutomUserUpdateForm
	template_name = 'users/profile.html'
	success_message = "Profile updated successfully." 

	def get_success_url(self):
		pk = self.get_object().pk
		return reverse_lazy('profile', kwargs={'pk': pk})


class CustomUserLoginView(SuccessMessageMixin, auth_views.LoginView):
	form_class = AuthenticationForm
	template_name = 'users/login.html'
	redirect_authenticated_user = True
	success_message = "Login successfully." 

	# + redirect_authenticated_user = True -> 
	# -> send to other view if user is already auth and try to access login page
	def get_success_url(self): 
		pk = self.request.user.pk
		return reverse_lazy('profile', kwargs={'pk': pk})


class CustomUserRegisterView(generic.CreateView):
	form_class = CustomUserRegistrationForm
	template_name = 'users/register.html'
	success_url = reverse_lazy('login')


class CustomUserLogoutView(SuccessMessageMixin, auth_views.LogoutView):
	model = CustomUser
	next_page = 'login'
	success_message = "Logout successfully" 


class CustomUserChangePassView(LoginRequiredMixin, auth_views.PasswordChangeView):  
	form_class = PasswordChangeForm
	template_name = 'users/password_change_form.html'
	success_url = reverse_lazy('password_change_done')

class CustomUserChangePassDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
	template_name = 'users/password_change_done.html'

	