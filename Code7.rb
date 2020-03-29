# @param {Integer} x
# @return {Integer}
def reverse(x)
	num=x.abs
	num_str=num.to_s
	num_str=num_str.reverse
	result= x>0 ? num_str.to_i : 0-num_str.to_i
	if result>=-2**31 && result<=2**31-1
		return result
	end
	return 0
end

puts reverse -120