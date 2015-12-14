'''
HELLOOOOOOOO there
'''

class game:
  # Class variables ----------------------------------------------------------
  OPEN_SPACE = 0

  PLAYER_TIE = 0
  PLAYER_ONE = 1
  PLAYER_TWO = 2

  OFF = 0
  ON = 1
  

  # Constructor --------------------------------------------------------------
  def __init__(self):
    self.__turn = game.PLAYER_ONE
    self.__gameStatus = game.ON

    self.__firstToGo = game.PLAYER_ONE
    
    self.__playerOne = 'Player One'
    self.__playerTwo = 'Player Two'

    self.__playerOneColor = 'red'
    self.__playerTwoColor = 'yellow'

    self.__scoreOne = 0
    self.__scoreTwo = 0

    self.__playerOneAI = 0
    self.__playerTwoAI = 0
    
    self.__gameArray = []
    for column in range(7):
      columnArray = []
      for row in range(6):
        columnArray.append(game.OPEN_SPACE)
      self.__gameArray.append(columnArray)

    
  # Predicates ---------------------------------------------------------------
##  def gameOver(self):
##    return 

  # Accessors ----------------------------------------------------------------
  def getTurn(self):
    return self.__turn

  def getPlayerOneName(self):
    return self.__playerOne

  def getPlayerTwoName(self):
    return self.__playerTwo

  # returns whose turn it is
  def getPlayerTurn(self):
    name = self.getPlayerOneName()
    if self.getTurn() == game.PLAYER_TWO:
      name = self.getPlayerTwoName()
    return name

  def getPlayerOneColor(self):
    return self.__playerOneColor

  def getPlayerTwoColor(self):
    return self.__playerTwoColor
    
  def getPlayerOneScore(self):
    return self.__scoreOne

  def getPlayerTwoScore(self):
    return self.__scoreTwo

  def getGameArray(self):
    return self.__gameArray

  def getGameStatus(self):
    return self.__gameStatus

  # Mutators -----------------------------------------------------------------

  # changes name
  def changeName(self, player, name):
    if player == game.PLAYER_ONE:
      self.__playerOne = name
    else:
      self.__playerTwo = name

  # changes color
  def changePlayerColor(self, player, newColor):
    if player == game.PLAYER_ONE:
      self.__playerOneColor = newColor
    else:
      self.__playerTwoColor = newColor

  # sets who goes first
  def setGoFirst(self, player):
    self.__firstToGo = player

  # sets turn to whoever goes first
  def setFirstTurn(self):
    self.__turn = self.__firstToGo

  # toggles computers if checkbutton checked
  def setComputers(self, playerOneStatus, playerTwoStatus):
    self.__playerOneAI = playerOneStatus
    self.__playerTwoAI = playerTwoStatus
    
  # Switches game status and wipes board
  def newGame(self):
    self.__gameStatus = game.ON
    for col in range(len(self.getGameArray())):
      for row in range(len(self.getGameArray()[0])):
        self.getGameArray()[col][row] = game.OPEN_SPACE

  # winner increments score by 1
  def incrementScore(self):
    if self.getTurn() == game.PLAYER_ONE:
      self.__scoreOne += 1
    elif self.getTurn() == game.PLAYER_TWO:
      self.__scoreTwo += 1

##  def startTurn(self):
    
    
  def switchTurn(self):
    if self.__turn == game.PLAYER_ONE:
      self.__turn = game.PLAYER_TWO
    else:
      self.__turn = game.PLAYER_ONE

  def possibleMove(self,xCoord):
    count = 0
    yCoord = len(self.__gameArray[xCoord])
    while count < len(self.__gameArray[xCoord]):
      if self.__gameArray[xCoord][count] == game.OPEN_SPACE and count < yCoord:
        yCoord = count
      count += 1
    return yCoord
      
  def endGame(self):
    self.__gameStatus = game.OFF

  # changes circle color
  def changeColor(self, xCoord, yCoord):
    self.__gameArray[xCoord][yCoord] = self.getTurn()

  # check if won by vertical
  def checkVertical(self):
    player = self.getTurn()
    for col in self.__gameArray:
      if col[2] == player and col[3] == player:
        if col[0] == player and col[1] == player or\
           col[1] == player and col[4] == player or\
           col[4] == player and col[5] == player:
          self.endGame()
          
  # check if won by horizontal
  def checkHorizontal(self):
    player = self.getTurn()
    for col in range(len(self.__gameArray[0])):
      row = [value[col] for value in self.__gameArray]
##      print(row)
      if row[1] == player and row[2] == player and row[3] == player:
        if row[0] == player or row[4] == player:
          self.endGame()
      elif row[3] == player and row[4] == player and row[5] == player:
        if row[2] == player or row[6] == player:
          self.endGame()

  # check if won by diagonal
  def checkDiag(self):
    player = self.getTurn()
    #downright direction
    for row in range(len(self.__gameArray) // 2, len(self.__gameArray[0])):
      for col in range(len(self.__gameArray) // 2 + 1):
        if self.__gameArray[col][row] == player and \
           self.__gameArray[col + 1][row - 1] == player and \
           self.__gameArray[col + 2][row - 2] == player and \
           self.__gameArray[col + 3][row - 3] == player:
          self.endGame()

    if self.getGameStatus() == 1:
    #downleft direction
      for row in range(len(self.__gameArray) // 2):
        for col in range(len(self.__gameArray) // 2 + 1):
##          print(col,row)
          if self.__gameArray[col][row] == player and \
             self.__gameArray[col + 1][row + 1] == player and \
             self.__gameArray[col + 2][row + 2] == player and \
             self.__gameArray[col + 3][row + 3] == player:
            self.endGame()

  # check if no moves left
  def checkTie(self):
    end = True
    for row in self.__gameArray:
      if game.OPEN_SPACE in row:
        end = False
    if end:
      self.__turn = game.PLAYER_TIE
      self.endGame()
      
  # checks if game won
  def checkWin(self):
    self.checkHorizontal()
    if self.getGameStatus() == game.ON:
      self.checkDiag()
    if self.getGameStatus() == game.ON:
      self.checkVertical()
    if self.getGameStatus() == game.ON:
      self.checkTie()
    

  # Convert to str -----------------------------------------------------------
  def __str__(self):
    return 'Connect Four Game'

##gameone = game()
##gameone.changeColor(0, 0)
##print(gameone.getGameArray())
##print(gameone.getGameArray())
#print(gameone.possibleMove(6))
#gameone.checkWin()
#print(gameone.getGameArray())

