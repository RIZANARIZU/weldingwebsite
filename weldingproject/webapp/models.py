from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='projects/')

    created_at = models.DateTimeField(auto_now_add=True)

    edited_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title



class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    location = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




class Review(models.Model):

    name = models.CharField(max_length=100)


    rating = models.IntegerField(
        choices=[
            (1, "⭐"),
            (2, "⭐⭐"),
            (3, "⭐⭐⭐"),
            (4, "⭐⭐⭐⭐"),
            (5, "⭐⭐⭐⭐⭐"),
        ]
    )


    message = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name