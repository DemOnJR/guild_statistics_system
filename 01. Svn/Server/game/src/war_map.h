//Search:

public:
	friend class CGuild;

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	typedef struct SGuildPlayerTable
	{
		DWORD	dwGuildID;
		const char* szName;
		BYTE	bKill;
		BYTE	bDead;
	} TGuildPlayerTable;

	typedef std::map<DWORD, TGuildPlayerTable *> TGuildPlayerDataMap;
#endif

//Search:

	void	SendScorePacket(BYTE bIdx, LPDESC d = NULL);

//Add belove:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	void	NewPlayerStatistics(DWORD dwPID, const char * szName, DWORD dwGuildID, bool bKill = true);
	void	LoadGuildWarStatistics(LPCHARACTER ch, BYTE bOnOff);
	TGuildPlayerTable * GetStatistics(DWORD dwPID);
#endif

//Search:

	CHARACTER_SET m_set_pkChr;

//Add belove:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
protected:
	TGuildPlayerDataMap	m_GuildPlayerTableDataMap;
#endif