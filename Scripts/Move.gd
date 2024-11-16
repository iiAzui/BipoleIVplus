class_name Move
extends Resource

@export var display_name: String
@export_enum("Attack", "Support") var move_type: String = "Attack"
@export_enum("Physical", "Magic") var damage_type: String = "Physical"
@export var hp_cost: int = 0
@export var min_range: int = 1
@export var max_range: int = 1
@export var power: float = 1.5 # multiplied by attack to get damage/heal amount
@export var hit_rate: float = 100 # new stat for accuracy percentage, only used outside of retro mode.
@export var hit: float = 1.0 # HIT stat from og bipole IV but renamed. only used in retro mode. not used on sppoort type spells.

# Used for dealing extra damage based on element.
# all except None will automatically deal a 1.3x damage mult towards the one element they deal more damage to.
# Fire -> Ice -> Bio -> Water -> Fire
# Electric <-> Shadow
@export_enum("None", "Fire", "Water", "Ice", "Bio", "Electric", "Shadow") var element: String = "None"

const elemental_chart = {
	"Fire": "Ice"
}

# Extra damage - seperate from the elmenetal system.
# Extra damage values will override what's in the elemental matchup table
# Trait to deal extra damage to
#@export_subgroup("Extra")
@export var extra_damage_trait: String
# Amount of extra damage to deal
@export var extra_multiplier: float

func get_damage_dealt(attacker: Unit, defender: Unit) -> int:
	var def_or_res = defender.defense if damage_type == "Physical" else defender.resistance
	var extra_mul = 1.0
	# Explicitly defined extra damage
	if extra_damage_trait in defender.traits:
		extra_mul = extra_multiplier
	# If not applicable, fallback to the type advantage table
	elif move_type in elemental_chart and elemental_chart[move_type] in defender.traits:
		extra_mul = 1.3
		
	var dmg: int = round((float(attacker.attack) * power - float(def_or_res) / 2.0) * extra_mul)
		
	print(attacker.character.display_name, " will deal ", dmg, " damage to ", defender.character.display_name, " with ", display_name)
		
	return dmg

func get_heal_amount(attacker: Unit, defender: Unit) -> int:
	return attacker.attack * power

# Get the percentage that this attack will hit the target.
func get_hit_chance(attacker: Unit, defender: Unit) -> float:
	var chance: float = clamp((float(attacker.accuracy) * hit - float(defender.agility)) / 10.0, 0.0, 1.0) 
	print(attacker.character.display_name, " has a ", chance*100, "% chance to hit ", defender.character.display_name, " with ", display_name)
	return chance
