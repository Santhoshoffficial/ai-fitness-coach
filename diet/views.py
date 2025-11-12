from django.shortcuts import render, get_object_or_404
from .models import DietMenu

def diet_plan(request):
    # --- Filters ---
    search_query = request.GET.get("search", "").strip()
    meal_filter = request.GET.get("category", "").strip()  # changed from 'meal' to 'category'

    # --- Base QuerySet ---
    diets = DietMenu.objects.all()

    if search_query:
        diets = diets.filter(name__icontains=search_query)
    if meal_filter and meal_filter.lower() != "all":
        diets = diets.filter(meal_type__iexact=meal_filter)

    # --- Popular & Recommended Menus ---
    popular_menus = DietMenu.objects.order_by("-rating")[:3]
    recommended_menus = DietMenu.objects.order_by("-health_score")[:3]

    context = {
        "diets": diets,
        "popular_menus": popular_menus,
        "recommended_menus": recommended_menus,
        "search_query": search_query,
        "meal_filter": meal_filter,
    }

    return render(request, "diet/diet-plan.html", context)


def diet_detail(request, pk):
    diet = get_object_or_404(DietMenu.objects.select_related(), pk=pk)
    return render(request, "diet/diet-detail.html", {"diet": diet})
