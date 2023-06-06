import math
from django.http import JsonResponse
from . models import Equation


def result(request):
    if request.method == 'GET':
        """Getting variables from url."""
        a = float(request.GET.get("a"))
        b = float(request.GET.get("b"))
        c = float(request.GET.get("c"))

        """Calculating roots."""
        d = b**2 - 4 * a * c

        if d < 0:
            """Creating json object."""
            Equation.objects.create(a=a, b=b, c=c, root1=None, root2=None)
            return JsonResponse("No roots for quadratic"
                                f" equation {a} * x^2 + {b} * x + {c} = 0",
                                safe=False)
        elif d == 0:
            root = -b / 2 * a
            Equation.objects.create(a=a, b=b, c=c, root1=root, root2=None)
            return JsonResponse(f"One root: {root} for quadratic "
                                f"equation {a} * x^2 + {b} * x + {c} = 0",
                                safe=False)
        else:
            root1 = (-b + math.sqrt(d)) / 2 * a
            root2 = (-b - math.sqrt(d)) / 2 * a
            Equation.obgects.cteate(a=a, b=b, c=c, root1=root1, root2=root2)
            return JsonResponse(f"Two roots: {root1}, {root2} for quadratic"
                                f" equation {a} * x^2 + {b} * x + {c} = 0",
                                safe=False)
    else:
        return JsonResponse("Invalid method!")
