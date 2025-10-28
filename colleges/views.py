# colleges/views.py
# colleges/views.py
from django.shortcuts import render, get_object_or_404
from .models import College, Course, City
from django.db.models import Q # Make sure Q is imported

from django.shortcuts import render, get_object_or_404, redirect # Add redirect
from django.contrib import messages # To show success messages
from django.core.mail import send_mail # For sending email
from django.conf import settings # To get admin email
from .models import College, Course, City, Review # Add Review
from .forms import ReviewForm # Import the new form
# ... (keep other imports like Q, login_required) ..

# ... (all your other views remain the same) ...

# REPLACE your old home_view with this one
def home_view(request):
    
    # --- Top 10 Table Logic ---
    # Get the course ID from the URL (e.g., ?course_filter=2)
    selected_course_id = request.GET.get('course_filter')
    
    # Start with all colleges that have a rank
    college_list = College.objects.filter(rank__isnull=False) 

    if selected_course_id:
        # If a course is selected, filter the list
        college_list = college_list.filter(courses__id=selected_course_id)
    
    # Order by rank and take the top 10 from the (filtered) list
    top_colleges = college_list.order_by('rank')[:10]
    # --- End Table Logic ---

    # --- Data for other sections on the page ---
    courses_for_cards = Course.objects.all()[:6] # For the "Browse by Course" cards
    all_courses_for_filter = Course.objects.all() # For the filter dropdown
    cities = City.objects.all() # For the "Browse by City" cards

    context = {
        'courses': courses_for_cards,
        'cities': cities,
        'top_colleges': top_colleges,
        'all_courses': all_courses_for_filter, # Pass this to the filter
        'selected_course_id': selected_course_id, # To re-select the dropdown
    }
    return render(request, 'index.html', context)




def course_detail_view(request, course_id):
    # Get the specific course the user clicked on, or show a 404 error
    course = get_object_or_404(Course, id=course_id)
    
    # Get all colleges that are linked to this course
    colleges_offering_course = course.colleges.all()
    
    context = {
        'course': course,
        'colleges': colleges_offering_course,
    }
    return render(request, 'course_detail.html', context)

def city_colleges_view(request, city_id):
    # Get the specific city
    city = get_object_or_404(City, id=city_id)
    
    # Get the course_id from the URL query (e.g., ?course_filter=2)
    course_filter_id = request.GET.get('course_filter')
    
    # Start by getting all colleges in this city
    colleges_in_city = College.objects.filter(city=city)
    
    # If a course filter is applied, filter the list further
    if course_filter_id:
        colleges_in_city = colleges_in_city.filter(courses__id=course_filter_id)
        
    # We also need to send all courses to the page to populate the filter dropdown
    all_courses = Course.objects.all()

    context = {
        'city': city,
        'colleges_in_city': colleges_in_city,
        'all_courses': all_courses,
        'selected_course_id': course_filter_id,
    }
    return render(request, 'city_colleges.html', context)

# colleges/views.py
from django.shortcuts import render, get_object_or_404
from .models import College, Course, City
from django.db.models import Q  # <-- IMPORT THIS

# ... (home_view, course_detail_view, city_colleges_view are the same) ...


