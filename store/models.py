from django.db import models

class Puppy(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_adopted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    age=models.PositiveBigIntegerField(default=16)
    gender=models.CharField(max_length=255)
    registration=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class PuppyImage(models.Model):
    puppy = models.ForeignKey(Puppy, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='puppy_images/')


class AdoptionRequest(models.Model):
    puppy = models.ForeignKey('Puppy', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Adoption Request by {self.name} for {self.puppy.name}"
# store/models.py


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
