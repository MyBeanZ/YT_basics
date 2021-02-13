from turtle import forward, right, pendown, penup, exitonclick

a = float(input('delka a:'))
b = float(input('delka b:'))
penon_len = 1
sum_a = 0
delky = [a, b]
corner = 0

for k in range(3):
    for i in range(2):
        for j in delky:
            while j > sum_a:
                if j < penon_len:
                    forward(j)
                else:
                    forward(penon_len - corner)
                penup()
                forward(5)
                pendown()
                sum_a += penon_len + 5 - corner
                penon_len += 1
                corner = 0
            else:
                if (j - sum_a) != 0:
                    sum_a -= penon_len
                    forward(j - sum_a)
                    corner = (j - sum_a)

            right(90)
            sum_a = 0 

          
    right(40)
exitonclick()