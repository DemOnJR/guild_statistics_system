//Add to end:

#ifdef ENABLE_GUILD_STATISTICS_SYSTEM
ACMD(do_lonca_istatistik)
{
	if (quest::CQuestManager::instance().GetEventFlag("lonca_istatistik_disable") == 1)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Sistem suan icin devre disi!");
		return;
	}

	int iPulse = thecore_pulse();

	if (iPulse - ch->GetLastLoncaIstatistikLastTime() < passes_per_sec * 2)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Biraz beklemelisin.");
		return;
	}

	ch->SetLastLoncaIstatistikLastTime(iPulse);

	if (!ch->GetGuild())
		return;

	auto g = ch->GetGuild();
	if (!g->UnderAnyWar())
	{
		ch->ChatPacket(CHAT_TYPE_INFO, ("<Guild> Sadece lonca savaþýnda kullanabilirsin."));
		return;
	}

	BYTE onoff = 1;
	auto lider = g->GetMember(ch->GetPlayerID());
	if (lider && lider->grade == GUILD_LEADER_GRADE)
		onoff = 0;

	auto pMap = CWarMapManager::instance().Find(ch->GetMapIndex());

	if (pMap)
		pMap->LoadGuildWarStatistics(ch, onoff);
}
#endif