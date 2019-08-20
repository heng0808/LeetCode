# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
	str_list=s.split('')
	temp_count=num_rows-2
	full_col_count=s.length
	node_list=[]
	begin_col=true
	str_list.each_with_index do |value, index|
		if begin_col

		else
			c_index=index-node_list.length
		end
	end
end

class Node
	@row=0
	@col=0
	def initialize(row, col)
		@row=row
		@col=col
	end
end



# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 0 1 2 3 4 5 6
# L     D     R 0  0     6       12
# E   O E   I I 1  1   5 7    11 13
# E C   I H   N 2  2 4   8 10    14
# T     S     G 3  3     9       15
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。