from django.db import models
from django.utils import timezone
from move_app.models import Move

# import built-in Django Validators
from django.core import validators as v

# import validate_name from our custom validators
from .validators import validate_name


# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(
        max_length=200, unique=True, blank=False, null=False, validators=[validate_name]
    )
    # IntegerField will allow only solid numerical values as input
    level = models.IntegerField(
        default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)]
    )
    # We are providing a default to someone born Jan 1st 2008
    date_encountered = models.DateField(default="2008-01-01")
    # If a value is not provided we are stating the last time this pokemon was at school was upon creation of the classes instance.
    date_captured = models.DateTimeField(default=timezone.now)
    # If no value is provided the Pokemon description will be "Unknown"
    description = models.TextField(
        default="Unknown",
        validators=[v.MinLengthValidator(7), v.MaxLengthValidator(150)],
    )
    # We must catch them all.
    captured = models.BooleanField(default=False)
    moves = models.ManyToManyField(Move, related_name="pokemon")

    # trainer = models.ForeignKey()
    # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self):
        self.level += 1
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self):
        self.captured = not self.captured
        self.save()
