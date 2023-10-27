# fitness_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile, FitnessTip
from .forms import UserProfileForm, FitnessTipForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# users profile views category
@login_required
def userprofile_detail(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profiles/userprofile_detail.html', {'profile': profile})

@login_required
def userprofile_create(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
        return redirect('userprofile_update', pk=profile.pk)
    except UserProfile.DoesNotExist:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user  # Set the user to the currently logged-in user
                profile.save()
                return redirect('userprofile_detail')
        else:
            form = UserProfileForm()
        return render(request, 'profiles/userprofile_form.html', {'form': form})

@login_required
def userprofile_update(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('userprofile_detail')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profiles/userprofile_form.html', {'form': form})

@login_required
def userprofile_delete(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk, user=request.user)
    if request.method == 'POST':
        profile.delete()
        return redirect('userprofile_detail')
    return render(request, 'profiles/userprofile_confirm_delete.html', {'profile': profile})


# fitness views category
@login_required
def fitnesstip_list(request):
    tips = FitnessTip.objects.all()
    return render(request, 'fitness_app/fitnesstip_list.html', {'tips': tips})

@login_required
def fitnesstip_detail(request, pk):
    tip = get_object_or_404(FitnessTip, pk=pk)
    return render(request, 'fitness_app/fitnesstip_detail.html', {'tip': tip})

@login_required
def fitnesstip_create(request):
    if request.method == 'POST':
        form = FitnessTipForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            tip = form.save()
            return redirect('fitnesstip_detail', pk=tip.pk)
    else:
        form = FitnessTipForm(user=request.user)
    return render(request, 'fitness_app/fitnesstip_form.html', {'form': form})

@login_required
def fitnesstip_update(request, pk):
    tip = get_object_or_404(FitnessTip, pk=pk)
    if tip.author == request.user:
        if request.method == 'POST':
            form = FitnessTipForm(request.POST, request.FILES, instance=tip, user=request.user)
            if form.is_valid():
                form.save()
                return redirect('fitnesstip_detail', pk=tip.pk)
        else:
            form = FitnessTipForm(instance=tip, user=request.user)
        return render(request, 'fitness_app/fitnesstip_form.html', {'form': form})
    else:
        raise Http404("You do not have permission to edit this tip")

@login_required
def fitnesstip_delete(request, pk):
    tip = get_object_or_404(FitnessTip, pk=pk)
    if tip.author == request.user:
        if request.method == 'POST':
            tip.delete()
            return redirect('fitnesstip_list')
        return render(request, 'fitness_app/fitnesstip_confirm_delete.html', {'tip': tip})
    else:
        raise Http404("You do not have permission to delete this tip")