# --- ADD THIS NEW VIEW FOR SEARCH RESULTS ---
def search_view(request):
    # Get the search query from the URL (e.g., /search/?q=MyQuery)
    query = request.GET.get('q')
    colleges = []

    if query:
        # Search for the query in college name, city name, AND course name
        # The .distinct() is important to avoid duplicates
        colleges = College.objects.filter(
            Q(name__icontains=query) |
            Q(city__name__icontains=query) |
            Q(courses__name__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'colleges': colleges,
    }
    return render(request, 'search_results.html', context)


# --- ADD THIS NEW VIEW FOR THE COLLEGE DETAIL PAGE ---
def college_detail_view(request, college_id):
    # Get the specific college by its ID, or show a 404 error if not found
    college = get_object_or_404(College, id=college_id)
    context = {
        'college': college
    }
    return render(request, 'college_detail.html', context)

def search_view(request):
    # Get the search query from the URL (e.g., /search/?q=MyQuery)
    query = request.GET.get('q')
    colleges = []

    if query:
        # Search for the query in college name, city name, AND course name
        # The .distinct() is important to avoid duplicates
        colleges = College.objects.filter(
            Q(name__icontains=query) |
            Q(city__name__icontains=query) |
            Q(courses__name__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'colleges': colleges,
    }
    return render(request, 'search_results.html', context)


# --- ADD THIS NEW VIEW FOR THE COLLEGE DETAIL PAGE ---
def college_detail_view(request, college_id):
    # Get the specific college by its ID, or show a 404 error if not found
    college = get_object_or_404(College, id=college_id)
    context = {
        'college': college
    }
    return render(request, 'college_detail.html', context)

# colleges/views.py

from django.shortcuts import render, get_object_or_404
from .models import College, Course, City
from django.db.models import Q
# Import the login_required decorator
from django.contrib.auth.decorators import login_required

# --- Add @login_required decorator to all views you want to protect ---

@login_required # Add this line
def home_view(request):
    selected_course_id = request.GET.get('course_filter')
    college_list = College.objects.filter(rank__isnull=False)
    if selected_course_id:
        college_list = college_list.filter(courses__id=selected_course_id)
    top_colleges = college_list.order_by('rank')[:10]

    courses_for_cards = Course.objects.all()[:6]
    all_courses_for_filter = Course.objects.all()
    cities = City.objects.all()

    context = {
        'courses': courses_for_cards,
        'cities': cities,
        'top_colleges': top_colleges,
        'all_courses': all_courses_for_filter,
        'selected_course_id': selected_course_id,
    }
    return render(request, 'index.html', context)

@login_required # Add this line
def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    colleges_offering_course = course.colleges.all()
    context = {
        'course': course,
        'colleges': colleges_offering_course,
    }
    return render(request, 'course_detail.html', context)

@login_required # Add this line
def city_colleges_view(request, city_id):
    city = get_object_or_404(City, id=city_id)
    course_filter_id = request.GET.get('course_filter')
    colleges_in_city = College.objects.filter(city=city)
    if course_filter_id:
        colleges_in_city = colleges_in_city.filter(courses__id=course_filter_id)
    all_courses = Course.objects.all()

    context = {
        'city': city,
        'colleges_in_city': colleges_in_city,
        'all_courses': all_courses,
        'selected_course_id': course_filter_id,
    }
    return render(request, 'city_colleges.html', context)

@login_required # Add this line
def search_view(request):
    query = request.GET.get('q')
    colleges = []
    if query:
        colleges = College.objects.filter(
            Q(name__icontains=query) |
            Q(city__name__icontains=query) |
            Q(courses__name__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'colleges': colleges,
    }
    return render(request, 'search_results.html', context)

@login_required # Add this line
def college_detail_view(request, college_id):
    college = get_object_or_404(College, id=college_id)
    context = {
        'college': college
    }
    return render(request, 'college_detail.html', context)


def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save() # Save the review to the database

            # --- Send Email to Admin ---
            subject = f"New Website Feedback ({review.rating} Stars)"
            message = f"""
            A new review has been submitted:

            Name: {review.name}
            Course: {review.course or 'Not provided'}
            Rating: {review.get_rating_display()}
            Feedback:
            {review.feedback}

            Submitted on: {review.created_at.strftime('%Y-%m-%d %H:%M:%S')}
            """
            from_email = settings.DEFAULT_FROM_EMAIL # Use email from settings.py
            admin_emails = "saranshsahu532@gmail.com" # Get emails of admins defined in settings.py

            try:
                if admin_emails: # Only send if ADMINS is configured
                    send_mail(subject, message, from_email, admin_emails)
                else:
                    print("WARNING: No ADMINS configured in settings.py. Email not sent.")
            except Exception as e:
                # Log the error, but don't crash the user's experience
                print(f"Error sending feedback email: {e}")


            messages.success(request, 'Thank you! Your feedback has been submitted.')
            return redirect('home') # Redirect to homepage after submission
        else:
            # Form is invalid, show errors
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request, show an empty form
        form = ReviewForm()

    context = {'form': form}
    return render(request, 'review_form.html', context)
# --- END OF NEW VIEW ---