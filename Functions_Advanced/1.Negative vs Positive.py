def what_is_sums(*args):
    negative = 0
    positive = 0

    for el in args:
        if el < 0:
            negative += el
        else:
            positive += el

    return negative, positive


nums = [int(x) for x in input().split(" ")]
negative_sum, positive_sum = what_is_sums(*nums)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
