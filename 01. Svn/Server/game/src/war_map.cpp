//Search:

	SetEndEvent(event_create(war_end_event, info, PASSES_PER_SEC(10)));

//Add belove:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
	for (const auto& it : m_GuildPlayerTableDataMap)
		delete it.second;

	m_GuildPlayerTableDataMap.clear();
#endif

//Search:

void CWarMap::OnKill(LPCHARACTER killer, LPCHARACTER ch)

//Add above:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
CWarMap::TGuildPlayerTable* CWarMap::GetStatistics(DWORD dwPID)
{
	const auto& it = m_GuildPlayerTableDataMap.find(dwPID);
	return it != m_GuildPlayerTableDataMap.end() ? it->second : nullptr;
}

void CWarMap::NewPlayerStatistics(DWORD dwPID, const char * szName, DWORD dwGuildID, bool bKill)
{
	const auto& pStatistics = GetStatistics(dwPID);

	if (pStatistics)
	{
		sys_err("Already Inserted Player : ID: %d", dwPID);
		return;
	}

	const auto& pGuildPlayerData = new TGuildPlayerTable;
	pGuildPlayerData->dwGuildID = dwGuildID;
	pGuildPlayerData->szName = szName;
	pGuildPlayerData->bKill = bKill ? 1 : 0;
	pGuildPlayerData->bDead = !bKill ? 1 : 0;
	m_GuildPlayerTableDataMap.emplace(dwPID, pGuildPlayerData);
}

void CWarMap::LoadGuildWarStatistics(LPCHARACTER ch, BYTE bOnOff)
{
	if (!ch || !ch->GetGuild()) 
		return;

	const DWORD dwGuildID1 = ch->GetGuild()->GetID();

	for (const auto& it : m_GuildPlayerTableDataMap)
	{
		const auto& pGuildStaticsTable = it.second;
		if (pGuildStaticsTable)
		{
			const DWORD dwGuildID2 = pGuildStaticsTable->dwGuildID;
			if (dwGuildID1 == dwGuildID2)
			{
				char szName[CHARACTER_NAME_MAX_LEN + 1];
				strlcpy(szName, pGuildStaticsTable->szName, sizeof(szName));
				const BYTE bDead = pGuildStaticsTable->bDead;
				const BYTE bKill = pGuildStaticsTable->bKill;
				char szStatistics[128];
				snprintf(szStatistics, sizeof(szStatistics), "Append|%s|%u|%u|%u", szName, bDead, bKill, bOnOff);
				ch->ChatPacket(CHAT_TYPE_COMMAND, "lonca_istatistik %s", szStatistics);
			}
		}
	}

	ch->ChatPacket(CHAT_TYPE_COMMAND, "lonca_istatistik Open");
}
#endif

//Search:

	if (!GetTeamIndex(dwDeadGuild, idx))
		return;

//Add belove:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
		const auto& pGuildPlayerStatistics = GetStatistics(ch->GetPlayerID());
		if (!pGuildPlayerStatistics)
			NewPlayerStatistics(ch->GetPlayerID(), ch->GetName(), dwDeadGuild, false);
		else
			pGuildPlayerStatistics->bDead += 1;

		const auto& pGuildKillerStatistics = GetStatistics(killer->GetPlayerID());
		if (!pGuildKillerStatistics)
			NewPlayerStatistics(killer->GetPlayerID(), killer->GetName(), dwKillerGuild);
		else
			pGuildKillerStatistics->bKill += 1;
#endif