from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Ring of Fire"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Frank")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    secondGoblin = Goblin("Scribble")
    print(f"{secondGoblin.name} enters the arena with {goblin.health} health.")

    hero = Hero("Bob")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")

    heroAttack = hero.attack()
    goblin.take_damage(heroAttack)

    goblinAttack = goblin.attack()
    hero.take_damage(goblinAttack)


if __name__ == "__main__":
    main()
