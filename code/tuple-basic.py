# %%
p = 'python'
y = 'python'
print(p, y)
# %%
#  immutable: 문자열, 정수, 실수
p[0] = 'j'
# %%
print(id(p), id(y))
# %%
t = ()
t = tuple()
type(t)
# %%
n = 1
type(n)
# %%
m = (1,)
type(m)
# %%
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 == t2)
print(id(t1), id(t2))
print(id(t1) == id(t2))
print(t1 is t2)
# %%
t1[0]
# %%
t1[0] = 10;
# %%
lst = [1, 2, 3]
lst[1] = 20
lst
# %%
dir(tuple)
# %%

# %%


