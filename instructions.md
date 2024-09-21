# Discussion Section - Week 5

## Working Together
For this discussion, we'd like for each group to try out a VSCode feature called "Live Share." Install [this extension](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) in your VSCode editor by clicking the "Install" button on the linked page.

One person in your group should then create a Live Share link following the [Quickstart Instructions](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) to share with the group. Please work collaboratively on the exercises in this discussion using Live Share. **Add your Liveshare link to the class Google Slides on the page for your group.**

## Programming Topics

The programming topic of the exercises for this week's discussion are function passing and comprehensions. 
Comprehensions are special syntaxes available in Python for working with lists and creating new sequences or dictionaries. 

To complete this discussion session, your group should complete the programming tasks and answer the questions in the instructions in a markdown file. 
These tasks are meant to be collaborative, so work together to ensure that all group members understand the code.

## Comprehensions
Comprehensions are constructs in Python that will often let you avoid writing for loops.

In general, a comprehension is written

```python

[x for x in iterable]
```

The example above would be a "list comprehension" because it produces a list. You can also produce sets through "set comprehension."

```python
{x for x in iterable}
```

Dictionary comprehensions need two values, separated by a colon:

```python
{k:v for x in iterable}
```

See the examples in `main.py`, then complete the following tasks.

For completing the tasks, program together in your groups. If you divide the tasks, you need to regroup to discuss the final code for each task as a group. 

## Tasks

For each task, write a version which doesn't use comprehension and a version that uses comprehensions. 
Create a new file called "exercises.py" and add these exercises. 
Label each one.
For each exercise, also add a check that confirms that the calculated values are the same with and without comprehensions.

There is a file `data.py` which contains the Gibbs Free Energy of formation for a collection of substances. 
The list `deltaG` contains the values of the Gibbs Free Energy, and the list `substances` contains the chemical formula for the substances.

1. Using the list `deltaG` from `data.py`, create a list containing the values representing a spontaneous reactions. (You'll have to know some chemistry here! What is the condition of delta G for a spontaneous reaction?)

1. Using the list `substances` from `data.py` create a set containing the substances that contain alumnium. 

1. Using `deltaG` and `substances` from `data.py` create a dictionary where the keys are substance names and the values are the associated values of `deltaG`.

1. **Challenge** (optional) - Use dictionary comprehension and the dictionary you created in the previous step to create a dictionary where you have only spontaneous values.

## Wrap up
1. Comprehensions are a nice feature of Python, and some people really like to use them. However, you should always aim for **code clarity** (easy for others to read) over using the "fanciest" syntax. Comprehensions will be appropriate in some, but not all tasks. If you are ever confused by comprehensions, you can just choose to write a loop.

Each group member should reflect on the exercises. Do you prefer using comprehensions for loops? Do you think using comprehensions is easier or harder to read?

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
Answer the following questions in your README:

1. How did you design your class for implementing the Riemann sum? What does the constructor take, what are the instance attributes, and what are the methods?
2. What considerations did you make when deciding whether or not to use inheritance for multiple integration methods?
3. What is function passing, and what advantages does it provide in the context of your integrator class?

