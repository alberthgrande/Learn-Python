full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intellegence, charisma):

    # Character name checks
    if not isinstance(character_name, str):
        return 'The character name should be a string'

    elif not character_name.strip():
        return 'The character should have a name'

    elif len(character_name) > 10:
        return 'The character name is too long'

    elif ' ' in character_name:
        return 'The character name should not contain spaces'

    # Stats validation
    if not all(isinstance(stats, int) for stats in (strength, intellegence, charisma)):
        return 'All stats should be integers'

    elif any(stats < 1 for stats in (strength, intellegence, charisma)):
        return 'All stats should be no less than 1'

    elif any(stats > 4 for stats in (strength, intellegence, charisma)):
        return 'All stats should be no more than 4'

    # THIS is the correct rule
    if strength + intellegence + charisma != 7:
        return 'The character should start with 7 points'

    # Build stat lines (1–10 scale visualization)
    def build_line(label, value):
        return f"{label} " + full_dot * value + empty_dot * (10 - value)

    return (
        f"{character_name}\n"
        f"{build_line('STR', strength)}\n"
        f"{build_line('INT', intellegence)}\n"
        f"{build_line('CHA', charisma)}"
    )

print(create_character("ren", 2,4,1))