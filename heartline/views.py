from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import BPEntry, BPJournal
from .forms import BPEntryForm, BPJournalForm
from datetime import date, timedelta
from django.db.models import Avg, Max, Min

# Create your views here.

@login_required
def bp_list(request):
    entries = BPEntry.objects.filter(user= request.user).order_by('-recorded_date')
    return render(request, 'heartline/bp_list.html', {'entries': entries})

@login_required
def bp_detail(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk, user= request.user)
    return render(request,'heartline/bp_detail.html', {'entry': entry})

@login_required
def bp_create(request):
    if request.method == "POST":
        form = BPEntryForm(request.POST)
        if form.is_valid():
            entry=form.save(commit=False)
            entry.user= request.user
            entry.save()
            return redirect('bp_list')
    else:
        form = BPEntryForm()
    return render(request, 'heartline/bp_form.html', {'form': form})
        

@login_required
def bp_update(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk, user= request.user)
    if request.method == "POST":
        form = BPEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('bp_list')
    else:
        form = BPEntryForm(instance=entry)
    return render(request, 'heartline/bp_update.html', {'form': form})


@login_required
def bp_confirm_delete(request, pk):
    entry = get_object_or_404(BPEntry, pk=pk, user=request.user)
    if request.method == "POST":
        entry.delete()
        return redirect('bp_list')
    return render(request, 'heartline/bp_confirm_delete.html', {'entry':entry})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('bp_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    entries = BPEntry.objects.filter(user = request.user).order_by('-recorded_date')
    total_entries = entries.count()
    recent_entries = entries[:7]

    journal_entries = BPJournal.objects.filter(user = request.user).order_by('-recorded_date')
    total_journal_entries = journal_entries.count()
    recent_journal_entries = journal_entries[:7]

    today= date.today()
    seven_days_ago = today - timedelta(days=7)
    thirty_days_ago = today -timedelta(days=30)

    bp_last_7 = BPEntry.objects.filter(user = request.user,recorded_date__gte = seven_days_ago,)

    bp_7_stats = bp_last_7.aggregate(
        avg_sys_7d =Avg('systolic'),
        avg_dia_7d = Avg('diastolic'),
    )

    avg_sys_7d = bp_7_stats['avg_sys_7d']
    avg_dia_7d = bp_7_stats['avg_dia_7d']

    bp_last_30= BPEntry.objects.filter( user = request.user, recorded_date__gte= thirty_days_ago,)

    bp_30_stats = bp_last_30.aggregate(
        max_sys_30d = Max('systolic'),
        min_sys_30d = Min('systolic'),
    )

    max_sys_30d = bp_30_stats['max_sys_30d']
    min_sys_30d = bp_30_stats['min_sys_30d']

    bp_all = BPEntry.objects.filter(user = request.user).order_by('-recorded_date', '-created_at')
    latest_entry = bp_all.first()
    previous_entry = bp_all[1] if bp_all.count() > 1 else None

    systolic_change = None
    if latest_entry and previous_entry:
        systolic_change = latest_entry.systolic - previous_entry.systolic

    context = {
        'total_entries': total_entries,
        'recent_entries': recent_entries,
        'total_journal_entries': total_journal_entries,
        'recent_journal_entries': recent_journal_entries,
        'avg_sys_7d': avg_sys_7d,
        'avg_dia_7d': avg_dia_7d,
        'max_sys_30d': max_sys_30d,
        'min_sys_30d': min_sys_30d,
        'latest_entry': latest_entry,
        'previous_entry': previous_entry,
        'systolic_change': systolic_change,
    }
    return render(request, 'heartline/dashboard.html', context)

@login_required
def bp_journal_list(request):
    entries = BPJournal.objects.filter(user = request.user).order_by('-recorded_date')
    return render(request, 'heartline/bp_journal_list.html', {'entries': entries})

@login_required
def bp_journal_detail(request, pk):
    entry = get_object_or_404(BPJournal, pk=pk, user = request.user)
    return render(request, 'heartline/bp_journal_detail.html', {'entry': entry})

@login_required
def bp_journal_create(request):
    if request.method == 'POST':
        form = BPJournalForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('bp_journal_list')
    else:
        form = BPJournalForm()
    return render(request, 'heartline/bp_journal_form.html', {'form':form})

@login_required
def bp_journal_update(request, pk):
    entry = get_object_or_404(BPJournal, pk=pk, user = request.user)
    if request.method =='POST':
        form = BPJournalForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('bp_journal_list')
    else:
        form = BPJournalForm(instance=entry)
    return render(request, 'heartline/bp_journal_update.html', {'form':form})

@login_required
def bp_journal_delete(request, pk):
    entry = get_object_or_404(BPJournal, pk=pk, user = request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('bp_journal_list')
    return render(request, 'heartline/bp_journal_delete.html', {'entry':entry})
    