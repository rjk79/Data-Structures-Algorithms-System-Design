def validate_stack_sequences(pushed, popped)
    stack = []
#   if we run out of one or the other we should be able to make a decision
    until popped.empty? 

        # always take from popped if u need to and can
        until stack.last == popped.first || pushed.empty?
            stack << pushed.shift
        end

        # just keep going, if theres ever a mismatch return false
        if stack.last != popped.first
            return false
        end

        stack.pop
        popped.shift
    end

    return true
end

# puts validate_stack_sequences([1,2,3,4,5], [4,3,5,1,2])
puts validate_stack_sequences([1,2,3,4,5], [4,5,3,2,1])