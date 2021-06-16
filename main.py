import math
def inputx():
    x = int(input("(Faka ikho_odineyith ka x"))
    return x
def inputY():
    y = int(input("Faka ikho_odineyith kay"))
    return y
def input_radius():
    radius = int(input("Faka irediyasi"))
    return radius
def calc_perimeter(r):
    perimeter = 2 * (3.14 * r)
    print("Ipherimeter yesekile ngu", perimeter)
def calc_area(r):
        area = 3.14 * (r * r)
        print("I-Eriya yesekile ngu", area)
def outsideinsidecircle(x,y,r):
            distance = math.sqrt((x-0))*(x-0)+(y-0)*(y-0)
            if distance < r :
                print("Ipoyinti ingaphandke kwesekile")
            else:
                print("Ipoyint ingaphakath kwesekile")

if __name__ == '__main__':
    x = inputx()
    c =inputY()
    d = input_radius()
    calc_perimeter(d)
    calc_area(d)
    outsideinsidecircle(x, c, d)
