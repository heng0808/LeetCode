# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, _target)
  nums.each_with_index do |_num, index|
    nums_left = nums[index + 1...:nums.length - 1]
    return [index, nums.find]
  end
end

result = two_sum([3, 3], 6)
puts result
