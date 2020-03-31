# @param {String} s
# @return {String}
def longest_palindrome(s)
	str_list=['#']
	strs=s.split('')
	strs.each do |value|
		str_list.push value
		str_list.push "#"
	end
	max_l=3
	max_l_i=1
	str_list.each_index do |index|
		length=palindrome_length str_list,index
		if length>max_l
			max_l=length
			max_l_i=index
		end
	end
	left_index=max_l_i-(max_l-1)/2
	right_index=max_l_i+(max_l-1)/2
	palindrome=''
	str_list.each_with_index do |value,index|
		if index>=left_index&&index<=right_index&&value!='#'
			palindrome=palindrome+value
		end
	end
	return palindrome
end

def palindrome_length(s_list, index)
	step=0
	while index-step-1 >= 0 and index+step+1  < s_list.length and s_list[index-step-1] == s_list[index+step+1]
		step=step+1
	end
	return step*2+1
end

puts longest_palindrome('babab')
puts longest_palindrome('babbac')