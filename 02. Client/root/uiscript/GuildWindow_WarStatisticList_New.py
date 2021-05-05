import uiScriptLocale

BOARD_WIDTH = 350
BOARD_HEIGHT = 350+120
PAGE_BUTTON = BOARD_WIDTH/2
ROOT_PATH = "d:/ymir work/ui/game/guild/"
LOCALE_PATH = "d:/ymir work/ui/akira_page/"

window = {
	"name" : "GuildWarStatisticListWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : BOARD_WIDTH-13,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":BOARD_WIDTH/2, "y":3, "text":"Lonca Savaþ Ýstatistikleri", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "GuildWarStatisticTiTleImg",
					"type" : "image",
					"x" : 18,
					"y" : 37,
					"image" : ROOT_PATH+"dragonlairranking/ranking_list_menu.sub",
					"children" :
					(
						## Text
						{ "name" : "MemberCount", "type" : "text", "x" : 15, "y" : 4,  "text" : "Sýra", },
						{ "name" : "MemberName", "type" : "text", "x" : 105, "y" : 4,  "text" : "Ýsim", },
						{ "name" : "MemberDeath", "type" : "text", "x" : 195, "y" : 4, "text" : "Ölüm", },
						{ "name" : "MemberKilling", "type" : "text", "x" : 250, "y" : 4, "text" : "Öldürme", },
					),
				},
				{
					"name" : "PageBar", "type" : "slotbar",
					"x" : PAGE_BUTTON-9, "y" : BOARD_HEIGHT-37,
					"width" : 18,
					"height" : 18,

					"children" :
					(
						{
							"name" : "PageText",
							"type" : "text",

							"x" : 0,
							"y" : 0,
							"all_align" : "",
							"text" : "1",
						},
					),
				},
				{
					"name" : "first_prev_button", "type" : "button",
					"x" : PAGE_BUTTON-60, "y" : BOARD_HEIGHT-33,

					"default_image" : LOCALE_PATH + "first_prev_btn_01.sub",
					"over_image" 	: LOCALE_PATH + "first_prev_btn_02.sub",
					"down_image" 	: LOCALE_PATH + "first_prev_btn_01.sub",
				},
				{
					"name" : "prev_button", "type" : "button",
					"x" : PAGE_BUTTON-40, "y" : BOARD_HEIGHT-33,

					"default_image" : LOCALE_PATH + "prev_btn_01.sub",
					"over_image" 	: LOCALE_PATH + "prev_btn_02.sub",
					"down_image" 	: LOCALE_PATH + "prev_btn_01.sub",
				},
				{
					"name" : "next_button", "type" : "button",
					"x" : PAGE_BUTTON+40-9, "y" : BOARD_HEIGHT-33,

					"default_image" : LOCALE_PATH + "next_btn_01.sub",
					"over_image" 	: LOCALE_PATH + "next_btn_02.sub",
					"down_image" 	: LOCALE_PATH + "next_btn_01.sub",
				},
				{
					"name" : "last_next_button", "type" : "button",
					"x" : PAGE_BUTTON+60-9, "y" : BOARD_HEIGHT-33,

					"default_image" : LOCALE_PATH + "last_next_btn_01.sub",
					"over_image" 	: LOCALE_PATH + "last_next_btn_02.sub",
					"down_image" 	: LOCALE_PATH + "last_next_btn_01.sub",
				},
			),
		},
	),
}

