⍝ ⎕NGET returns a vector of length 3, where element 1 is the contents of the file, 2 is the encoding used, and 3 is the first newline character detected.
⍝ input←A assigns A to the variable input.
⍝ 1⊂A is element 1 of A.
⍝ ⎕UCS takes the number of a Unicode code point and returns the corresponding Unicode character. 3⊃input is the code point of the newline character the file is using, so ⎕UCS 3⊃input is a newline.
⍝ Given two vectors of the same length A and B, A≠B returns a vector of comparisons between the elements of A and B, so 1 2 3≠1 4 3 returns 0 1 0.
⍝ A⊢B just returns B. We can't just write B here because that would make the functions be applied differently.
⍝ A⊆B splits B up into sub-vectors, with a new one wherever a value of A is greater than the previous one and 0s dropped. 1 1 0 2 3 ⊆ 'hello' returns 'he' 'l' 'o'.
⍝ A(≠⊆⊢)B gets applied as (A≠B)⊆(A⊢B).
⍝ So, we have basically '\n'(≠⊆⊢)input, which is ('\n'≠input)⊆('\n'⊢input). '\n'≠input turns '3478\n487\n1283' into 1 1 1 1 0 1 1 1 0 1 1 1 1. We then partition the input by that to get a vector like '3478' '487' '1283'.
⍝ ¨ is a map; it applies the left function to each element of the right vector.
⍝ ⍎ is eval; ⍎'123' returns 123. This mapped to our vector of strings turns it into a vector of numbers that we can do math on.
input←⍎¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\01\input'

⍝ input,0 appends 0 to input.
⍝ 1↓input,0 drops the first element of the input, so 3 6 2 becomes 6 2 0.
⍝ A-B returns a vector of the differences of the elements of A and B, so 6 2 0 - 3 6 2 returns 3 ¯4 ¯2.
⍝ ¯1↓A drops the last element of A, so 3 ¯4 2 becomes 3 ¯4.
⍝ Curly braces are lambdas, and ⍵ is the right-side input. Mapping "x > 0" to 3 ¯4, we get 1 0.
⍝ / is a fold; it takes the function to the left and applies it to each element of the vector to the right. If A is a vector of numbers, +/A is the sum of the numbers.
+/{⍵>0}¨¯1↓(1↓input,0)-input