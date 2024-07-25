import sys

# state = (is_player_turn, hp, mana, enemy_hp, duration_poison, duration_shield, duration_recharge)
state = (bool, int, int, int, int, int, int)
states_seen: {state: int} = {}
spells: {str: int} = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}
recharge_rate: int = 101
damage_poison: int = 3
damage_magic_missile: int = 4
damage_drain: int = 2
heal_drain: int = 2
shield_armor: int = 7
duration_poison: int = 6
duration_shield: int = 6
duration_recharge: int = 5


def get_values(file_name: str) -> [int]:
    return [int(i.strip().split(' ')[-1]) for i in open(file_name, 'r')]


def main() -> None:
    lines: [int] = get_values("input.txt")
    hp_enemy: int = lines[0]
    damage_enemy: int = lines[1]
    state_start: state = (True, 50, 500, hp_enemy, 0, 0, 0)
    minimum_mana_easy: int = fight(state_start, damage_enemy, 0, sys.maxsize, False)
    minimum_mana_hard: int = fight(state_start, damage_enemy, 0, sys.maxsize, True)

    print(str(minimum_mana_easy))
    print(str(minimum_mana_hard))


def fight(current_state: state, damage_enemy: int, mana_used: int, best_so_far: int, hard_mode: bool) -> int:
    duration_poison_new: int = current_state[4]
    duration_shield_new: int = current_state[5]
    duration_recharge_new: int = current_state[6]
    damage_actual: int = damage_enemy
    hp_enemy_new: int = current_state[3]
    mana_new: int = current_state[2]
    hp_new: int = current_state[1]
    state_new: state

    if mana_used > best_so_far or mana_used > current_state[2]:
        return sys.maxsize
    if current_state in states_seen:
        return states_seen.get(current_state)
    if hard_mode and current_state[0]:
        hp_new -= 1
        if hp_new <= 0:
            states_seen[current_state] = sys.maxsize
            return sys.maxsize

    if current_state[4] != 0:
        duration_poison_new -= 1
        hp_enemy_new -= damage_poison
    if current_state[5] != 0:
        duration_shield_new -= 1
        damage_actual -= shield_armor
    if current_state[6] != 0:
        mana_new += recharge_rate
        duration_recharge_new -= 1
    if hp_enemy_new <= 0:
        states_seen[current_state] = mana_used
        return mana_used

    if not current_state[0]:
        return round_boss(current_state, best_so_far, damage_actual, damage_enemy, duration_poison_new,
                          duration_recharge_new, duration_shield_new, hard_mode, hp_enemy_new, hp_new, mana_new,
                          mana_used)

    else:
        return round_player(current_state, best_so_far, damage_enemy, duration_poison_new, duration_recharge_new,
                            duration_shield_new, hard_mode, hp_enemy_new, hp_new, mana_new, mana_used)


def round_player(current_state: state, best_so_far: int, damage_enemy: int, duration_poison_new: int, 
                 duration_recharge_new: int, duration_shield_new: int, hard_mode: bool, hp_enemy_new: int, hp_new: int,
                 mana_new: int, mana_used: int) -> int:
    mana_min: int = sys.maxsize
    for spell, mana_cost in spells.items():
        mana_result: int = sys.maxsize

        if mana_new - mana_cost <= 0:
            states_seen[current_state] = sys.maxsize
            return mana_result

        state_new = get_state_new(current_state, spell, hp_new, mana_new, hp_enemy_new, duration_poison_new,
                                  duration_shield_new, duration_recharge_new)
        mana_result = fight(state_new, damage_enemy, mana_used + mana_cost, best_so_far, hard_mode)
        if mana_result < best_so_far:
            best_so_far = mana_result
        if mana_result < mana_min:
            mana_min = mana_result
    return mana_min


def round_boss(current_state: state, best_so_far: int, damage_actual: int, damage_enemy: int, duration_poison_new: int, 
               duration_recharge_new: int, duration_shield_new: int, hard_mode: bool, hp_enemy_new: int, hp_new: int, 
               mana_new: int, mana_used: int) -> int:
    if hp_new - damage_actual <= 0:
        states_seen[current_state] = sys.maxsize
        return sys.maxsize
    state_new = (True, hp_new - damage_actual, mana_new, hp_enemy_new,
                 duration_poison_new, duration_shield_new, duration_recharge_new)
    return fight(state_new, damage_enemy, mana_used, best_so_far, hard_mode)


def get_state_new(current_state: state, spell: str, hp_new: int, mana_new: int, hp_enemy_new: int,
                  duration_poison_new: int, duration_shield_new: int, duration_recharge_new: int) -> state:
    state_new: state = current_state

    match spell:
        case "Magic Missile":
            state_new = (False, hp_new, mana_new, hp_enemy_new - damage_magic_missile,
                         duration_poison_new, duration_shield_new, duration_recharge_new)
        case "Drain":
            state_new = (False, hp_new + heal_drain, mana_new,
                         hp_enemy_new - damage_drain, duration_poison_new, duration_shield_new,
                         duration_recharge_new)
        case "Poison":
            if duration_poison_new == 0:
                state_new = (False, hp_new, mana_new, hp_enemy_new,
                             duration_poison, duration_shield_new, duration_recharge_new)
        case "Shield":
            if duration_shield_new == 0:
                state_new = (False, hp_new, mana_new, hp_enemy_new,
                             duration_poison_new, duration_shield, duration_recharge_new)
        case "Recharge":
            if duration_recharge_new == 0:
                state_new = (False, hp_new, mana_new, hp_enemy_new,
                             duration_poison_new, duration_shield_new,
                             duration_recharge)

    return state_new


main()
