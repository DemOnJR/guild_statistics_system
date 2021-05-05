#Search:

		onPressKeyDict[app.DIK_F12]	= lambda : self.interface.OpenHelpWindow()

#Add belove:

		onPressKeyDict[app.DIK_TAB]	= lambda : self.LoncaIstatistikOpen()

#Search:

"MyShopPriceList"						: self.__PrivateShop_PriceList,

#Add belove:

			"lonca_istatistik"			: self.__OpenGuildWarRank,

#Add to end:

	def LoncaIstatistikOpen(self):
		if self.interface:
			if constInfo.IsGuildWarStatShow:
				self.interface.CloseGuildWarRankingList()
			else:
				net.SendChatPacket("/lonca_istatistik")

	def __OpenGuildWarRank(self, tokenn):
		token = tokenn.split("|")
		if token[0] == "Open":
			if self.interface:
				self.interface.OpenGuildWarRankingList()
		elif token[0] == "Append":
			if self.interface:
				self.interface.AppendGuildWarRankingList(str(token[1]), int(token[2]), int(token[3]), int(token[4]))