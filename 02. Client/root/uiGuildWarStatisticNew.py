import ui, player, uiScriptLocale, app, constInfo, net, uiCommon, chat

line_max_count = 15

class GuildWarStatisticListWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__statisticButtons = {}
		self.__statisticData = {}
		self.page = 1
		self.xStart = 0
		self.yStart = 0
		self.on_off = 0
		self.questionDialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.__statisticButtons = {}
		self.__statisticData = {}
		self.page = 1
		self.xStart = 0
		self.yStart = 0
		self.on_off = 0
		self.questionDialog = None

	def LoadWindow(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "UIScript/GuildWindow_WarStatisticList_New.py")
		except:
			import exception
			exception.Abort("RankingList.LoadWindow.LoadObject")
		try:
			self.GetChild("TitleBar").SetCloseEvent(self.Close)
			self.TitleName = self.GetChild("TitleName")
			self.first_prev_btn = self.GetChild("first_prev_button")
			self.last_next_btn = self.GetChild("last_next_button")
			self.prev_btn = self.GetChild("prev_button")
			self.next_btn = self.GetChild("next_button")
			self.page_text = self.GetChild("PageText")

		except:
			import exception
			exception.Abort("RankingList.LoadWindow.BindObject")

		self.first_prev_btn.SetEvent(ui.__mem_func__(self.__FirstPrevButton))
		self.last_next_btn.SetEvent(ui.__mem_func__(self.__LastNextButton))
		self.prev_btn.SetEvent(ui.__mem_func__(self.__PrevButton))
		self.next_btn.SetEvent(ui.__mem_func__(self.__NextButton))
		self.next_btn.Show(), self.last_next_btn.Hide()
		self.prev_btn.Show(), self.first_prev_btn.Hide()

	def __CreateButton(self, page):
		self.page = page
		self.page_text.SetText(str(page))
		for i in xrange(line_max_count):
			i+=1
			self.__statisticButtons[i] = {}

		for i,j in self.__statisticButtons.iteritems():
			for item in self.__statisticButtons[i].itervalues():
				item.Hide()

		for j in xrange(line_max_count):
			self.__statisticButtons[page][j] = ui.MakeButton(self, 20, 65 + j*24 , "", "d:/ymir work/ui/game/guild/dragonlairranking/", "ranking_list_button01.sub", "ranking_list_button02.sub", "ranking_list_button02.sub")

			self.__statisticButtons[page][j].SetEvent(ui.__mem_func__(self.__SelectButton), j)

			self.__statisticButtons[page][j].pos = ui.TextLine()
			self.__statisticButtons[page][j].pos.SetParent(self.__statisticButtons[page][j])
			self.__statisticButtons[page][j].pos.SetText("")
			self.__statisticButtons[page][j].pos.SetPosition(18, 2)
			self.__statisticButtons[page][j].pos.Show()

			self.__statisticButtons[page][j].MemberName = ui.TextLine()
			self.__statisticButtons[page][j].MemberName.SetParent(self.__statisticButtons[page][j])
			self.__statisticButtons[page][j].MemberName.SetText("")
			self.__statisticButtons[page][j].MemberName.SetPosition(62, 2)
			self.__statisticButtons[page][j].MemberName.Show()

			self.__statisticButtons[page][j].MemberDeath = ui.TextLine()
			self.__statisticButtons[page][j].MemberDeath.SetParent(self.__statisticButtons[page][j])
			self.__statisticButtons[page][j].MemberDeath.SetText("")
			self.__statisticButtons[page][j].MemberDeath.SetPosition(154, 2)
			self.__statisticButtons[page][j].MemberDeath.Show()

			self.__statisticButtons[page][j].MemberKilling = ui.TextLine()
			self.__statisticButtons[page][j].MemberKilling.SetParent(self.__statisticButtons[page][j])
			self.__statisticButtons[page][j].MemberKilling.SetText("")
			self.__statisticButtons[page][j].MemberKilling.SetPosition(193, 2)
			self.__statisticButtons[page][j].MemberKilling.Show()
		self.__Refresh()

	def __SelectButton(self, gelen):
		getname = self.__statisticButtons[self.page][gelen].MemberName.GetText()
		if not self.__Exists(getname):
			return

		if self.on_off == 1:
			return

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(getname + " adlý oyuncuyu savaþtan atmak istiyor musun?")
		questionDialog.SetAcceptEvent(lambda arg=getname: self.SelectButton(getname))
		questionDialog.SetCancelEvent(lambda arg=0: self.SelectButton(arg))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def SelectButton(self, arg):
		if not self.questionDialog:
			return
		if arg:
			net.SendChatPacket("/savasat %s" % (str(arg)))
		self.questionDialog.Close()
		self.questionDialog = None

	def __PrevButton(self):
		if self.page-1 < 1:
			return
		self.page-=1
		self.__CreateButton(self.page)

	def __NextButton(self):
		pages = (self.page)*line_max_count
		if pages >= len(self.__statisticData):
			return

		self.page+=1
		self.__CreateButton(self.page)

	def __FirstPrevButton(self):
		self.page=1
		self.__CreateButton(self.page)

	def __LastNextButton(self):
		self.page=5
		self.__CreateButton(self.page)

	def __Refresh(self):
		if self.page > 1:
			self.prev_btn.Show(), self.first_prev_btn.Show()
		else:
			self.prev_btn.Hide(), self.first_prev_btn.Hide()

		pages = (self.page-1)*line_max_count
		for i in xrange(line_max_count):
			if pages+i >= len(self.__statisticData):
				break

			self.__statisticButtons[self.page][i].pos.SetText(str(pages+i+1))
			self.__statisticButtons[self.page][i].MemberName.SetText(self.__statisticData[pages+i][0])
			self.__statisticButtons[self.page][i].MemberDeath.SetText(str(self.__statisticData[pages+i][1]))
			self.__statisticButtons[self.page][i].MemberKilling.SetText(str(self.__statisticData[pages+i][2]))
			self.__statisticButtons[self.page][i].MemberName.SetPosition(-38 - len(self.__statisticData[pages+i][0]), 0)
			self.__statisticButtons[self.page][i].MemberName.SetHorizontalAlignCenter()
			self.__statisticButtons[self.page][i].MemberName.SetVerticalAlignCenter()
			self.__statisticButtons[self.page][i].MemberName.SetWindowHorizontalAlignCenter()
			self.__statisticButtons[self.page][i].MemberName.SetWindowVerticalAlignCenter()
			self.__statisticButtons[self.page][i].MemberDeath.SetPosition(200 - len(str(self.__statisticData[pages+i][1])), 0)
			self.__statisticButtons[self.page][i].MemberDeath.SetWindowVerticalAlignCenter()
			self.__statisticButtons[self.page][i].MemberDeath.SetVerticalAlignCenter()
			self.__statisticButtons[self.page][i].MemberKilling.SetPosition(265 - len(str(self.__statisticData[pages+i][2])), 0)
			self.__statisticButtons[self.page][i].MemberKilling.SetWindowVerticalAlignCenter()
			self.__statisticButtons[self.page][i].MemberKilling.SetVerticalAlignCenter()

	def __Exists(self, name):
		for i in xrange(len(self.__statisticData)):
			if name in self.__statisticData[i]:
				return TRUE

		return FALSE

	def AppendWarList(self, name, death, killing, onoff):
		if self.__Exists(name):
			return
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Error")

		self.__statisticData[len(self.__statisticData)] = (name, death, killing)
		self.on_off = onoff

	def Open(self):
		ui.ScriptWindow.Show(self)
		self.SetCenterPosition()
		self.__CreateButton(1)
		(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()
		constInfo.IsGuildWarStatShow = 1

	def Close(self):
		self.Hide()
		self.__statisticData = {}
		constInfo.IsGuildWarStatShow = 0
		return TRUE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
