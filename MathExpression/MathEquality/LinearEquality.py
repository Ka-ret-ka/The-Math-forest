from MathExpression.MathRelation import MathRelation
import sympy



class LinearEquality(MathRelation):
    """Класс решения псевдо-линейных уравнений."""

    def solving_linear_equation(self):
        """Решение линейного уравнения."""

        if self.left_side != sympy.powsimp(self.left_side) or self.right_side != sympy.powsimp(self.right_side):
            self.reduction()
            self.app_stage("Сокращаем обе стороны")

        if self.right_side.subs(self.var, 0) != self.right_side:
            self.left_side = sympy.powsimp(self.left_side - (self.right_side - self.right_side.subs(self.var, 0)))
            self.right_side = self.right_side.subs(self.var, 0)
            self.app_stage(f"Переносим члены, содержащие переменную {self.var}, влево")

        if self.left_side.subs(self.var, 0) != 0:
            self.right_side = sympy.powsimp(self.right_side - self.left_side.subs(self.var, 0))
            self.left_side = sympy.powsimp(self.left_side - self.left_side.subs(self.var, 0))
            self.app_stage(f"Переносим члены, не содержащие переменную {self.var}, вправо")

        divisor = self.left_side.subs(self.var, 1)
        if divisor != 1:
            self.right_side /= divisor
            self.left_side /= divisor
            self.app_stage(f"Делим обе стороны на {divisor}")

        return [self.right_side]

