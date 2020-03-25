# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    c = a.to_i(2)
    (a.to_i(2) + b.to_i(2)).to_s(2)

    ans = ''
    a.reverse!
    b.reverse!
    temp = 0
    (0...[a.length, b.length].max).each do |i|
        first = i < a.length ? a[i].to_i : 0
        second = i < b.length ? b[i].to_i : 0
        result = first + second + temp
        ans = ans + (result % 2).to_s
        temp = result / 2
    end
    if temp != 0
        ans = ans + temp.to_s
    end
    return ans.reverse
end

puts add_binary "1010", "1011"