# colleges/models.py
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='city_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration_in_years = models.CharField(max_length=20) # e.g., "3 Years", "4 Years"
    average_fees = models.DecimalField(max_digits=10, decimal_places=2, help_text="Average fees in Lakhs (e.g., 5.50)")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class College(models.Model):
    COLLEGE_TYPE_CHOICES = [
        ('GOVT', 'Government'),
        ('PVT', 'Private'),
        ('SEMI', 'Semi-Government'),
    ]

    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='colleges')
    rank = models.PositiveIntegerField(null=True, blank=True, help_text="NIRF or other ranking")
    
    # --- ADD THIS LINE ---
    rank_source = models.CharField(max_length=100, null=True, blank=True, help_text="e.g., NIRF, India Today, Outlook")
    # --- END OF ADDITION ---
    
    courses = models.ManyToManyField(Course, related_name='colleges')
    fees_per_year = models.DecimalField(max_digits=10, decimal_places=2, help_text="Fees in Lakhs (e.g., 2.2)")
    image = models.ImageField(upload_to='college_images/', null=True, blank=True)
    area = models.CharField(max_length=150, blank=True, null=True, help_text="e.g., 'South Delhi'")
    college_type = models.CharField(max_length=4, choices=COLLEGE_TYPE_CHOICES, default='PVT')
    description = models.TextField(blank=True, null=True, help_text="A detailed description of the college")
    
    def __str__(self):
        return f"{self.name}, {self.city.name}"
    COLLEGE_TYPE_CHOICES = [
        ('GOVT', 'Government'),
        ('PVT', 'Private'),
        ('SEMI', 'Semi-Government'),
    ]

    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='colleges')
    rank = models.PositiveIntegerField(null=True, blank=True, help_text="NIRF or other ranking")
    courses = models.ManyToManyField(Course, related_name='colleges')
    fees_per_year = models.DecimalField(max_digits=10, decimal_places=2, help_text="Fees in Lakhs (e.g., 2.2)")
    image = models.ImageField(upload_to='college_images/', null=True, blank=True)
    area = models.CharField(max_length=150, blank=True, null=True, help_text="e.g., 'South Delhi'")
    college_type = models.CharField(max_length=4, choices=COLLEGE_TYPE_CHOICES, default='PVT')
    
    # --- THIS WAS THE MISSING LINE ---
    description = models.TextField(blank=True, null=True, help_text="A detailed description of the college")
    
    def __str__(self):
        return f"{self.name}, {self.city.name}"


# colleges/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator # Import validators

# ... (Keep your City, Course, College models) ...

# --- ADD THIS NEW MODEL ---
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100, blank=True, null=True, help_text="Optional: Course the user is interested in/studying")
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate the website (1-5 stars)"
    )
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} ({self.rating} stars)"

    class Meta:
        ordering = ['-created_at'] # Show newest reviews first if listed
# --- END OF NEW MODEL ---