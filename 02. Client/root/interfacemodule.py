#Add imports:

import uiGuildWarStatisticNew

#Search:

	def __MakeCubeResultWindow(self):
		self.wndCubeResult = uiCube.CubeResultWindow()
		self.wndCubeResult.LoadWindow()
		self.wndCubeResult.Hide()

#Add belove:

	def __MakeGuildWarRankingListWindow(self):
		self.wndGuildWarRankingList = uiGuildWarStatisticNew.GuildWarStatisticListWindow()
		self.wndGuildWarRankingList.LoadWindow()
		self.wndGuildWarRankingList.Hide()

#Search:

		if self.wndItemSelect:
			self.wndItemSelect.Destroy()

#Add belove:

		if self.wndGuildWarRankingList:
			self.wndGuildWarRankingList.Destroy()

#Search:

		del self.wndItemSelect

#Add belove:

		del self.wndGuildWarRankingList

#Search:

	def __HideWindows(self):

#Add above:

	def OpenGuildWarRankingList(self):
		self.wndGuildWarRankingList.Open()

	def CloseGuildWarRankingList(self):
		self.wndGuildWarRankingList.Close()

	def AppendGuildWarRankingList(self, name, death, killing, onoff):
		self.wndGuildWarRankingList.AppendWarList(name, death, killing, onoff)