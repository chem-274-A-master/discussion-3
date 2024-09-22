# Discussion Section - Week 5

## Working Together
For this discussion, we'd like for each group to try out a VSCode feature called "Live Share." Install [this extension](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) in your VSCode editor by clicking the "Install" button on the linked page.

One person in your group should then create a Live Share link following the [Quickstart Instructions](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) to share with the group. Please work collaboratively on the exercises in this discussion using Live Share. **Add your Liveshare link to the class Google Slides on the page for your group.**

## Programming Topics

The programming topic of the exercises for this week's discussion are C++ references (again), and revisiting Python class design.

To complete this discussion session, your group should complete the programming tasks and answer the questions in the class Google Slide presentation.
These tasks are meant to be collaborative, so work together to ensure that all group members understand the code.

## C++ References

References can be tricky for new C++ programmers, but they are a powerful tool for ensuring data is not copied unnecessarily, which is requried for good performance.
In general, references and pointers allow for fine-grained control over "aliasing", which is the general concept of multiple variables referring
to the same location in memory. That is, if two variables are aliased, then changes to the value of one variable will be reflected in the other.

```c++
double a = 10;
double & b = a; // b and a are aliased
```

When declaring arguments to a function, declaring a parameter as a reference will alias that paramter to what is passed in. If not declared as
a reference, the value of the variable will be copied instead and the variable will not be aliased.

```c++

void f(double & d)
{...}

int main(void)
{
  double x = 1.0;
  f(x);  // x (here) and d (inside function) are aliased
}
```

The same is true for returning from a function.

### Exercise

Consider the following code snippets. Which variables are aliased? Put your answers with justification in the class Google Slides presentation.

1. ```c++
   int f(int i)
   {
     i += 1;
     return i;
   }
   
   int main(void)
   {
     int j = 4;
     int k = f(j);
   }
   ```

1. ```c++
   double f(const double & d)
   {
     return 2.0*d;
   }
   
   int main(void)
   {
     double m = 9.123;
     double m2 = f(m);
   }
   ```

1. ```c++
   double & f(double & q)
   {
     q = 3.14*q;
     return q;
   }
   
   int main(void)
   {
     double a = 7.9471;
     double b = f(a);
   }
   ```

1. ```c++
   double & f(double & q)
   {
     q = 3.14*q;
     return q;
   }
  
   int main(void)
   {
     double a = 7.9471;
     double & b = f(a);
   }
   ```


1. ```c++
   void f(std::vector<double> v)
   {
     v[0] = 3.14*v[0];
   }
   
   int main(void)
   {
     std::vector<double> my_vec{1.0, 2.0, 3.0};
     f(my_vec);
   }
   ```

1. ```c++
   double & f(std::vector<double> & v)
   {
     v[0] = 3.14*v[0];
     return v[0];
   }
   
   int main(void)
   {
     std::vector<double> my_vec{1.0, 2.0, 3.0};
     double & b = f(my_vec);
   }
   ```

## Python Object Practice - Integration Objects with Inheritance

### Python - Integration Objects

In Chem 280, you wrote C++ code for evaluating an integral using the [midpoint rule](https://msse-chem-280-2024.github.io/day6/group-assignment.html#coding-assignment). 
Now, you're going to expand on that concept using Python and object-oriented programming.

#### Step 1: Class Design
With your group, discuss how you would design a Python class to perform integration using the midpoint rule. Think about the following:

- What should go into the constructor?
- What attributes will the class need?
- What methods will the class need?

Once you've designed the class, write it out in Python.

#### Step 2: Extending to Other Integration Methods
After implementing your midpoint rule integrator, consider the following questions:

- What if you wanted to implement other integration techniques, like the trapezoidal rule or Simpson’s rule? How would you modify your class to accommodate these methods?
- Does it make sense to use inheritance in this case? Why or why not?
- What benefits or challenges might arise from designing a class hierarchy with a base integrator class and specific subclasses for each method?

Discuss these questions with your group, and modify your design accordingly. You can implement multiple integrators if you'd like to explore this idea further.

#### Step 3: First-class Functions
In Python, functions are [first-class citizens](https://en.wikipedia.org/wiki/First-class_citizen), meaning they can be passed to and returned from object methods/functions. Review the file `first_class_functions.py` and write a short explanation of how it works in your README. 

Once you've done that, modify your integrator class to take a function as an argument and use it to evaluate the integral.

### Questions
Answer the following questions:

1. How did you design your class for implementing the Riemann sum? What does the constructor take, what are the instance attributes, and what are the methods?
2. What considerations did you make when deciding whether or not to use inheritance for multiple integration methods?
3. What is function passing, and what advantages does it provide in the context of your integrator class?


