⍝ Read and parse input as in part 1.
input←⍎¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\01\input'

⍝ input,1↓input,0,2↓input,0 0 turns 3 7 1 2 5 into 3 7 1 2 5 7 1 2 5 0 1 2 5 0 0.
⍝ ⍴A returns the length of the vector A, so 3,⍴input is 3 (length of input).
⍝ A⍴B reshapes B, so 5 2⍴B turns B into a matrix of 5 rows and 2 columns, either just taking the first 10 elements of B or repeating B if it doesn't have length 10. We end up with a matrix where the first row is our input, the second row is our input shifted one step left with a 0 appended, and the third two steps and 0s.
⍝ f⌿A where f is a function and A is a matrix folds f over each column of A, so +⌿A is a vector of the sums of A's columns. In our case, this means it's our list of three-measurement windows, with two junk elements at the end that we chop off.
threes←¯2↓+⌿(3,⍴input)⍴input,1↓input,0,2↓input,0 0

⍝ Count increases as in part 1.
+/⊃{⍵>0}⊆¯1↓(1↓threes,0)-threes