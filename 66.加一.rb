# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
    if digits.length > 0
        digits[-1] += 1
    end
    (digits.length - 1).step(0, -1) do |i|
        if i != 0
            digits[i - 1] += digits[i] / 10
            digits[i] = digits[i] % 10
        else
            if digits[i] > 9
                digits.insert(0, digits[i] / 10)
                digits[1] = digits[1] % 10
            end
        end
    end
    return digits
end

plus_one([9,9,9])