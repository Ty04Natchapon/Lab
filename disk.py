import turtle


def draw_towers():
    tower.color("gray")
    tower.width(5)
    for i in range(3):  
        tower.penup()
        tower.goto((i - 1) * 150, -150)  
        tower.pendown()
        tower.goto((i - 1) * 150, 150)  
        tower.penup()


def move_disk(t, start, end):
    start_pos, end_pos = pegs[start], pegs[end]
    width = t.shapesize()[1] * 10

    
    t.goto(t.xcor(), 200)
    
    t.goto(end_pos[0], 200)
    
    t.goto(end_pos[0], end_pos[1])

    
    pegs[end][1] += width
    pegs[start][1] -= width

def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 0:
        return

    
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    
    move_disk(disks[n - 1], source, destination)
    
    TowerOfHanoi(n - 1, auxiliary, destination, source)


screen = turtle.Screen()


tower = turtle.Turtle()
tower.speed(0)  


draw_towers()


num_disks = 4
disk_height = 25
disk_width = 25


pegs = {
    'A': [-150, -125 + disk_height * num_disks],  
    'B': [0, -125],                              
    'C': [150, -125]                             
}


disks = []
for i in range(num_disks):
    disk = turtle.Turtle()
    disk.shape("square")
    disk.shapesize(disk_height / 20, (disk_width + i * 30) / 20)  
    disk.penup()
    disk.goto(pegs['A'][0], pegs['A'][1] - (i * disk_height))  
    disks.append(disk)


TowerOfHanoi(num_disks, 'A', 'B', 'C')


screen.mainloop()