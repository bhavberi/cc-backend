from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cc_admins.serializers import ClubSerializer
from organizers.serializers import EventSerializer
from .models import Club, Event
from django.utils import timezone

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required
def get_token(request):
    user = request.user
    usergroup = "enduser"
    if user.groups.exists():
        usergroup = user.groups.all()[0].name
    token, created = Token.objects.get_or_create(user=user)
    context = {"token": token.key, "usergroup": usergroup}
    return render(request, "login_redirect.html", context)


@api_view(["GET"])
def events(request):
    token = request.headers.get("Authorization", None)
    events = Event.objects.all()
    for event in events:
        if event.datetime < timezone.now() and event.state != "deleted":
            event.state = "completed"
            event.save()
    if token:
        mail = Token.objects.get(key=token[6:]).user
        club = Club.objects.filter(mail=mail).first()
        if club:
            events = events.filter(club=club)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def clubs(request):
    club_id = request.query_params.get("id", None)
    clubs = Club.objects.all()
    if club_id is not None:
        clubs = clubs.filter(id=club_id)
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)
