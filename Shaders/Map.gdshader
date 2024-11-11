shader_type spatial;

uniform vec3 albedo: source_color = vec3(0,0.5,0);
uniform vec4 grid_color: source_color = vec4(0,0,0,0.25);
uniform float grid_thickness = 0.1;

varying vec3 position;

void vertex() {
	position = NODE_POSITION_WORLD + VERTEX;
}

void fragment() {
	float grid_step = step(1.0 - grid_thickness, max(fract(position.x + 0.5 - grid_thickness/2.0), fract(position.z + 0.5 - grid_thickness/2.0)));
	
	ALBEDO = mix(albedo, vec3(grid_color.r, grid_color.g, grid_color.b), grid_step * grid_color.a);
}

//void light() {
	// Called for every pixel for every light affecting the material.
	// Uncomment to replace the default light processing function with this one.
//}
