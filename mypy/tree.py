class Tree(object):
    Name = None
    Label = None
    Degree = 0
    Level = 0
    Content = None
    Parent = None
    Children = {}
    def __init__(self, Label = None, Name = None, Content = None, Parent = None):
        if Label != None:
            self.Label = Label
        else:
            right = False
            while not right:
                try:
                    self.Label = eval(input("input the Label and its type: "))
                    right = True
                except:
                    print("Wrong format! try: <type>(<Label>)")
        if Name != None:
            self.Name = Name
        else:
            self.Name = input("input the name: ")
        self.Content = Content
        self.Parent = Parent
    def rename(self,Name):
        self.Name = Name
    def relabel(self,Label):
        self.Label = Label
    def son(self,parent):
        if type(parent) == Tree and self.parent == None:
            parent.Children[self.Label] = self
            self.Parent = parent
            self.Level = parent.Level + 1
            parent.Degree += 1
