import bottle
import Board
import os, sys
import uuid

boards = {}
app_dir = os.path.dirname(sys.argv[0])

@bottle.route('/<filename:re:.*\.css>')
def send_css(filename):
    return bottle.static_file(filename, root=app_dir)

@bottle.route('/<filename:re:.*\.gif>')
def send_image(filename):
    return bottle.static_file(filename, root=app_dir, mimetype='image/png')

def get_board():
    id = bottle.request.get_cookie('Minesweeper_player')
    if (id == None or boards.get(id) == None):
        id = str(uuid.uuid1())
        bottle.response.set_cookie('Minesweeper_player', id, path='/')
        boards[id] = Board.Board(9,9,5)

    return boards[id]

@bottle.get('/')
def osnovna_stran():
    return bottle.template('home.html', board=get_board())

@bottle.post('/new/')
def new_game():
    board = get_board()
    board.init(board.get_width(), board.get_height(), board.get_mine_count())
    bottle.redirect('/')

@bottle.post('/open/')
def open_cell():
    col = int(bottle.request.forms['selected_col'])
    row = int(bottle.request.forms['selected_row'])
    mouse_button = bottle.request.forms['mouse_button']

    board = get_board()
    if (mouse_button == "left"):
        board.open(row, col)
    elif (mouse_button == "middle"):
        board.open_neighbours(row, col)
    elif (mouse_button == "right"):
        board.toggle_marked(row, col)

    bottle.redirect('/')

bottle.run(debug=True, reloader=True)

