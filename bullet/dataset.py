from bullet.dataclasse import *

bulletsetting = {
	'Normal_Bullet' : {
		'contact_range' 	: 10,
		'life_time' 		: 15,
		'speed' 			: 3,
	},

	'Guided_Bullet' : {
		'contact_range' 	: 12,
		'life_time' 		: 4,
		'speed' 			: 3,
	},

	'Variable_Velocity_Guided_Bullet' : {
		'contact_range' 	: 14,
		'life_time' 		: 6,
	
		'max_speed' 		: 12,
		'min_speed' 		: 0.01,
		'attenuation_value'	: 0.1,
	},
	'Normal_Multiple_Bullet' : {
		'contact_range' 	: 12,
		'life_time' 		: 7,
		'speed'				: 2,

		'shots_angle'		: 1,
		'shots_size'		: 4,
		'shots_cool_time'	: 0.5,
		'shots_spin_angle'	: 0,		
		'shots_contact_range':4,
		'shots_life_time' 	: 2,
		'shots_speed'		: 1,
	}
}


RANGE_type_01 = 350
RANGE_type_02 = 400
SIZE_type_01 = 6
SIZE_type_02 = 12

formations = {
	'sickle_Normal_Bullet_1' : [
		{
		'bullat_type'	: 'Normal_Bullet',
		'formation'		: 'wall',		
		'other': {
			'range_' 			: RANGE_type_01,
			'size' 				: SIZE_type_01,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(-10*RANGE_type_01,10*RANGE_type_01),		
			'location'			: Vector.Up,		
			'target_centralization':True,
			}
		},
		{
		'bullat_type'	: 'Normal_Bullet',
		'formation'		: 'wall',		
		'other': {
			'range_' 			: RANGE_type_01,
			'size' 				: SIZE_type_01,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(-10*RANGE_type_01,10*RANGE_type_01),		
			'location'			: Vector.Right,		
			'target_centralization':True,
			}
		},
	],
	'sickle_Normal_Bullet_2' : [
		{
		'bullat_type'	: 'Normal_Bullet',
		'formation'		: 'wall',		
		'other': {
			'range_' 			: RANGE_type_01,
			'size' 				: SIZE_type_01,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(10*RANGE_type_01,-10*RANGE_type_01),		
			'location'			: Vector.Down,		
			'target_centralization':True,
			}
		},
		{
		'bullat_type'	: 'Normal_Bullet',
		'formation'		: 'wall',		
		'other': {
			'range_' 			: RANGE_type_01,
			'size' 				: SIZE_type_01,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(10*RANGE_type_01,-10*RANGE_type_01),		
			'location'			: Vector.Left,		
			'target_centralization':True,
			}
		},
	],
	
	'circle_Guided_Bullet_1' : [
		{
		'bullat_type'	: 'Guided_Bullet',
		'formation'		: 'circle',		
		'other':{		
			'range_' 			: RANGE_type_02,
			'size' 				: 6,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(RANGE_type_01,RANGE_type_01),
			}
		}
	],
	'circle_Guided_Bullet_2' : [
		{
		'bullat_type'	: 'Variable_Velocity_Guided_Bullet',
		'formation'		: 'circle',		
		'other':{		
			'range_' 			: RANGE_type_02,
			'size' 				: 6,
			'center_position'	: Vector(RANGE_type_01,RANGE_type_01),
			'target_position'	: Vector(RANGE_type_01,RANGE_type_01),
			}
		}
	],

	'arc_Normal_Bullet_1' : [
		{
		'bullat_type'	: 'Normal_Bullet',
		'formation'		: 'circle',		
		'other':{		
			'range_' 			: RANGE_type_02, 		
			'size' 				: 12, 		
			'center_position' 	: Vector(RANGE_type_01,RANGE_type_01), 		
			'target_position' 	: Vector(RANGE_type_01,RANGE_type_01),		
			'arc_angle' : 0.4,
			}
		}
	],
	
	'Normal_Multiple_Bullet_1' : [
		{
		'bullat_type'	: 'Normal_Multiple_Bullet',
		'formation'		: None,		
		'other':{		
			'start_position' 	: Vector(RANGE_type_01,0),
 			'target_position' 	: 'target_position',
			**bulletsetting['Normal_Multiple_Bullet'],
			}
		}
	],
}

stagesettion = [
(1.0, 4.0, formations['sickle_Normal_Bullet_1']),
(3.0, 4.0, formations['sickle_Normal_Bullet_2']),
(7.0, 5.0, formations['circle_Guided_Bullet_1']),
(12.0, 7.0, formations['arc_Normal_Bullet_1']),
(17.0, 2.0, formations['Normal_Multiple_Bullet_1']),
(31.0, 6.0, formations['circle_Guided_Bullet_2']),
(99999, None, None),
]