class_name Move
extends Resource

@export var display_name: String
@export_enum("Physical", "Magic") var move_type: String = "Physical"
@export var hp_cost: int = 0
@export var range: int = 1
@export var power: float = 1.5 # multiplied by attack to get damage/heal amount
@export var hit: float = 1.0

# Used for dealing extra damage based on element.
# all except None will automatically deal a 1.3x damage mult towards the one element they deal more damage to.
# Fire -> Ice -> Bio -> Water -> Fire
# Electric <-> Shadow
@export_enum("None", "Fire", "Water", "Ice", "Bio", "Thunder", "Shadow") var element: String = "None"

# Extra damage - seperate from the elmenetal system.
# Extra damage values will override what's in the elemental matchup table
# Trait to deal extra damage to
@export var extra: String
# Amount of extra damage to deal
@export var extra_multiplier: float
