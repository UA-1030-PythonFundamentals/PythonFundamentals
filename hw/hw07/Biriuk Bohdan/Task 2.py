def s_rectangle(lenght, height):
    S_r = lenght * height
    return S_r


def s_triangel(h, a):
    S_t = 0.5 * h * a
    return S_t


def s_circle(R):
    S_c = 3.14 * R**2
    return S_c


#area = input("Select a shape (rectangle, triangle, circle): ")
Selected = input("Select a shape (rectangle, triangle, circle): ")
for sel in Selected:
    if Selected == "rectangle":
        l = float(input("enter length: "))
        h = float(input("enter height: "))
        result_r = s_rectangle(l, h)
        print(result_r)
        break
    elif Selected == "triangle":
        h = float(input("enter height: "))
        a = float(input("enter base: "))
        result_t = s_triangel(h, a)
        print(result_t)
        break
    elif Selected == "circle":
        R = float(input("enter radius: "))
        result_c = s_circle(R)
        print(result_c)
        break
    else:
        print("The shape is not selected correctly")
        break



