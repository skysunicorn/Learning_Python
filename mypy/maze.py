original_font='\33[0m'
green_font='\33[0;32m'
red_font='\33[0;31m'
blue_font='\33[0;34m'
def up():
    return(maze[i-1][j])
def down():
    return(maze[i+1][j])
def left():
    return(maze[i][j-1])
def right():
    return(maze[i][j+1])
direction_dict={'up':[-1,0],'down':[1,0],'left':[0,-1],'right':[0,1]}
def show_process():
    for r in range(1,len(maze)-1):
        for c in range (1,len(maze[1])):
            if maze[r][c]==0:
                print(green_font,end='')
                print(maze[r][c],end='')
            elif maze[r][c]==1:
                print(red_font, end='')
                print(maze[r][c], end='')
            elif maze[r][c]==2:
                print(blue_font, end='')
                print(maze[r][c], end='')
        print()
    print()
file=open('/Users/wyy/Documents/mypy/record/maze001.txt')
maze=[]
for each_line in file:
    maze.append(list(each_line[:-1]))
for i in range(len(maze)):
    for j in range(len(maze[i])):
        maze[i][j]=int(maze[i][j])
print(maze)
i=0
j=0
while j<=len(maze[1]):
    j+=1
    if maze[1][j]==0:
        break
dead=False
step=[]
while not dead:
    if (up()==0) + (down()==0) + (left()==0) + (right()==0) >= 1:
        if down()==0:
            i+=1
            step.insert(0,'down')
        elif up()==0:
            i-=1
            step.insert(0,'up')
        elif right()==0:
            j+=1
            step.insert(0,'right')
        elif left()==0:
            j-=1
            step.insert(0,'left')
        maze[i][j]=2
    else:
        maze[i][j]=1
        i+=-direction_dict[step[0]][0]
        j+=-direction_dict[step[0]][1]
        del step[0]
    show_process()
    if ((up()==1) and (down()==1) and (left()==1) and (right()==1)) or i==len(maze)-2:
        dead=True
        maze[i][j]=2
number_of_step=len(step)
print(original_font)
for i in range(number_of_step):
    print('step',str(i+1).zfill(3),':',step[number_of_step-1-i])