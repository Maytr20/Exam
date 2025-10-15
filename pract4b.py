#A program to solve water jug problem 

#Python Code:
Capacity = (12, 8, 5)
X = Capacity[0]
Y = Capacity[1]
Z = Capacity[2]
memory = {}
ans = []

def get_all_states (State):
    a = State[0]
    b = State[1]
    c = State[2]
    
    if (a==6 and b==6):
        ans.append(State)
        return True

    if (a, b, c) in memory:
        return False
    
    memory[(a, b, c)] = 1
    
    
    if get_all_states((a, Y, c)):
        ans.append(State)
        return True
    
    if get_all_states((a, b, Z)):
        ans.append(State)
        return True

    if get_all_states((X, b, c)):
        ans.append(State)
        return True

    
    if (a > 0):
        if get_all_states((0, b, c)):
            ans.append(State)
            return True
        
    if (b > 0):
        if get_all_states((a, 0, c)):
            ans.append(State)
            return True

    if (c > 0):
        if get_all_states((a, b, 0)):
            ans.append(State)
            return True


    if (a > 0) and (b < Y):
        if (a + b <= Y): # A pours fully into B
            if get_all_states((0, a + b, c)):
                ans.append(State)
                return True
        else: # B fills up, A has remainder
            if get_all_states((a - (Y - b), Y, c)):
                ans.append(State)
                return True
    
    # Pour A into C
    if (a > 0) and (c < Z):
        if (a + c <= Z): # A pours fully into C
            if get_all_states((0, b, a + c)):
                ans.append(State)
                return True
        else: # C fills up, A has remainder
            if get_all_states((a - (Z - c), b, Z)):
                ans.append(State)
                return True

    # Pour B into A
    if (b > 0) and (a < X):
        if (a + b <= X): # B pours fully into A
            if get_all_states((a + b, 0, c)):
                ans.append(State)
                return True
        else: # A fills up, B has remainder
            if get_all_states((X, b - (X - a), c)):
                ans.append(State)
                return True
    

    if (b > 0) and (c < Z):
        if (b + c <= Z): # B pours fully into C
            if get_all_states((a, 0, b + c)):
                ans.append(State)
                return True
        else: # C fills up, B has remainder
            if get_all_states((a, b - (Z - c), Z)):
                ans.append(State)
                return True

    if (c > 0) and (a < X):
        if (a + c <= X): # C pours fully into A
            if get_all_states((a + c, b, 0)):
                ans.append(State)
                return True
        else: # A fills up, C has remainder
            if get_all_states((X, b, c - (X - a))):
                ans.append(State)
                return True

    if (c > 0) and (b < Y):
        if (b + c <= Y): # C pours fully into B
            if get_all_states((a, b + c, 0)):
                ans.append(State)
                return True
        else: # B fills up, C has remainder
            if get_all_states((a, Y, c - (Y - b))):
                ans.append(State)
                return True
    
    return False

initial_state = (0, 0, 0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
    print(i)