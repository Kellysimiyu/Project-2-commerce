from django.contrib.auth.models import AbstractUser
from django.db import models


# user model      
class User(AbstractUser):
     id = models.BigAutoField(primary_key=True)
      
   # model for the category 

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.name

# model for the listing

class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name=models.CharField(max_length=64)
    cover=models.ImageField(upload_to="images/", null=True,blank=True)
    Starting_Bid =models.IntegerField()
    Description = models.CharField(max_length=300)
    isActive =models.BooleanField()
    category= models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Lister =models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="User")

    
    def __str__(self):
        return f"{self.Name}:{self.cover} to {self.Starting_Bid} to {self.Description}"
  


# models for the watchlist 
class watchlist(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, related_name="wathclist")
    listing = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="watchlist")

    def __str__(self):
        return f"{self.user.username} watching {self.listing.Name}"
    
#Models for Comments 
class Comments(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()  # Add this field for the comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Add timestamp
    
    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.Name}"