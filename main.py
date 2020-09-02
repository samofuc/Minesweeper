import bottle
import Board

board = Board.Board(15,15,40)

@bottle.get('/')
def osnovna_stran():
    return bottle.template('home.html', board=board)

@bottle.post('/new/')
def new_game():
    board.init_board()
    bottle.redirect('/')

@bottle.post('/open/')
def open_cell():
    col = int(bottle.request.forms['selected_col'])
    row = int(bottle.request.forms['selected_row'])
    mouse_button = bottle.request.forms['mouse_button']

    if (mouse_button == "left"):
        board.open(row, col)
    elif (mouse_button == "right"):
        board.toggle_marked(row, col)

    bottle.redirect('/')

bottle.run(debug=True, reloader=True)

