input←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\05\test'
nums←⍎¨¨{1 0 1/⍵}¨' '(≠⊆⊢)¨input

to←{x←((⍺⌊⍵)-1)+(⍳1+|⍺-⍵) ⋄ ⍺>⍵:⌽x ⋄ x}
to2←{x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵⋄len←(⍴x1 to x2)⌈(⍴y1 to y2) ⋄ (len⍴x1 to x2),¨(len⍴y1 to y2)}

alwi←{(⊃⍵){x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵ ⋄ (x1=x2)∨(y1=y2)}(2⊃⍵)}
isdiag←{(⊃⍵){x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵ ⋄ (⍴x1 to x2)=(⍴y1 to y2)}(2⊃⍵)}
fnums←({(alwi ⍵)∨(⊃,/isdiag ⍵)}¨nums)/nums

coords←⊃,/{(⊃⍵)to2(2⊃⍵)}¨fnums

xmax←{1+⌈/⊃,/⊃¨¨⍵}
ymax←{1+⌈/⊃,/2⊃¨¨⍵}
board←(xmax nums) (ymax nums)⍴0
+/+/2≤¨¨coords{0=⍴⍺:⍵ ⋄ (1↓⍺)∇(({1+⍵}@(1+⊃⍺)(1+⊃⍺))⍵)}board