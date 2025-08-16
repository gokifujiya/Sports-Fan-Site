import random
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

# Sample data — swap to your favorite sport/game
SPORT_IMAGE_URLS = [
    "https://images.unsplash.com/photo-1517649763962-0c623066013b",  # tennis
    "https://images.unsplash.com/photo-1521417531039-94da0b6b1ef4",  # soccer
    "https://images.unsplash.com/photo-1502877338535-766e1452684a",  # basketball
]

NOTABLES = [
    {
        "name": "Alex Ace",
        "image": "https://images.unsplash.com/photo-1517649763962-0c623066013b",
        "description": "Aggressive baseline player with powerful forehand.",
        "stats": ["World Rank: 3", "Titles: 12", "Handed: Right", "Age: 26"],
    },
    {
        "name": "Bella Blitz",
        "image": "https://images.unsplash.com/photo-1502877338535-766e1452684a",
        "description": "Playmaker known for vision and clutch plays.",
        "stats": ["MVP: 2x", "Assists/Game: 8.1", "Team Captain", "Age: 29"],
    },
    {
        "name": "Cypher",
        "image": "https://images.unsplash.com/photo-1521417531039-94da0b6b1ef4",
        "description": "Esports sniper with unmatched map control.",
        "stats": ["K/D: 1.42", "Headshot%: 31", "Role: Sentinel", "Age: 22"],
    },
]

EXTERNAL_LINKS = [
    "https://www.espn.com/",
    "https://www.skysports.com/",
    "https://www.ea.com/games",
]

def index(request):
    img_url = random.choice(SPORT_IMAGE_URLS) if SPORT_IMAGE_URLS else ""
    return render(request, "index.html", {"img_url": img_url})

def rules(request):
    return render(request, "rules.html")

def notablesList(request):
    return render(request, "notables_list.html", {"notables": NOTABLES})

def notablesDetail(request, notablesIndex: int):
    try:
        player = NOTABLES[notablesIndex]
    except IndexError:
        raise Http404("No player exists")
    return render(request, "notables_detail.html", {"player": player, "idx": notablesIndex})

def externalLinks(request):
    return render(request, "external_links.html", {"links": EXTERNAL_LINKS})
