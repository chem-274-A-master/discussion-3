# Integration Objects Discussion Guide

## Class Design

The students should identify the information needed to perform the integration:
* Lower and upper bounds of integration
* Number of intervals
* The function to be integrated
   
Some things they might consider when writing their class
* Where should these be stored? (As attributes in the constructor)
* Should we calculate and store the step size? (Yes, as self.dx)
* Should the function be a method of the class?
* Should the result be stored as an attribute or returned? If it's stored, how should it be initialized?
     * Storing as an attribute allows for later access without recomputation
     * It separates the computation from the retrieval of the result
     * Consider initializing result to `None` in the constructor

Here is a sample implementation where the result is stored as an attribute and the function to integrate is a method of the class:

```python
class MidpointIntegrator:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.dx = (self.b - self.a) / self.n
        self.result = None
    
    def function(self, x):
        return 1 / (1 + x**2)
    
    def integrate(self):
        total = 0
        for i in range(self.n):
            mid = self.a + (i + 0.5) * self.dx
            total += self.function(mid)
        self.result = total * self.dx

integrator = MidpointIntegrator(0, 1, 1000)
integrator.integrate()
print(f"The result of the integration is: {integrator.result}")
```
## Extending to Other Methods

If we used inheritance we could define a base class with a common constructor and method for the function to integrate. Then, we could create subclasses for each integration method.

```python
class BaseIntegrator:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.dx = (self.b - self.a) / self.n
        self.result = None
    
    def function(self, x):
        return 1 / (1 + x**2)

    def integrate(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class MidpointIntegrator(BaseIntegrator):
    def integrate(self):
        total = 0
        for i in range(self.n):
            mid = self.a + (i + 0.5) * self.dx
            total += self.function(mid)
        self.result = total * self.dx

class TrapezoidalIntegrator(BaseIntegrator):
    def integrate(self):
        total = 0.5 * (self.function(self.a) + self.function(self.b))
        for i in range(1, self.n):
            x = self.a + i * self.dx
            total += self.function(x)
        self.result = total * self.dx

# Usage
midpoint = MidpointIntegrator(0, 1, 1000)
trapezoidal = TrapezoidalIntegrator(0, 1, 1000)

midpoint.integrate()
trapezoidal.integrate()

print(f"Midpoint result: {midpoint.result}")
print(f"Trapezoidal result: {trapezoidal.result}")
```

- Discuss:
* What's shared in the base class and why?
* How does this design support adding new integration methods?
* What are the limitations of this approach?

## First-class Functions
Here is an example where the function to integrate is passed as an argument to the integration method.

In our previous examples, the function to integrate was a method of the class. However, we can also pass the function as an argument to the `integrate` method. This is known as a first-class function.

In our class design with inheritance, we can update all the integrators to accept a function as an argument by updating the base class constructor.

```python
class BaseIntegrator:
    def __init__(self, func, a, b, n):
        self.function = func  # Accept a function as a parameter
        self.a = a
        self.b = b
        self.n = n
        self.dx = (self.b - self.a) / self.n
        self.result = None

    def integrate(self):
        raise NotImplementedError("Subclasses must implement this method")
```
