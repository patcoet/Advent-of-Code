⍝ input←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\05\input'
⍝ nums←⍎¨¨{1 0 1/⍵}¨' '(≠⊆⊢)¨input
⍝ to←{((⍺⌊⍵)-1)+(⍳1+|⍺-⍵)}
⍝ to2←{x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵⋄len←(⍴x1 to x2)⌈(⍴y1 to y2) ⋄ (x1≠x2)∧(y1≠y2):⍬ ⋄ (len⍴x1 to x2),¨(len⍴y1 to y2)}
⍝ coords←⊃,/{(⊃⍵)to2(2⊃⍵)}¨nums
⍝ counts←{a←⊃⍵⋄n←+/(⊂a)⍷⍵⋄ns←⍺+1<n ⋄ 0=⍴⍵:ns ⋄ ns∇⍵~⊂a}
⍝ 0 counts coords

input←(⎕UCS 3⊃input)(≠⊆⊢)1⊃input←⎕NGET 'Z:\projects\Advent-of-Code\2021\05\input'
nums←⍎¨¨{1 0 1/⍵}¨' '(≠⊆⊢)¨input
alwi←{(⊃⍵){x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵ ⋄ (x1=x2)∨(y1=y2)}(2⊃⍵)}
fnums←(alwi¨nums)/nums
to←{((⍺⌊⍵)-1)+(⍳1+|⍺-⍵)}
to2←{x1←⊃⍺⋄x2←⊃⍵⋄y1←2⊃⍺⋄y2←2⊃⍵⋄len←(⍴x1 to x2)⌈(⍴y1 to y2) ⋄ (len⍴x1 to x2),¨(len⍴y1 to y2)}
coords←⊃,/{(⊃⍵)to2(2⊃⍵)}¨fnums

xmax←{1+⌈/⊃,/⊃¨¨⍵}
ymax←{1+⌈/⊃,/2⊃¨¨⍵}
board←(xmax nums) (ymax nums)⍴0
+/+/2≤coords{0=⍴⍺:⍵ ⋄ (1↓⍺)∇(({1+⍵}@(1+⊃⍺)(1+⊃⍺))⍵)}board