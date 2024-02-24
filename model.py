# A Python function that creates a new product in your ecommerce website
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def create_product(request):
  # Check if the request is a POST method
  if request.method == "POST":
    # Create a new product form with the request data
    form = ProductForm(request.POST, request.FILES)
    # Validate the form
    if form.is_valid():
      # Save the form to the database
      form.save()
      # Redirect to the product list page
      return redirect("product_list")
  else:
    # Create an empty product form
    form = ProductForm()
  # Render the product creation page with the form
  return render(request, "product_create.html", {"form": form})
