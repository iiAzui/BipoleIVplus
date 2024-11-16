shader_type canvas_item;

uniform sampler2D color_texture : source_color, repeat_enable;
uniform float tile_size = 64;
uniform vec2 uv_scroll = vec2(-0.25, -0.25);


varying vec2 position;

void vertex() {
	position = VERTEX;
}

void fragment() {
	vec4 texture_color = texture(color_texture, vec2(position.x / tile_size, position.y / tile_size) + uv_scroll * TIME);
	COLOR = texture_color;
}

//void light() {
	// Called for every pixel for every light affecting the CanvasItem.
	// Uncomment to replace the default light processing function with this one.
//}
