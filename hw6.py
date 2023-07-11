def is_decreasing(seq):
    if len(seq) < 2:
        return True

    for itr in range(len(seq) - 1):
        if seq[itr] <= seq[itr + 1]:
            return False

    return True
print(is_decreasing([1,2,3]))