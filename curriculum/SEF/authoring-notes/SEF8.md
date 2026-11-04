# SEF8 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** Mathematics supplies the exact language of computing and the foundation of machine learning. This course teaches the parts that later courses rely on and applies each one in code.
- **History:** Boole's algebra of logic dates from the 1840s, Cayley formalized matrices in 1858, Newton and Leibniz developed calculus in the seventeenth century, and Bayes' theorem was published in 1763.
- **Usage:** The learner implements each idea without libraries first, then verifies the result against a scientific library.
- **Applications:** Algorithm analysis, graphics, data science, cryptography, and machine learning.
- **Strengths:** Exact definitions allow exact reasoning and results that can be checked.
- **Limitations:** Models simplify reality, numerical computation introduces rounding error, and mathematical correctness does not guarantee that software behaves as intended.
- **Key concepts:** proposition; set; function; counting; vector; matrix; probability; distribution; derivative; gradient; Big-O

## Module 1 — Logic, Sets & Discrete Reasoning

- **Introduction:** Discrete mathematics is the language of correctness and counting. This module covers logic, sets, functions, and counting.
- **Overview:** It covers propositional logic, quantifiers, sets, functions, counting rules, permutations, and combinations.
- **History:** George Boole formalized logic in the 1840s and 1850s, and Georg Cantor developed set theory in the 1870s.
- **Key concepts:** proposition; quantifier; set; function; counting rule; permutation; combination

## Module 2 — Vectors & Matrices

- **Introduction:** Data, images, graphics, and models are arrays of numbers. Linear algebra gives rules for working with them.
- **Overview:** It covers vectors, norms and distance, dot products, angles, matrices, matrix multiplication, and linear systems.
- **History:** Arthur Cayley formalized matrices in 1858, and Gauss's elimination method for linear systems is older still.
- **Limitations:** Numerical error accumulates, and large matrices use a lot of memory and computation.
- **Key concepts:** vector; norm; dot product; angle; matrix; matrix multiplication; linear system

## Module 3 — Probability & Statistics

- **Introduction:** Uncertainty is everywhere in software, from random inputs to measurement error. Probability gives rules for reasoning about it.
- **Overview:** It covers probability spaces, conditional probability, independence, Bayes' theorem, distributions, expected value, variance, and descriptive statistics.
- **History:** Bayes' theorem was published posthumously in 1763 from the work of Thomas Bayes, and Pierre-Simon Laplace developed it further.
- **Limitations:** Results depend on model assumptions, and conditional probabilities are often misread.
- **Key concepts:** probability; conditional probability; independence; Bayes' theorem; distribution; expected value; variance

## Module 4 — Derivatives, Gradients & Complexity

- **Introduction:** Change and growth are central to optimization and performance. This module covers derivatives, gradients, and the growth of functions.
- **Overview:** It covers derivatives, numerical derivatives, partial derivatives, gradients, the growth of functions, and algorithm complexity.
- **History:** Newton and Leibniz developed calculus in the late seventeenth century, and Augustin-Louis Cauchy proposed gradient descent in 1847.
- **Limitations:** A gradient gives only local information, and numerical differentiation is sensitive to step size.
- **Key concepts:** derivative; partial derivative; gradient; numerical approximation; growth rate; Big-O

## Module 5 — Numerical Computing Notebook

- **Introduction:** This lab integrates the course. The learner builds numerical functions from first principles and verifies them against a scientific library.
- **Overview:** It combines vector and matrix operations, probability simulation, and derivative checking in one notebook.
- **Applications:** Graphics, data science, and machine learning all run on these operations.
- **Key concepts integrated:** vectors; matrices; probability; simulation; derivatives; verification

1. **Numerical Computing Notebook**
   - kind: `lab`

## Original topic inventory

- Logic and sets
- Functions
- Combinatorics
- Vectors
- Matrices
- Dot products
- Probability
- Conditional probability
- Bayes' rule
- Descriptive statistics
- Derivatives
- Gradients
- Big-O notation
