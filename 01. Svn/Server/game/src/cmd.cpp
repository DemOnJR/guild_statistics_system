//Search:

struct command_info cmd_info[] =

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
ACMD(do_lonca_istatistik);
#endif

//Search:

{ "\n",		NULL,			0,			POS_DEAD,	GM_IMPLEMENTOR	}

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	{ "lonca_istatistik",		do_lonca_istatistik,			0,			POS_DEAD,	GM_PLAYER	},
#endif