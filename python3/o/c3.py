def damage(ski111, ski112):
    damage1 = ski111 * 3
    damage2 = ski112 *2 + 10
    return damage1, damage2
damages = damage(3, 6)
print(damages[0], damages[1])

ski111_damage, ski112_damage = damage(3, 6)
print(ski111_damage, ski112_damage)