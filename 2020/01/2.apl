input←⎕NGET 'Z:\projects\Advent-of-Code\2020\01\input.txt'
nums←⍎¨(⎕UCS 10)(≠⊆⊢)1⊃input
sums←{(⍵⊃nums)+nums}¨⍳⍴nums
sums2←{(⍵⊃nums)+¨sums}¨⍳⍴nums
i1←((1∊¨{⍵∊¨(sums2⍳¨¨2020)}¨⍳⍴nums)⍳1)
i←i1,((i1⊃(sums2⍳¨¨2020))~(⍴nums)+1)
×/{(⍵⊃i)⊃nums}¨⍳3