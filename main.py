from MathExpression import *

# y = MathExpression('2*x - 3 = x*(3*5 - 7)', 'x')
y = MathExpression('2*x^2-4*x+5 = 0', 'x')
y.solving_expression()
y.print_stages()
print()
y.print_answer()
