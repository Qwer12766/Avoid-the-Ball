bulletsetting = {
	'Normal_Bullet' : {
		'contact_range' 	: 10,
		'life_time' 		: 3,
		'speed' 			: 20,
	},

	'Guided_Bullet' : {
		'contact_range' 	: 15,
		'life_time' 		: 3,
		'speed' 			: 7,
	},

	'Variable_Velocity_Guided_Bullet' : {
		'contact_range' 	: 25,
		'life_time' 		: 5, 
		'max_speed' 		: 30,
		'min_speed' 		: 0.01,
		'attenuation_value'	: 0.1,
	},
	'Normal_Multiple_Bullet' : {
		'contact_range' 	: 20,
		'life_time' 		: 5,
		'speed'				: 3,

		'shots_angle'		: 2,
		'shots_size'		: 4,
		'shots_cool_time'	: 0.5,
		'shots_spin_speed'	: None,
		
		'shots_contact_range' 	: 7,
		'shots_life_time' 		: 2,
		'shots_speed'			: 7,
	}
}

Color = {
	'black' : (0,0,0),
	'white' : (255,255,255),
}