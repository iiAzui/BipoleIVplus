extends CharacterBody2D

func _physics_process(delta):
	if Input.is_action_just_pressed("Left"):
		if self.position.x > -304:
			self.position.x -= 32
	if Input.is_action_just_pressed("Right"):
		if self.position.x < 304:
			self.position.x += 32
	if Input.is_action_just_pressed("Up"):
		if self.position.y > -224:
			self.position.y -= 32
	if Input.is_action_just_pressed("Down"):
		if self.position.y < 224:
			self.position.y += 32
