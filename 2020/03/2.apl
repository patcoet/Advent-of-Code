input←⎕NGET 'C:\Users\salts\Documents\GitHub\Advent-of-Code\2020\03\input.txt'
parsed←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input
r1d1←+/'#'={(1⊃⍵){⍺⊃⍵⊃(1×⍴parsed)⍴¨parsed}(2⊃⍵)}¨({1+1×⍵-1}¨⍳⍴parsed),¨⍳⍴parsed
r1d3←+/'#'={(1⊃⍵){⍺⊃⍵⊃(3×⍴parsed)⍴¨parsed}(2⊃⍵)}¨({1+3×⍵-1}¨⍳⍴parsed),¨⍳⍴parsed
r1d5←+/'#'={(1⊃⍵){⍺⊃⍵⊃(5×⍴parsed)⍴¨parsed}(2⊃⍵)}¨({1+5×⍵-1}¨⍳⍴parsed),¨⍳⍴parsed
r1d7←+/'#'={(1⊃⍵){⍺⊃⍵⊃(7×⍴parsed)⍴¨parsed}(2⊃⍵)}¨({1+7×⍵-1}¨⍳⍴parsed),¨⍳⍴parsed
r1d2←+/'#'={(1⊃⍵){⍺⊃⍵⊃(2×⍴parsed)⍴¨parsed}(2⊃⍵)}¨(⍳⍴(2|⍳⍴parsed)⊆⍳⍴parsed),¨(2|⍳⍴parsed)⊆⍳⍴parsed
r1d1×r1d3×r1d5×r1d7×r1d2