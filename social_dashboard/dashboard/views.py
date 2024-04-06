from django.shortcuts import render

from .models import Message


def dashboard_view(request):
    messages = (
        Message.objects.all()
    )  # This fetches all messages, you'll add filtering later
    return render(request, "dashboard/dashboard.html", {"messages": messages})
