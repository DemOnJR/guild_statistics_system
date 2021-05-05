//Search:

	void			SetLastAttacked(DWORD time);

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	void			SetLastLoncaIstatistikLastTime(int time) { m_dwLonIstLastTime = time; }
	int				GetLastLoncaIstatistikLastTime() const	{ return m_dwLonIstLastTime; }
#endif

//Search:

	bool			m_bStaminaConsume;

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	int				m_dwLonIstLastTime;
#endif