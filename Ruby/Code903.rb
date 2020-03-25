# @param {String} s
# @return {Integer}
def num_perms_di_sequence(s)
    $s = s
    $nums = Array.new(s.length != 0 ? s.length + 1 : 0) { |i| i }
    $ans = 0
    def nextNum(sequence)
        if $nums.length == 0
            puts sequence.to_s
            $ans += 1
        else
            $nums.each_with_index do |num, index|
                if sequence.length == 0 || ($s[sequence.length - 1] == 'D' and sequence[-1] > num) || ($s[sequence.length - 1] == 'I' and sequence[-1] < num)
                    $nums.delete_at(index)
                    sequence.push(num)
                    nextNum(sequence)
                    sequence.pop()
                    $nums.insert(index, num)
                end
            end
        end
    end
    nextNum([])
    $ans
end

puts num_perms_di_sequence "IDDDIIDIIIIIIIIDIDID"