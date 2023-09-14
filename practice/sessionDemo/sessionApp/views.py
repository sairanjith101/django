from django.shortcuts import render

# Create your views here.

def session_count_view(request):
    count = request.session.get('count',0)
    totalCount = int(count) + 1
    request.session['count'] = totalCount
    return render(request, 'sessionApp/input.html', {'count':totalCount})
