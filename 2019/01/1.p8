pico-8 cartridge // http://www.pico-8.com
version 33
__lua__
function num(str)
	digits = {}
 for i=1, #str do
 	digits[#str - i + 1] = tonum(sub(str, i, i))
 end
	return digits
end

function n(a)
	s = ""
	for i = 0, #a do
		s = (a[i] or "") .. s
	end
	return s
end

function plus(a, b)
 r = {}
 for i=1, max(#a, #b) do
  ai = a[i] or 0
  bi = b[i] or 0
  r[i] = ai + bi
 end
 
 for i=1, #r do
 	if r[i] > 9 then
 		r[i+1] = (r[i+1] or 0) + 1
 		r[i] = r[i] % 10
 	end
 end
 
 return r
end

function mul(a, b)
	tmp = num("0")
	for i = 1, tonum(n(b)) do
		tmp = plus(tmp, a)
	end
	return tmp
end

function _add(a, b)
 return n(plus(num(a), num(b)))
end

function _mul(a, b)
	return n(mul(num(a), num(b)))
end

function minus(a, b)
	r = {}
 for i=1, max(#a, #b) do
  ai = a[i] or 0
  bi = b[i] or 0
  r[i] = ai - bi
 end
 
 for i=1, #r do
 	if r[i] < 0 then
 		r[i+1] = (r[i+1] or 0) - 1
 		r[i] = 10 + r[i]
		end
 end
 
 return r
end

function _sub(a, b)
 return n(minus(num(a), num(b)))
end

function div(a, b)
	acc = num("0")
	while not lt(a, num("0")) do
		a = minus(a, b)
		acc = plus(acc, num("1"))
	end
	return minus(acc, num("1"))
end

function _div(a, b)
 return n(div(num(a), num(b)))
end

function lt(a, b)
 return sub(n(minus(a, b)), 1, 1) == "-"
end

function req(mass)
	return n(minus(div(num(mass), num("3")), num("2")))
end

#include input_.txt

input = split(input, "\n", false)

sum = num("0")
for i = 1, #input do
	ii = input[i]
	?"mass: " .. ii
	ri = req(ii)
	?"fuel: " .. ri
	sum = plus(num(ri), sum)
	?"sum:  " .. n(sum)
	?""
end
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
