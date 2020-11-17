from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

import numpy as np

app = Flask(__name__)


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


class Game():

	isDraw = False
	isWinner = False

	winner = ""

	def __init__(self, player):
		self.player = player

	def setPlayerTurn(self, player):
		self.player = player

	def getPlayerTurn(self):
		return self.player




class Board():
	numOfOccupied = 0

	def __init__(self, n):
		self.n = n
		self.array = np.full([n, n], None)

	def makeMove(self, r, c, value):
		self.array[r][c] = value

	def getBoard(self):
		return self.array

	def makeNewBoard(self):
		self.array = np.full([self.n, self.n], None)
		self.numOfOccupied = 0

	def getn(self):
		return self.n

	def isFull(self):
		return self.numOfOccupied == (self.n * self.n)


	def win_indexes(self):
		n = self.n

		# Rows
		for r in range(n):
			yield [(r, c) for c in range(n)]
		# Columns
		for c in range(n):
			yield [(r, c) for r in range(n)]

		# Diagonal top left to bottom right
		yield [(i, i) for i in range(n)]
		# Diagonal top right to bottom left
		yield [(i, n - 1 - i) for i in range(n)]


	def is_winner(self, playerToken):

		board = self.getBoard()

		for indexes in self.win_indexes():
			if all(board[r][c] == playerToken for r, c in indexes):
				return True
		return False



newBoard = Board(3)
board = newBoard.getBoard()
newGame = Game("X")


@app.route("/")
def index():
	winner = winnerFound(newBoard)

	if(winner[0] == True):
		newGame.isWinner = True
		newGame.setPlayerTurn(winner[1])

	return render_template("game.html", game=newBoard.getBoard(), turn=newGame.getPlayerTurn(), winnerFound=newGame.isWinner, winner=newGame.getPlayerTurn(), draw=newGame.isDraw, size = newBoard.getn())


@app.route("/play/<int:row>/<int:col>")
def play(row, col):

	newBoard.makeMove(row, col, newGame.getPlayerTurn())
	newBoard.numOfOccupied += 1

	if(newGame.getPlayerTurn() == "X"):
		newGame.setPlayerTurn("O")
	else:
		newGame.setPlayerTurn("X")

	return redirect(url_for("index"))


@app.route("/reset")
def reset():
	newBoard.makeNewBoard()
	newGame.setPlayerTurn("X")
	newGame.isWinner = False
	newGame.isDraw = False
	return redirect(url_for("index"))


def winnerFound(board):

	if (board.is_winner("X")):
		return [True, "X"]
	elif(board.is_winner("O")):
		return [True, "O"]
	elif(newBoard.numOfOccupied == (newBoard.getn())**2):
		newGame.isDraw = True
		return[False, "draw"]
	else:
		return [False, False]


if __name__ == "__main__":
    app.run()

