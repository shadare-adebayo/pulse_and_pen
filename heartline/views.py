from django.shortcuts import render, get_object_or_404, redirect
from .models import BPEntry
from .forms import BPEntryForm

# Create your views here.
def bp_list(request):
    entries = BPEntry.objects.all()
    return render(request, 'heartline/bp_list.html', {'entries': entries})


def bp_detail(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk)
    return render(request,'heartline/bp_detail.html', {'entry': entry})

def bp_create(request):
    if request.method == "POST":
        form = BPEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bp_list')
    else:
        form = BPEntryForm()
    return render(request, 'heartline/bp_form.html', {'form': form})
        

def bp_update(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk)
    if request.method == "POST":
        form = BPEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('bp_list')
    else:
        form = BPEntryForm(instance=entry)
    return render(request, 'heartline/bp_update.html', {'form': form})

def bp_confirm_delete(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk)
    if request.method == "POST":
        entry.delete()
        return redirect('bp_list')
    return render(request, 'heartline/bp_confirm_delete.html', {'entry':entry})

