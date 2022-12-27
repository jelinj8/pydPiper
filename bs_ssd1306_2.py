#!/usr/bin/python.pydPiper
# coding: UTF-8

from __future__ import unicode_literals


# Page Definitions
# See Page Format.txt for instructions and examples on how to modify your display settings

# Load the fonts needed for this system
FONTS = {
	'small': { 'default':True, 'file':'latin1_5x8.fnt','size':(5,8) },
#	'large': { 'file':'BigFont_10x16.fnt', 'size':(10,16) },
	'large': { 'file':'Vintl01_10x16.fnt', 'size':(10,16) },
	'tiny': { 'file':'upperasciiwide_3x5_fixed.fnt', 'size':(5,5) },
}

TRUETYPE_FONTS = {
	'DejaVuSansTIT': { 'file':'DejaVuSans.ttf', 'size':20 },
        'DejaVuSansART': { 'file':'DejaVuSans.ttf', 'size':14 },

        'DejaVuSans35': { 'file':'DejaVuSans.ttf', 'size':35 },
        'DejaVuSans45': { 'file':'DejaVuSans.ttf', 'size':45 },
        'DejaVuSans50': { 'file':'DejaVuSans.ttf', 'size':50 },

}

IMAGES = {
#	'progbar': {'file':'progressbar_80x8.png' },
#	'splash': {'file':'pydPiper_fixed_splash.png' }
}

# Load the Widgets that will be used to produce the display pages
WIDGETS = {
	'songprogress': { 'type':'progressbar', 'value':'elapsed', 'rangeval':(0,'length'), 'size':(128,2) },
	'xofy': { 'type':'text', 'format':'{0}/{1}', 'variables':['playlist_position', 'playlist_length'], 'font':'large', 'size':(128,16), 'just':'center', 'varwidth':True },
	'volume': { 'type':'text', 'format':'Hlasitost: {0}', 'variables':['volume'], 'font':'small', 'just':'right', 'size':(64,8), 'varwidth':True },

	#'encoding': { 'type':'text', 'format':'{0}', 'variables':['encoding'], 'font':'small', 'just':'right', 'size':(60,16), 'varwidth':True },
	'tracktype': { 'type':'text', 'format':'{0}kHz {1}b {3}ch {2}kbps', 'variables':['sample','bits','kbps','channels'], 'font':'small', 'just':'center', 'size':(128,8), 'varwidth':True },

	'volumelarge': { 'type':'ttext', 'format':'{0}', 'variables':['volume'], 'font':'DejaVuSans50', 'just':'center', 'varwidth':True, 'size':(128,40) },
	'volumebar': { 'type':'progressbar', 'value':'volume', 'rangeval':(0,100), 'size':(128,8) },

	'title': { 'type':'ttext', 'format':'{0}', 'variables':['title'], 'font':'DejaVuSansTIT','varwidth':True,'effect':('scroll','left',2,1,100,'onstart',3,128), 'size':(128,30), 'just':'center'},
	'artist': { 'type':'ttext', 'format':'{0}', 'variables':['artist'], 'font':'DejaVuSansART','varwidth':True,'effect':('scroll','left',2,1,100,'onstart',3,128), 'size':(128,16), 'just':'center'},
        'album': { 'type':'ttext', 'format':'{0}', 'variables':['album'], 'font':'DejaVuSansART','varwidth':True,'effect':('scroll','left',2,1,100,'constart',3,128), 'size':(128,16), 'just':'center'},

	'elapsed1': { 'type':'text', 'format':'{0}', 'variables':['elapsed|strftime+%-M:%S'], 'font':'small','size':(30,8), 'varwidth':True},
	'length1': { 'type':'text', 'format':'{0}', 'variables':['length|strftime+%-M:%S'], 'font':'small','size':(30,8),'just':'right','varwidth':True},
	'elapsed2': { 'type':'text', 'format':'{0}', 'variables':['elapsed|strftime+%M:%S'], 'font':'small','size':(30,8), 'varwidth':True},
	'length2': { 'type':'text', 'format':'{0}', 'variables':['length|strftime+%M:%S'], 'font':'small','size':(30,8),'just':'right','varwidth':True},
	'elapsed3': { 'type':'text', 'format':'{0}', 'variables':['elapsed|strftime+%-H:%M:%S'], 'font':'small','size':(40,8), 'varwidth':True},
	'length3': { 'type':'text', 'format':'{0}', 'variables':['length|strftime+%-H:%M:%S'], 'font':'small','size':(40,8),'just':'right','varwidth':True},


	'stime': { 'type':'text', 'format':'{0}', 'variables':['utc|timezone+Europe/Prague|strftime+%H:%M'], 'font':'small', 'just':'right', 'varwidth':True, 'size':(60,16) },
	'time': { 'type':'text', 'format':'{0}', 'variables':['utc|timezone+Europe/Prague|strftime+%H:%M'], 'font':'large', 'just':'center', 'varwidth':True, 'size':(128,16) },
	'ttime': { 'type':'ttext', 'format':'{0}', 'variables':['utc|timezone+Europe/Prague|strftime+%H:%M'], 'font':'DejaVuSans45', 'just':'center', 'varwidth':True, 'size':(128,64) },
	'tempsmall': { 'type':'text', 'format':'{0}', 'variables':['outside_temp_formatted'], 'font':'small', 'just':'right', 'size':(24,16) },
	'temphilow': { 'type':'text', 'format':'H {0}\nL {1}', 'variables':['outside_temp_max|int', 'outside_temp_min|int'], 'font':'small', 'just':'right', 'size':(25,16) },
	'temp': { 'type':'text', 'format':'{0}', 'variables':['outside_temp_formatted'], 'font':'large', 'just':'center', 'size':(80,16) },
	'weather': { 'type':'text', 'format':'{0}', 'variables':['outside_conditions|capitalize'], 'font':'large','varwidth':True, 'effect':('scroll','left',1,1,20,'onloop',3,100)},

	'splash': { 'type':'ttext', 'format':'MoOde', 'font':'DejaVuSans35', 'just':'center', 'varwidth':True, 'size':(128,64) },
	'spotify': { 'type':'ttext', 'format':'Spotify', 'font':'DejaVuSans35', 'just':'center', 'varwidth':True, 'size':(128,64) },
	'webradio': { 'type':'ttext', 'format':'webradio', 'font':'DejaVuSans35', 'just':'center', 'varwidth':True, 'size':(128,64) },
	'player': { 'type':'ttext', 'format':'{0}', 'variables':['actPlayer'], 'font':'DejaVuSans35', 'just':'center', 'varwidth':True, 'size':(128,64) },
}

