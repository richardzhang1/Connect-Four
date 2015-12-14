from tkinter import *
from gameplay import *
import random


class gameBoard:
  # Class variables --------------------------------------------------------
  ENTRY_BOX_WIDTH = 14
  GAME_DIMENSIONS = 0
  CUSTOM_FONT = ('Comic Sans MS', 11)
  COLORS = ['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'yellow']
  
  NUM_COLUMNS = 7
  NUM_ROWS = 6
  CIRCLE_SIZE = 60
  GAP = 10

  COLUMN_ONE = 65
  COLUMN_TWO = 125
  COLUMN_THREE = 185
  COLUMN_FOUR = 245
  COLUMN_FIVE = 305
  COLUMN_SIX = 365
  
  # Constructor ------------------------------------------------------------
  def __init__(self):
    # Window
    self.__win = Tk()
    self.__win.wm_title('Connect Four Game')

    # Initialize game
    self.__game = game()

    # New Game Button
    Button(self.__win, text = 'New Game', command = self.newGame, \
           font = gameBoard.CUSTOM_FONT).grid \
           (row = 0, column = 0, columnspan = 5)
    
    # Tells which player to go
    self.__playerTurn = StringVar()
    self.__playerTurn.set('Welcome to Connect Four! Click board to begin.')
    self.__whoseTurn = Label(self.__win, textvariable = self.__playerTurn, \
                             font = gameBoard.CUSTOM_FONT). \
                             grid(row = 0, column = 5)
    
    # Player One Name
    Label(self.__win, text = 'Player One: '). \
                      grid(row = 1, column = 0, \
                           sticky = S + W, columnspan = 2)
    self.__nameOne = StringVar()
    self.__nameOne.set(self.__game.getPlayerOneName())
    self.__playerOneName = Entry(self.__win, \
                                 textvariable = self.__nameOne, \
                                 width = gameBoard.ENTRY_BOX_WIDTH)
    self.__playerOneName.grid(row = 1, column = 1, \
                                sticky = S + E, columnspan = 3)

    # Player One Color; default 'red'
    Label(self.__win, text = 'Color: ').grid(row = 2, column = 0)
    self.__playerOneColor = StringVar()
    self.__playerOneColor.set(self.__game.getPlayerOneColor())
    self.__colorOne = OptionMenu(self.__win, self.__playerOneColor, \
                                 *gameBoard.COLORS)
    self.__colorOne.grid(row = 2, column = 1)
    
    # Player One Score
    Label(self.__win, text = 'Score: ').grid(row = 2, column = 2)
    self.__playerOneScore = IntVar()
    self.__playerOneScore.set(self.__game.getPlayerOneScore())
    self.__scoreOne = Label(self.__win, \
                      textvariable = self.__playerOneScore). \
                      grid(row = 2, column = 3)

    # Player One is computer?
    self.__playerOneCpu = IntVar()
    self.__playerOneCpu.set(0)
    self.__computerOne = Checkbutton(self.__win, text = ' is a computer', \
                           variable = self.__playerOneCpu). \
                           grid(row = 3, column = 0, \
                           sticky = N, columnspan = 5)

    # Player Two Name
    Label(self.__win, text = 'Player Two: '). \
                      grid(row = 4, column = 0, \
                           sticky = S + W, columnspan = 2)
    self.__nameTwo = StringVar()
    self.__nameTwo.set(self.__game.getPlayerTwoName())
    self.__playerTwoName = Entry(self.__win, \
                                 textvariable = self.__nameTwo, \
                                 width = gameBoard.ENTRY_BOX_WIDTH)
    self.__playerTwoName.grid(row = 4, column = 1, \
                                sticky = S + E, columnspan = 3)

    # Player Two Color; default 'red'
    Label(self.__win, text = 'Color: ').grid(row = 5, column = 0)
    self.__playerTwoColor = StringVar()
    self.__playerTwoColor.set(self.__game.getPlayerTwoColor())
    self.__colorTwo = OptionMenu(self.__win, self.__playerTwoColor, \
                                 *gameBoard.COLORS).grid(row = 5, column = 1)

    # Player Two Score
    Label(self.__win, text = 'Score: ').grid(row = 5, column = 2)
    self.__playerTwoScore = IntVar()
    self.__playerTwoScore.set(self.__game.getPlayerTwoScore())
    self.__scoreTwo = Label(self.__win, textvariable = \
                            self.__playerTwoScore).grid(row = 5, column = 3)

    # Player One is computer?
    self.__playerTwoCpu = IntVar()
    self.__playerTwoCpu.set(0)
    self.__computerTwo = Checkbutton(self.__win, text = ' is a computer', \
                           variable = self.__playerTwoCpu). \
                           grid(row = 6, column = 0, \
                           sticky = N, columnspan = 5)


    # Who goes first?
    Label(self.__win, text = 'Who is going first?', \
          font = gameBoard.CUSTOM_FONT). \
          grid(row = 7, column = 0, sticky = S, columnspan = 5)
    self.__playerOneFirst = Button(self.__win, text = 'Player One', \
                                   bg = 'light gray', \
                                   command = self.playerOneGoesFirst)
    self.__playerOneFirst.grid(row = 8, column = 0, columnspan = 2)
    
    self.__playerTwoFirst = Button(self.__win, text = 'Player Two', \
                                   command = self.playerTwoGoesFirst)
    self.__playerTwoFirst.grid(row = 8, column = 1, \
                               sticky = E, columnspan = 2)
    
    # Create the playing board
    self.__frame = Frame(self.__win)    
    self.__frame.grid(row = 1, column = 5, rowspan = 10)

    self.__circles = Canvas(self.__frame, bg = 'powder blue', \
                            height= 370, width = 430)
    self.__grid = []

    # Iterate circles in canvas
    for col in range(gameBoard.NUM_COLUMNS):
      singleCol = []
      for row in range(gameBoard.NUM_ROWS):
        singleCol.append(self.__circles.create_oval(col * \
                           gameBoard.CIRCLE_SIZE + gameBoard.GAP, \
                           row * gameBoard.CIRCLE_SIZE + gameBoard.GAP, \
                           (col+1) * gameBoard.CIRCLE_SIZE, \
                           (row+1) * gameBoard.CIRCLE_SIZE, fill='white'))
      self.__grid.append(singleCol)
    self.__circles.grid()

    self.__circles.bind('<Button-1>', self.move)

    self.__turn = 0



  # Mutators --------------------------------------------------------------

  # Starts game
  # Applies new information and wipes boards
  def newGame(self):
    # sets names
    self.__game.changeName(self.__game.PLAYER_ONE, self.__playerOneName.get())
    self.__game.changeName(self.__game.PLAYER_TWO, self.__playerTwoName.get())

    # sets colors
    self.__game.changePlayerColor(self.__game.PLAYER_ONE, \
                                  self.__playerOneColor.get())
    self.__game.changePlayerColor(self.__game.PLAYER_TWO, \
                                  self.__playerTwoColor.get())

    # sets who goes first
    self.__game.setFirstTurn()

    # sets computers
    self.__game.setComputers(self.__playerOneCpu.get(), \
                             self.__playerTwoCpu.get())

##    print(self.__game.getPlayerOneName())
##    print(self.__game.getPlayerTwoName())

    self.__playerTurn.set(self.__game.getPlayerTurn() + "'s Turn")
    self.__game.newGame()
    for col in range(7):
      for row in range(6):
        self.__circles.itemconfig(self.__grid[col][row], fill='white')

  # change bottom button color
  def playerOneGoesFirst(self):
    self.__playerOneFirst.configure(bg = 'light gray')
    self.__playerTwoFirst.config(bg = 'SystemButtonFace')
    self.__game.setGoFirst(self.__game.PLAYER_ONE)

  # change bottom button color
  def playerTwoGoesFirst(self):
    self.__playerTwoFirst.configure(bg = 'light gray')
    self.__playerOneFirst.config(bg = 'SystemButtonFace')
    self.__game.setGoFirst(self.__game.PLAYER_TWO)

  def updateScore(self):
    self.__playerOneScore.set(self.__game.getPlayerOneScore())
    self.__playerTwoScore.set(self.__game.getPlayerTwoScore())
    
  # displays winner
  def updateWinner(self):
    if self.__game.getTurn() == self.__game.PLAYER_ONE:
      self.__playerTurn.set('Winner is %s!  Click New Game to play again.' \
                            %(self.__game.getPlayerTurn()))
    elif self.__game.getTurn() == self.__game.PLAYER_TWO:
      self.__playerTurn.set('Winner is %s!  Click New Game to play again.' \
                            %(self.__game.getPlayerTurn()))
    else:
      self.__playerTurn.set('No Winner!  Click New Game to play again.')
                
  # Plots circle on grid
  def move(self,event):
##    print(self.__game.getGameArray())
##    print(self.__game.getGameStatus())
    # Prevents moves if game is over
    if self.__game.getGameStatus():
      # Gets x-coordinate
      if event.x >= gameBoard.COLUMN_SIX:
        xCoord = 6
      elif event.x >= gameBoard.COLUMN_FIVE:
        xCoord = 5
      elif event.x >= gameBoard.COLUMN_FOUR:
        xCoord = 4
      elif event.x >= gameBoard.COLUMN_THREE:
        xCoord = 3
      elif event.x >= gameBoard.COLUMN_TWO:
        xCoord = 2
      elif event.x >= gameBoard.COLUMN_ONE:
        xCoord = 1
      else:
        xCoord = 0

      # Get lowest blank space in column
      # In other words, gets y-coordinate
      yCoord = self.__game.possibleMove(xCoord)

      # Checks if y-coordinate is on gameboard
      if yCoord < gameBoard.NUM_ROWS:
        # Gets color
        color = self.__game.getPlayerOneColor()
        if self.__game.getTurn() == self.__game.PLAYER_TWO:
          color = self.__game.getPlayerTwoColor()

        # Shades in circle on grid
        self.__circles.itemconfig(self.__grid[xCoord][5 - yCoord], \
                                  fill = color)
        self.__game.changeColor(xCoord, yCoord)

        # Checks for win; stops game if won
        self.__game.checkWin()

        # Increments score and displays winner
        if not self.__game.getGameStatus():
          self.__game.incrementScore()
          self.updateScore()
          
          self.updateWinner()
        else:
          self.__game.switchTurn()
          self.__playerTurn.set(self.__game.getPlayerTurn() + "'s Turn")
        
    mainloop()

gameBoard()
