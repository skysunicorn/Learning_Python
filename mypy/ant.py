def remain_same(var):
    return var
def remove_ith(todo,i):
    assignment = todo[:]
    del assignment[i]
    return assignment
def only_one_left(todo):
    return len(todo) == 1
def ant(todo, task=remove_ith, end=only_one_left, f_each=remain_same):
    if end(todo):
        return [[f_each(todo[0])]]
    else:
        report = []
        for i in range(len(todo)):
            assignment = task(todo, i)
            re = ant(assignment, task, end, f_each)
            for j in range(len(re)):
                re[j].insert(0, f_each(todo[i]))
            report.extend(re)
        return report
a = ant(['c','a','d','e','u','s'])
for each in a:
    print(each)
print(len(a))
