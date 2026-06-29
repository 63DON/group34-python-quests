# Quest 28 - The Healing Spell
def heal(current_hp, heal_amount, max_hp):
    new_hp = current_hp + heal_amount
    if new_hp > max_hp:
        new_hp = max_hp
    return new_hp

hero_hp = 40
max_hp = 100
print("HP before healing:", hero_hp)
hero_hp = heal(hero_hp, 30, max_hp)
print("HP after healing by 30:", hero_hp)
hero_hp = heal(hero_hp, 80, max_hp)
print("HP after healing by 80 (capped at max):", hero_hp)
