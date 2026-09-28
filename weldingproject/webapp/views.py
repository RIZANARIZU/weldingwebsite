from django.shortcuts import render
from django.db.models import Avg

from .models import Contact, Project, Review


# Home Page
def home(request):
    return render(
        request,
        'home.html'
    )


# About Page
def about(request):
    return render(
        request,
        'about.html'
    )


# Services Page
def services(request):
    return render(
        request,
        'services.html'
    )


# Projects Page
def projects(request):
    projects = Project.objects.all().order_by('-created_at')

    return render(
        request,
        'projects.html',
        {
            'projects': projects
        }
    )


# Contact Page
def contact(request):
    success = False
    review_success = False

    # POST
    if request.method == "POST":

        # CONTACT FORM
        if request.POST.get("form_type") == "contact":

            Contact.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                location=request.POST.get("location"),
                message=request.POST.get("message")
            )

            success = True

        # CUSTOMER REVIEW FORM
        elif request.POST.get("form_type") == "review":

            Review.objects.create(
                name=request.POST.get("review_name"),
                rating=int(request.POST.get("rating")),
                message=request.POST.get("review_message")
            )

            review_success = True

    # CUSTOMER REVIEWS
    reviews = Review.objects.all().order_by("-created_at")

    # CALCULATE AVERAGE RATING
    average_rating = reviews.aggregate(
        Avg("rating")
    )["rating__avg"]

    if average_rating:
        average_rating = round(
            average_rating,
            1
        )
    else:
        average_rating = 0

    return render(
        request,
        "contact.html",
        {
            "success": success,
            "review_success": review_success,
            "reviews": reviews,
            "average_rating": average_rating
        }
    )