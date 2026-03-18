# *Codeing UTF-8*
def pfsp(n):
    if n == 1:
        return "皮"
    else:
        return "皮" + "肤死皮" * (n-1)
    
print(pfsp(1)) # 皮
print(pfsp(2)) # 皮肤死皮
print(pfsp(3)) # 皮肤死皮肤死皮
print(pfsp(4)) # 皮肤死皮肤死皮肤死皮
print(pfsp(5)) # 皮肤死皮肤死皮肤死皮肤死皮
print(pfsp(6)) # 皮肤死皮肤死皮肤死皮肤死皮肤死皮
print(pfsp(7)) # 皮肤死皮肤死皮肤死皮肤死皮肤死皮肤死皮
