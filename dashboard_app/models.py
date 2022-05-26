from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
    )

class Data(models.Model):
     name = models.CharField(max_length=100, null=True)
     sex = models.PositiveBigIntegerField(choices=GENDER, null=True)
     age = models.PositiveBigIntegerField(validators=[MinValueValidator(5), MaxValueValidator(50)], null=True)	
     nombre_de_personnes = models.CharField(max_length=100, null=True)
     predictions = models.CharField(max_length=100, blank=True)
     date = models.DateTimeField(auto_now_add=True)

def save(self, *args, **kwargs):
    ml_model = joblib.load('ml_model/ml_Mortalité_précoce_model.joblib')
    self.predictions = ml_model.predict([[self.sex, self.age, self.nombre_de_personnes]])
    return super().save(*args, **kwargs)

class Meta:
    ordering = ['-date']

def __str__(self):
    return self.name
