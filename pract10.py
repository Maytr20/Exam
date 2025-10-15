from ete3 import Tree

t = Tree("((male,female),(((((ME,Brother,Sister)Father,Mother)Grandfather,Grandmother)parent)Tree);", format=1)
print(t.get_ascii(show_internal=True))

male = {"robert", "john", "tom", "david"}
female = {"mary", "anna", "lisa", "emma"}

parent = {
    ("robert", "john"),
    ("mary", "john"),
    ("robert", "lisa"),
    ("mary", "lisa"),
    ("john", "tom"),
    ("anna", "tom"),
    ("lisa", "emma"),
    ("david", "emma")
}

def father(x, y):
    return x in male and (x, y) in parent

def mother(x, y):
    return x in female and (x, y) in parent

def grandfather(x, y):
    return x in male and any((x, z) in parent and (z, y) in parent for z in male | female)

def grandmother(x, y):
    return x in female and any((x, z) in parent and (z, y) in parent for z in male | female)

def brother(x, y):
    return x in male and x != y and any((p, x) in parent and (p, y) in parent for p in male | female)

def sister(x, y):
    return x in female and x != y and any((p, x) in parent and (p, y) in parent for p in male | female)

def uncle(x, y):
    return x in male and any(brother(x, p) and (p, y) in parent for p in male | female)

def aunt(x, y):
    return x in female and any(sister(x, p) and (p, y) in parent for p in male | female)

def nephew(x, y):
    return x in male and any((p, x) in parent and (y, p) in parent for p in male | female)

def niece(x, y):
    return x in female and any((p, x) in parent and (y, p) in parent for p in male | female)

def cousin(x, y):
    return x != y and any(
        (a, x) in parent and (b, y) in parent and sibling(a, b)
        for a in male | female for b in male | female
    )

def sibling(x, y):
    return (brother(x, y) or sister(x, y))

print("Father of John:", [p for p in male if father(p, "john")])
print("Mother of John:", [p for p in female if mother(p, "john")])
print("Grandfather of Emma:", [p for p in male if grandfather(p, "emma")])
print("Grandmother of Tom:", [p for p in female if grandmother(p, "tom")])
print("Brothers of Lisa:", [p for p in male if brother(p, "lisa")])
print("Sisters of John:", [p for p in female if sister(p, "john")])
print("Uncles of Emma:", [p for p in male if uncle(p, "emma")])
print("Aunts of Tom:", [p for p in female if aunt(p, "tom")])
print("Cousins of Tom:", [p for p in male | female if cousin(p, "tom")])