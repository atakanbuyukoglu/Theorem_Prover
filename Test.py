from Sets import Set
from Logic import Condition

S = Set((1,2,3), var_name='S')
cond = Condition(comparator='>', value=2)
S1 = Set(parent_set=S, parent_cond=cond)

print(S1)

print(2 in S1)
print(3 in S1)
