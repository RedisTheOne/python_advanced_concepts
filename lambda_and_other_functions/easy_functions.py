def mult_by_2(num):
    return num * 2

times_two = mult_by_2
print(times_two(10))

def get_func_mult_by_num(value):
    def mult_by(num):
        return num * value
    return mult_by

mult_by_num = get_func_mult_by_num(10)
print(mult_by_num(10))