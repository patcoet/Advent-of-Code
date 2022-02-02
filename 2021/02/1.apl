input←{(⊃⊃⍵) (⍎2⊃⍵)}¨' '(≠⊆⊢)¨(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\02\input'
n←{x←⍵⋄+/2⊃¨({x=⊃⍵}¨input)/input}
(n'f')×(n'd')-(n'u')