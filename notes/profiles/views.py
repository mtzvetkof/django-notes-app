from django.shortcuts import render, redirect

from notes.common.utils import get_profile, get_notes
from notes.profiles.forms import CreateProfileForm, DeleteProfileForm


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def profile_info(request):
    profile = get_profile()
    notes = get_notes()
    notes_number = len(notes)
    context = {
        'profile': profile,
        'notes_number': notes_number,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = get_notes()
    notes.delete()
    profile.delete()
    return redirect('home')



