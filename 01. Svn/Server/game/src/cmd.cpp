//Search:

struct command_info cmd_info[] =

//Add on:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
ACMD(do_lonca_istatistik);
#endif

//Search:

{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}

//Add on:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	{ "lonca_istatistik",		do_lonca_istatistik,			0,			POS_DEAD,	GM_PLAYER	},
#endif