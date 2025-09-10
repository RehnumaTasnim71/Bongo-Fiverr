from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Order, Review
from .forms import OrderForm, ReviewForm, OrderCompletionForm
from services.models import Service
from notifications.utils import create_notification


@login_required
def place_order(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.user.role != 'buyer':
        return redirect('login')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.service = service
            order.buyer = request.user
            order.seller = service.seller
            order.save()

            # Notify seller
            create_notification(
                order.seller,
                f"New order placed for your service: {service.title}"
            )

            messages.success(request, "Order placed successfully!")
            return redirect('buyer_dashboard')
    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {
        'form': form,
        'service': service
    })


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, id=pk)
    form = None

    if request.user.role == 'buyer' and order.status == 'completed':
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.order = order
                review.buyer = request.user     
                review.seller = order.seller
                review.service = order.service  
                review.save()


                # Notify seller
                create_notification(
                    order.seller,
                    f"{request.user.username} left a review for your service: {order.service.title}"
                )

                messages.success(request, "Review submitted successfully!")
                return redirect('buyer_dashboard')
        else:
            form = ReviewForm()

    return render(request, 'orders/order_detail.html', {
        'order': order,
        'form': form
    })


@login_required
def buyer_dashboard(request):
    buyer = request.user

    # Orders
    orders = Order.objects.filter(buyer=buyer).order_by('-created_at')
    status_filter = request.GET.get('status')
    if status_filter:
        orders = orders.filter(status=status_filter)

    # Reviews given by this buyer
    reviews = Review.objects.filter(buyer=buyer).select_related('seller', 'order', 'order__service')

    # Applied services
    applied_services = [order.service for order in orders]

    context = {
        'orders': orders,
        'reviews': reviews,
        'applied_services': applied_services,
        'status_filter': status_filter,  
    }

    return render(request, 'orders/buyer_dashboard.html', context)


@login_required
def seller_dashboard(request):
    user = request.user
    # Ensure only sellers can access
    if not user.groups.filter(name='Seller').exists():
        return redirect('buyer_dashboard')

    services = Service.objects.filter(seller=user)
    orders = Order.objects.filter(service__seller=user)

    # Total earnings
    earnings = orders.filter(status="completed").aggregate(
        total=Sum("service__price")
    )["total"] or 0

    # Reviews for this seller's services
    reviews = Review.objects.filter(order__service__in=services).select_related(
        'buyer', 'order', 'order__service'
    ).order_by('-created_at')

    context = {
        "services": services,
        "orders": orders,
        "earnings": earnings,
        "reviews": reviews,
    }

    return render(request, "users/seller_dashboard.html", context)


@login_required
def complete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        if request.FILES.get("delivery_file"):
            order.delivery_file = request.FILES["delivery_file"]
            order.status = "completed"
            order.save()

            # Notify buyer
            create_notification(
                order.buyer,
                f"Your order #{order.id} has been marked as completed by {order.seller.username}"
            )

            messages.success(request, "Order marked as completed and file uploaded!")
            return redirect("seller_dashboard")
        else:
            messages.error(request, "Please upload a file before completing the order.")
            return redirect("complete_order", order_id=order.id)

    return render(request, "orders/complete_order.html", {"order": order})


@login_required
def order_mark_inprogress(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = "in_progress"
    order.save()
    messages.success(request, "Order marked as In Progress.")
    return redirect("seller_dashboard")


@login_required
def submit_review(request, order_id):
    order = get_object_or_404(Order, id=order_id, buyer=request.user)

    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment", "")

        review, created = Review.objects.get_or_create(
            order=order,
            buyer=request.user,
            defaults={'rating': rating, 'comment': comment, 'seller': order.seller}
        )
        if not created:
            review.rating = rating
            review.comment = comment
            review.save()

        messages.success(request, "Review submitted successfully!")
        return redirect('buyer_dashboard')

    return render(request, "orders/submit_review.html", {"order": order})
