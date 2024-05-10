from django.shortcuts import render, redirect
from .forms import HealthRecordForm
from datetime import date, timedelta
from .models import Student

def add_health_record(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('health_record_success')
    else:
        form = HealthRecordForm()
    return render(request, 'myhealthapp/add_health_record.html', {'form': form})

def health_record_success(request):
    return render(request, 'myhealthapp/health_record_success.html')

def your_view(request):
    # 生徒のリストを取得する仮定
    students = Student.objects.all()
    # 今週の日付リストを生成
    today = date.today()
    week_dates = [today + timedelta(days=i) for i in range(7)]  # 一週間の日付

    context = {
        'students': students,
        'dates': week_dates,
    }
    return render(request, 'myhealthapp/your_template.html', context)