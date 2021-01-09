class A:
    def __init__(self, argument):
        self.value = argument


class B(A):
    def __init__(self, nest_drugo, *args, **kwargs):
        self.nest_drugo = nest_drugo
        super().__init__(*args, **kwargs)


obj = B("nest drugo", "NESTO TRECE")

print(obj.nest_drugo)
print(obj.value)
