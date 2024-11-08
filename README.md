a quick implementation to encode 64bit unsigned integers into protocol buffers varint encoding. 

(didn't end up spending time to refactor, this is just the first implementation, could be alot of improvements, especially in the split_into_groups function. and overall the most efficient way is to use bitwise operations)
