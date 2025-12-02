
class TestCounter:
    count = 0

    def __init__(self):
        TestCounter.count +=1

#Each time an object is created, count increases.
# count is shared across all objects.

t1 = TestCounter()
t2 = TestCounter()
t3 = TestCounter()
print(TestCounter.count)


