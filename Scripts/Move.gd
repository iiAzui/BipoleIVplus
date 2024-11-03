class_name Move
extends Resource

@export var display_name: String
@export_enum("Attack", "Support") var move_type: String = "Attack"
@export_enum("Physical", "Magic") var damage_type: String = "Physical"
@export var hp_cost: int = 0
@export var range: int = 1
@export var power: float = 1.5 # multiplied by attack to get damage/heal amount
@export var hit_rate: float = 100 # new stat for accuracy percentage, only used outside of retro mode.
@export var accuracy_multiplier: float = 1.0 # HIT stat from og bipole IV but renamed. only used in retro mode.

# Used for dealing extra damage based on element.
# all except None will automatically deal a 1.3x damage mult towards the one element they deal more damage to.
# Fire -> Ice -> Bio -> Water -> Fire
# Electric <-> Shadow
@export_enum("None", "Fire", "Water", "Ice", "Bio", "Thunder", "Shadow") var element: String = "None"

# Extra damage - seperate from the elmenetal system.
# Extra damage values will override what's in the elemental matchup table
# Trait to deal extra damage to
@export_subgroup("Extra")
@export var extra_damage_trait: String
# Amount of extra damage to deal
@export var extra_multiplier: float
