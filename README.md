# MCP Student Sandbox

## Module: mystery_module.py

This repository includes a small utility function in `mystery_module.py` for solving quadratic equations using the quadratic formula.

### Function: `fn_x(a, b, c)`

Calculates the roots of a quadratic equation `ax^2 + bx + c = 0`.

- `a` (float or int): coefficient of `x^2` (must be non-zero for meaningful quadratic equation)
- `b` (float or int): coefficient of `x`
- `c` (float or int): constant term

Returns:
- `tuple[float, float]` containing the two real roots `(x1, x2)` when discriminant `b^2 - 4ac >= 0`
- `None` when discriminant < 0 (there are no real roots)

Behavior:
- Computes `d = b^2 - 4*a*c` (the discriminant)
- If `d < 0`: returns `None`
- Else: returns a tuple of two solutions:
  - `(-b + sqrt(d)) / (2*a)`
  - `(-b - sqrt(d)) / (2*a)`

Notes:
- If `a == 0`, this function performs division by zero. Callers should validate or handle this case.

## Usage Examples

```python
from mystery_module import fn_x

# Example 1: two real roots
roots = fn_x(1, -3, 2)
print(roots)  # (2.0, 1.0)

# Example 2: one repeated real root
roots = fn_x(1, 2, 1)
print(roots)  # (-1.0, -1.0)

# Example 3: no real roots
roots = fn_x(1, 0, 1)
print(roots)  # None
```

## Repository files
- `mystery_module.py` - quadratic formula utility
- `failing_calculator.py` - average ratio calculator (fix/bug in current branch)
- `spaghetti_logic.py` - sample data-processing code (refactored)
- `secret_leak.py` - hardcoded secret example (security risk)

## Security note
`secret_leak.py` contains a hardcoded AWS key pattern; do not commit real secrets.
