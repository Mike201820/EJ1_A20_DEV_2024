from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ChessProblem
from .serializers import ChessProblemSerializer
import json

class ChessProblemViewSet(viewsets.ModelViewSet):
    queryset = ChessProblem.objects.all()
    serializer_class = ChessProblemSerializer

    def queens_attack(self, n, k, rq, cq, obstacles):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        attackable_squares = 0
        obstacles = set((r, c) for r, c in obstacles)

        for dr, dc in directions:
            r, c = rq, cq
            while 1 <= r + dr <= n and 1 <= c + dc <= n:
                r += dr
                c += dc
                if (r, c) in obstacles:
                    break
                attackable_squares += 1

        return attackable_squares

    @action(detail=True, methods=['post'])
    def calculate(self, request, pk=None):
        problem = self.get_object()
        n = problem.n
        k = problem.k
        rq = problem.rq
        cq = problem.cq
        obstacles = json.loads(problem.obstacles)

        result = self.queens_attack(n, k, rq, cq, obstacles)
        problem.result = result
        problem.save()

        return Response({'result': result})
