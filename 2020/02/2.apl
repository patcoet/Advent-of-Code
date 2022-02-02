input←⎕NGET 'C:\Users\salts\Documents\GitHub\Advent-of-Code\2020\02\input.txt'
lines←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input
nums←{⍎¨'-'(≠⊆⊢)1⊃' '(≠⊆⊢)⍵}
letter←{1⊃2⊃' '(≠⊆⊢)⍵}
password←{3⊃' '(≠⊆⊢)⍵}
valid←{((letter ⍵)=((1⊃nums ⍵)⊃password ⍵))≢((letter ⍵)=((2⊃nums ⍵)⊃password ⍵))}
+/valid¨lines