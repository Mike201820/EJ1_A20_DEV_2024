from django.db import models

class ChessProblem(models.Model):
    n = models.IntegerField()
    k = models.IntegerField()
    rq = models.IntegerField()
    cq = models.IntegerField()
    obstacles = models.TextField()  # Almacenar los obstáculos como texto JSON
    result = models.IntegerField(null=True, blank=True)  # Resultado del cálculo

    def __str__(self):
        return f"ChessProblem {self.id}"
