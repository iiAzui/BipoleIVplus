shader_type spatial;
render_mode unshaded;

uniform bool use_billboard = true;
void vertex() {
	if (use_billboard){
        MODELVIEW_MATRIX = VIEW_MATRIX * mat4(INV_VIEW_MATRIX[0], INV_VIEW_MATRIX[1], INV_VIEW_MATRIX[2], MODEL_MATRIX[3]);
	}
}

// --- Uniforms --- //
const bool weighted_grayscale = false;	// Determines whether to use normal or weighted averages

uniform bool acted;
uniform sampler2D texture_albedo : source_color, filter_nearest;
void fragment() {
	if (acted) {
		vec4 color = texture(texture_albedo, UV);
		ALBEDO = vec3((color.r + color.g + color.b) * 0.25);
	} else {
		ALBEDO = texture(texture_albedo, UV).rgb;
	}
	ALPHA = texture(texture_albedo, UV).a;
}