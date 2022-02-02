input←⎕NGET 'Z:\projects\Advent-of-Code\2020\03\input.txt'
parsed←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input
+/'#'={(1⊃⍵){⍺⊃⍵⊃(3×⍴parsed)⍴¨parsed}(2⊃⍵)}¨({1+3×⍵-1}¨⍳⍴parsed),¨⍳⍴parsed
