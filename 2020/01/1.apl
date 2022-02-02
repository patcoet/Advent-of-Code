input←⎕NGET 'Z:\projects\Advent-of-Code\2020\01\input.txt'
nums←⍎¨(⎕UCS 10)(≠⊆⊢)1⊃input
sums←{(⍵⊃nums)+nums}¨⍳⍴nums
i1←(2020∊¨sums)⍳1
i2←(i1⊃sums)⍳2020
result←(i1⊃nums)×(i2⊃nums)
result
