sample_dict = {'a': 100, 'b': 200, 'c': 300}

def val(va):
    for k in sample_dict.values():
        if k == va:
            print(f"{k} is exist in sample_dict.")

val(200)
val(400)