from django.db import models

# Create your models here.
class  Auteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Livre(models.Model):
    GENRE_CHOICES = [
        ('F', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SF', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MYS', 'Mystery'),
        ('ROM', 'Romance'),
        ('HOR', 'Horror'),
        ('BIO', 'Biography'),
        ('HIS', 'History'),
        ('SEL', 'Self-Help'),
    ]

    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')
    date_publication = models.DateField()
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    disponible = models.BooleanField(default=True) 


    def __str__(self):
        return f"{self.titre}"