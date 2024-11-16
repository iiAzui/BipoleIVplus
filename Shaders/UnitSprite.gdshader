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
uniform vec3 overlay_color = vec3(1);
uniform float overlay_blend = 0;

void fragment() {
	if (acted) {
		vec3 color = texture(texture_albedo, UV).rgb;
		ALBEDO = vec3((color.r + color.g + color.b) * 0.25);
	} else {
		vec3 texture_color = texture(texture_albedo, UV).rgb;
		ALBEDO = mix(texture_color, overlay_color, overlay_blend);
	}
	ALPHA = texture(texture_albedo, UV).a;
}