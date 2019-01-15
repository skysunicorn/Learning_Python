class excel(object):
    row=0
    column=0
    place=[0,0]
    origin=[0,0]
    speed=1
    face='none'
    dimension=2
    horizontal='count from left to right'
    vertical='count from top to bottom'
    __show_process=False
    __direction_dict={'up':0,'0':'up','right':90,'90':'right','down':180,'180':'down','left':270,'270':'left'}
    __reverse_dict={'up':'down','down':'up','left':'right','right':'left'}
    def __init__(self,row=0,column=0,speed=1,place=[0,0],origin='default',face='none',listname='no list'):
        if place==[row,column]:
            self.row=row
            self.column=column
            self.place=place
        elif (row==0 and column==0) and (place!=[0,0]):
            self.place=place
            self.row=self.place[0]
            self.column=self.place[1]
        elif (row!=0 or column!=0) and (place==[0,0]):
            self.row=row
            self.column=column
            self.place=[self.row,self.column]
        else:
            print('BE CAREFUL!!! the row,column and place inputed do not agree with each other!')
        if origin=='default':
            self.origin=self.place
        else:
            self.origin=origin
        self.speed=speed
        self.face=face
        self.listname=listname
    def show_process_on(self):
        self.__show_process=True
        print('process is on')
    def show_process_off(self):
        self.__show_process=False
        print('process is off')
    def show_process(self):
        if self.__show_process==True:
            print('request done\ncurrent place:',self.place,'\ncurrent face:',self.face)
    def refresh_place(self):
        self.place=[self.row,self.column]
    def refresh_face(self,face_degree):
        self.face=self.__direction_dict[str(face_degree)]
    def refresh_row_and_column(self):
        self.row=self.place[0]
        self.column=self.place[1]
    def move_up(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.row=self.row-n
        self.refresh_place()
        self.show_process()
    def move_down(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.row=self.row+n
        self.refresh_place()
        self.show_process()
    def move_left(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.column=self.column-n
        self.refresh_place()
        self.show_process()
    def move_right(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.column=self.column+n
        self.refresh_place()
        self.show_process()
    def move_forward(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            move_direction='self.move_'+self.face+'(n)'
            eval(move_direction)
    def move_backward(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            move_direction='self.move_'+self.__reverse_dict[self.face]+'(n)'
            eval(move_direction)
    def move(self,direction,n='speed'):
        if direction=='up':
            self.move_up(n)
        elif direction=='down':
            self.move_down(n)
        elif direction=='left':
            self.move_left(n)
        elif direction=='right':
            self.move_right(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
    def turn_left(self):
        face_degree=(self.__direction_dict[self.face]+270)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn_right(self):
        face_degree=(self.__direction_dict[self.face]+90)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn_around(self):
        face_degree=(self.__direction_dict[self.face]+180)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn(self,direction):
        if direction=='left':
            self.turn_left()
        elif direction=='right':
            self.turn_right()
        elif direction=='around':
            self.turn_around()
        else:
            print('BE CAREFUL!!! undefined direction')
    def face_(self,direction):
        if direction=='up':
            self.face='up'
        elif direction=='down':
            self.face='down'
        elif direction=='left':
            self.face='left'
        elif direction=='right':
            self.face='right'
        elif direction=='none':
            self.face='none'
        else:
            print('BE CAREFUL!!! undefined direction!')
    def jump_to(self,place):
        self.place=place
        self.refresh_row_and_column()
        self.show_process()
    def back_to_origin(self):
        self.place=self.origin
        self.refresh_row_and_column()
        self.show_process()
    def up_place(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_place=[self.place[0]-n,self.place[1]]
        return(spying_place)
    def down_place(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_place=[self.place[0]+n,self.place[1]]
        return(spying_place)
    def left_place(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_place=[self.place[0],self.place[1]-n]
        return(spying_place)
    def right_place(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_place=[self.place[0],self.place[1]+n]
        return(spying_place)
    def forward_place(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            direction_place='self.'+self.face+'_place(n)'
            spying_place=eval(direction_place)
            return(spying_place)
    def backward_place(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            direction_place='self.'+self.__reverse_dict[self.face]+'_place(n)'
            spying_place=eval(direction_place)
            return(spying_place)
    def lefthand_place(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! undefined direction!')
        else:
            face_degree=(self.__direction_dict[self.face]+270)%360
            direction=self.__direction_dict[str(face_degree)]
            direction_place='self.'+direction+'_place(n)'
            spying_place=eval(direction_place)
            return(spying_place)
    def righthand_place(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! undefined direction!')
        else:
            face_degree=(self.__direction_dict[self.face]+90)%360
            direction=self.__direction_dict[str(face_degree)]
            direction_place='self.'+direction+'_place(n)'
            spying_place=eval(direction_place)
            return(spying_place)
    def spy_place(self,direction,n='speed'):
        if direction=='up':
            self.up_place(n)
        elif direction=='down':
            self.down_place(n)
        elif direction=='left':
            self.left_place(n)
        elif direction=='right':
            self.right_place(n)
        elif direction=='forward':
            self.forward_place(n)
        elif direction=='backward':
            self.backward_place(n)
        elif direction=='lefthand':
            self.lefthand_place(n)
        elif direction=='righthand':
            self.righthand_place(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
    def place_to_string(self,listname,spying_place):
        spying_place_string=listname+'['+str(spying_place[0])+']'+'['+str(spying_place[1])+']'
        return(spying_place_string)
    def current_value(self,listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            current_place_string=self.place_to_string(listname,self.place)
            current_value=eval(current_place_string)
            return(current_value)
    def up_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_place=self.up_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def down_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_place=self.down_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def left_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_place=self.left_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def right_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_place=self.right_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def forward_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_place=self.forward_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def backward_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_place=self.backward_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def lefthand_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_place=self.lefthand_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def righthand_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_place=self.righthand_place(n)
            spying_place_string=self.place_to_string(listname,spying_place)
            spying_value=eval(spying_place_string)
            return(spying_value)
    def spy_value(self,direction,n='speed'):
        if direction=='up':
            self.up_value(n)
        elif direction=='down':
            self.down_value(n)
        elif direction=='left':
            self.left_value(n)
        elif direction=='right':
            self.right_value(n)
        elif direction=='forward':
            self.forward_value(n)
        elif direction=='backward':
            self.backward_value(n)
        elif direction=='lefthand':
            self.lefthand_value(n)
        elif direction=='righthand':
            self.righthand_value(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
class coordinate(object):
    x=0
    y=0
    coordinate=[0,0]
    origin=[0,0]
    speed=1
    face='none'
    dimension=2
    horizontal='count from left to right'
    vertical='count from bottom to top'
    __show_process=False
    __direction_dict={'up':0,'0':'up','right':90,'90':'right','down':180,'180':'down','left':270,'270':'left'}
    __reverse_dict={'up':'down','down':'up','left':'right','right':'left'}
    def __init__(self,x=0,y=0,speed=1,coordinate=[0,0],origin='default',face='none',surface_name='no surface'):
        if coordinate==[x,y]:
            self.x=x
            self.y=y
            self.coordinate=coordinate
        elif (x==0 and y==0) and (coordinate!=[0,0]):
            self.coordinate=coordinate
            self.x=self.coordinate[0]
            self.y=self.coordinate[1]
        elif (x!=0 or y!=0) and (coordinate==[0,0]):
            self.x=x
            self.y=y
            self.coordinate=[self.x,self.y]
        else:
            print('BE CAREFUL!!! the x,y and coordinate inputed do not agree with each other!')
        if origin=='default':
            self.origin=self.coordinate
        else:
            self.origin=origin
        self.speed=speed
        self.face=face
        self.surface_name=surface_name
    def show_process_on(self):
        self.__show_process=True
        print('process is on')
    def show_process_off(self):
        self.__show_process=False
        print('process is off')
    def show_process(self):
        if self.__show_process==True:
            print('request done\ncurrent coordinate:',self.coordinate,'\ncurrent face:',self.face)
    def refresh_coordinate(self):
        self.coordinate=[self.x,self.y]
    def refresh_face(self,face_degree):
        self.face=self.__direction_dict[str(face_degree)]
    def refresh_x_and_y(self):
        self.x=self.coordinate[0]
        self.y=self.coordinate[1]
    def move_up(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.y=self.y+n
        self.refresh_coordinate()
        self.show_process()
    def move_down(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.y=self.y-n
        self.refresh_coordinate()
        self.show_process()
    def move_left(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.x=self.x-n
        self.refresh_coordinate()
        self.show_process()
    def move_right(self,n='speed'):
        if n=='speed':
            n=self.speed
        self.y=self.x+n
        self.refresh_coordinate()
        self.show_process()
    def move_forward(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            move_direction='self.move_'+self.face+'(n)'
            eval(move_direction)
    def move_backward(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            move_direction='self.move_'+self.__reverse_dict[self.face]+'(n)'
            eval(move_direction)
    def move(self,direction,n='speed'):
        if direction=='up':
            self.move_up(n)
        elif direction=='down':
            self.move_down(n)
        elif direction=='left':
            self.move_left(n)
        elif direction=='right':
            self.move_right(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
    def turn_left(self):
        face_degree=(self.__direction_dict[self.face]+270)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn_right(self):
        face_degree=(self.__direction_dict[self.face]+90)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn_around(self):
        face_degree=(self.__direction_dict[self.face]+180)%360
        self.refresh_face(face_degree)
        self.show_process()
    def turn(self,direction):
        if direction=='left':
            self.turn_left()
        elif direction=='right':
            self.turn_right()
        elif direction=='around':
            self.turn_around()
        else:
            print('BE CAREFUL!!! undefined direction')
    def face_(self,direction):
        if direction=='up':
            self.face='up'
        elif direction=='down':
            self.face='down'
        elif direction=='left':
            self.face='left'
        elif direction=='right':
            self.face='right'
        elif direction=='none':
            self.face='none'
        else:
            print('BE CAREFUL!!! undefined direction!')
    def jump_to(self,coordinate):
        self.coordinate=coordinate
        self.refresh_x_and_y()
        self.show_process()
    def back_to_origin(self):
        self.coordinate=self.origin
        self.refresh_x_and_y()
        self.show_process()
    def up_coordinate(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_coordinate=[self.coordinate[0],self.coordinate[1]+n]
        return(spying_coordinate)
    def down_coordinate(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_coordinate=[self.coordinate[0],self.coordinate[1]-n]
        return(spying_coordinate)
    def left_coordinate(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_coordinate=[self.coordinate[0]-n,self.coordinate[1]]
        return(spying_coordinate)
    def right_coordinate(self,n='speed'):
        if n=='speed':
            n=self.speed
        spying_coordinate=[self.coordinate[0]+n,self.coordinate[1]]
        return(spying_coordinate)
    def forward_coordinate(self,n='speed'):
        if n=='speed':
            n=self.speed
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            direction_coordinate='self.'+self.coordinate+'_coordinate(n)'
            spying_coordinate=eval(direction_coordinate)
            return(spying_coordinate)
    def backward_coordinate(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        else:
            direction_coordinate='self.'+self.__reverse_dict[self.face]+'_coordinate(n)'
            spying_coordinate=eval(direction_coordinate)
            return(spying_coordinate)
    def lefthand_coordinate(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! undefined direction!')
        else:
            face_degree=(self.__direction_dict[self.face]+270)%360
            direction=self.__direction_dict[str(face_degree)]
            direction_coordinate='self.'+direction+'_coordinate(n)'
            spying_coordinate=eval(direction_coordinate)
            return(spying_coordinate)
    def righthand_coordinate(self,n='speed'):
        if self.face=='none':
            print('BE CAREFUL!!! undefined direction!')
        else:
            face_degree=(self.__direction_dict[self.face]+90)%360
            direction=self.__direction_dict[str(face_degree)]
            direction_coordinate='self.'+direction+'_coordinate(n)'
            spying_coordinate=eval(direction_coordinate)
            return(spying_coordinate)
    def spy_coordinate(self,direction,n='speed'):
        if direction=='up':
            self.up_coordinate(n)
        elif direction=='down':
            self.down_coordinate(n)
        elif direction=='left':
            self.left_coordinate(n)
        elif direction=='right':
            self.right_coordinate(n)
        elif direction=='forward':
            self.forward_coordinate(n)
        elif direction=='backward':
            self.backward_coordinate(n)
        elif direction=='lefthand':
            self.lefthand_coordinate(n)
        elif direction=='righthand':
            self.righthand_coordinate(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
    def coordinate_to_string(self,listname,spying_coordinate):
        spying_coordinate_string=listname+'['+str(spying_coordinate[0])+']'+'['+str(spying_coordinate[1])+']'
        return(spying_coordinate_string)
    def current_value(self,listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            current_coordinate_string=self.coordinate_to_string(listname,self.coordinate)
            current_value=eval(current_coordinate_string)
            return(current_value)
    def up_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_coordinate=self.up_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def down_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_coordinate=self.down_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def left_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_coordinate=self.left_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def right_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        else:
            spying_coordinate=self.right_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def forward_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        if self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_coordinate=self.forward_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def backward_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_coordinate=self.backward_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def lefthand_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_coordinate=self.lefthand_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def righthand_value(self,n='speed',listname='list name'):
        if listname=='list name':
            listname=self.listname
        if listname=='no list':
            print('BE CAREFUL!!! there is no list!')
        elif self.face=='none':
            print('BE CAREFUL!!! this object has no direction!')
        if listname!='no list' and self.face!='none':
            spying_coordinate=self.righthand_coordinate(n)
            spying_coordinate_string=self.coordinate_to_string(listname,spying_coordinate)
            spying_value=eval(spying_coordinate_string)
            return(spying_value)
    def spy_value(self,direction,n='speed'):
        if direction=='up':
            self.up_value(n)
        elif direction=='down':
            self.down_value(n)
        elif direction=='left':
            self.left_value(n)
        elif direction=='right':
            self.right_value(n)
        elif direction=='forward':
            self.forward_value(n)
        elif direction=='backward':
            self.backward_value(n)
        elif direction=='lefthand':
            self.lefthand_value(n)
        elif direction=='righthand':
            self.righthand_value(n)
        else:
            print('BE CAREFUL!!! undefined direction!')
def copied(character):
    if type(character)==excel:
        copied_character=excel(row=character.row,column=character.column,place=character.place,speed=character.speed,origin=character.origin,face=character.face,listname=character.listname)
        return(copied_character)
    if type(character)==coordinate:
        copied_character=coordinate(x=character.x,y=character.y,coordinate=character.coordinate,speed=character.speed,origin=character.origin,face=character.face,surface_name=character.surface_name)
        return(copied_character)
    else:
        print("BE CAREFUL!!! cannot recognize this type of character!")
