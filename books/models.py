from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class AuthorProfile(models.Model):
    # One-to-One relationship
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    website = models.URLField(blank=True)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='author_profiles/', blank=True)

    def __str__(self):
        return f"Profile of {self.author.name}"

class Book(models.Model):
    # Many-to-One relationship (Many books can have one author)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    # Many-to-Many relationship (Buyers can purchase many books, and books can be purchased by many buyers)
    purchased_books = models.ManyToManyField(Book, through='Purchase')

    def __str__(self):
        return self.name

class Purchase(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.buyer.name} purchased {self.book.title}"