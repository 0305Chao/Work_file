origin = 0
def factory(pos):
    def go(stop):
        nonlocal pos
        new_pos = pos + stop
        pos = new_pos
        return pos
    return go
tourist = factory(origin)

print(tourist(2))
print(tourist.__closure__[0].cell_contents)
print(tourist(5))
print(tourist.__closure__[0].cell_contents)
print(tourist(6))
print(tourist.__closure__[0].cell_contents)
