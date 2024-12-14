from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


# Create your views here.

## Vista a través de templates.
def register(request):
    """Vista para registrar un usuario."""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'authentication/register.html', {'error': 'Las contraseñas no coinciden'})

        if User.objects.filter(username=username).exists():
            return render(request, 'authentication/register.html', {'error': 'El nombre de usuario ya existe'})

        if User.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {'error': 'El correo ya está registrado'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Iniciar sesión automáticamente tras el registro.

        return redirect('edit_profile')

    return render(request, 'authentication/register.html')

def login_view(request):
    """Vista para iniciar sesión."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirigir al perfil para completar los datos faltantes.
            return redirect('edit_profile')
        else:
            return render(request, 'authentication/login.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'authentication/login.html')

@login_required
def edit_profile(request):
    """Vista para editar avatar y fecha de nacimiento."""
    profile = request.user.profile
    status = None

    if request.method == 'POST':
        profile.birth_date = request.POST.get('birth_date', profile.birth_date)
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        status = 'ok'  # Cambios realizados.

    return render(request, 'authentication/edit_profile.html', {'profile': profile, 'status': status})

@login_required
def logout_view(request):
    """Cierra la sesión del usuario."""
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    """Vista para cambiar la contraseña del usuario."""
    status = None

    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not check_password(current_password, request.user.password):
            status = 'error'
        elif new_password != confirm_password:
            status = 'error'
        else:
            request.user.set_password(new_password)
            request.user.save()
            login(request, request.user)
            status = 'ok'
    return render(request, 'authentication/change_password.html', {'status': status})

## Vista basada a través de API Rest - obtiene un JSON.
class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        data = request.data
        profile = user.profile
        profile.bio = data.get('bio', profile.bio)
        profile.birth_date = data.get('birth_date', profile.birth_date)
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        profile.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