# Assemble the widgets into canvases.  Only needed if you need to combine multiple widgets together so you can produce effects on them as a group.
CANVASES = {
	# -M:SS
	'playing1': {
		'widgets': [ 
			('title',0,0),
#			('artist',0,25),
                        ('album',0,25),

			('xofy',0,47),
			('elapsed1',0,50),
			('length1',97,50),
			('songprogress',0,62),
		],
		'size':(128,64) 
	},
	
	# MM:SS
	'playing2': {
	'widgets': [
			('title',0,0),
#			('artist',0,25),
                        ('album',0,25),

			('xofy',0,47),
			('elapsed2',0,50),
			('length2',97,50),
			('songprogress',0,62),
		],
		'size':(128,64)
	},

	# -H:MM:SS
	'playing3': {
		'widgets': [
			('title',0,0),
#			('artist',0,25),
                        ('album',0,25),

			('xofy',0,47),
			('elapsed3',0,50),
			('length3',87,50),
			('songprogress',0,62),
		],
		'size':(128,64)
	},

	'stoptime': {
		'widgets': [
			#('ttime',0,10),
			#('player',0,10),
		],
		'size':(128,64)
	},

	'splashw': {
		'widgets': [
			('splash',0,10),
		],
		'size':(128,64)
	},

	'spotifyw': {
		'widgets': [
			('spotify',0,10),
		],
		'size':(128,64)
	},

	'webradiow': {
		'widgets': [
			('webradio',0,10),
		],
		'size':(128,64)
	},

	'stoptimetemp_popup': {
		'widgets': [
			('ttime',3,0), 
			('tempsmall',100,0), 
			('weather',8,47), 
			('temphilow',100,48) 
		],
		'size':(128,64)
	},

	'volume_changed': {
		'widgets': [ 
			('volumelarge',0,0),
			('volumebar',0,55),
		],
		'size':(128,64)
	}

}

# Place the canvases into sequences to display when their condition is met
# More than one sequence can be active at the same time to allow for alert messages
# You are allowed to include a widget in the sequence without placing it on a canvas

# Note about Conditionals
# Conditionals must evaluate to a True or False resulting
# To access system variables, refer to them within the db dictionary (e.g. db['title'])
# To access the most recent previous state of a variable, refer to them within the dbp dictionary (e.g. dbp['title'])
SEQUENCES = [
	{
		'name': 'seqPlay',
		'canvases': [
			{ 'name':'playing1', 'duration':999, 'conditional':"db['length'] < 600"},
			{ 'name':'playing2', 'duration':999, 'conditional':"db['length'] >= 600 and db['length'] < 3600"},
			{ 'name':'playing3', 'duration':999, 'conditional':"db['length'] >= 3600"},
		],
		'conditional': "db['state']=='play'"
	},

	{
		'name': 'seqStop',
		'canvases': [
			{'name':'stoptime', 'duration':9999, },
			#{'name':'stoptime', 'duration':9999, 'conditional':"db['actPlayer'] == 'MPD'"},
			#{'name':'spotifyw', 'duration':9999, 'conditional':"db['actPlayer'] == 'Spotify'"},
			#{'name':'webradiow', 'duration':9999, 'conditional':"db['actPlayer'] == 'Webradio'"},
		],
		'conditional': "db['state']=='stop' or db['state']=='pause'"
		#'conditional': "False"
	},
	{
		'name':'seqVolume',
		'coordinates':(0,0),
		'canvases': [
			{'name':'volume_changed', 'duration':1},
		],
		'conditional': "db['volume'] != dbp['volume']",
		'minimum':3,
	},
	{
		'name':'seqPlayer',
		'coordinates':(0,0),
		'canvases': [
			{'name':'player', 'duration':1},
		],
		'conditional': "db['actPlayer'] != dbp['actPlayer']",
		'minimum':3,
	},
	{
		'name': 'seqSplash',
		'canvases': [
			{'name':'splashw', 'duration':999, 'conditional':'True' },
		],
		'conditional': "db['state']=='starting'"
	},
]
