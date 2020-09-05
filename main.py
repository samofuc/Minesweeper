import bottle
import Board
import os, sys

board = Board.Board(15,15,40)

app_dir = os.path.dirname(sys.argv[0])

@bottle.route('/<filename:re:.*\.css>')
def send_css(filename):
    return bottle.static_file(filename, root=app_dir)

@bottle.route('/<filename:re:.*\.gif>')
def send_image(filename):
    return bottle.static_file(filename, root=app_dir, mimetype='image/png')

@bottle.get('/')
def osnovna_stran():
    return bottle.template('home.html', board=board)

@bottle.post('/new/')
def new_game():
    board.init(15, 15, 40)
    bottle.redirect('/')

@bottle.post('/open/')
def open_cell():
    col = int(bottle.request.forms['selected_col'])
    row = int(bottle.request.forms['selected_row'])
    mouse_button = bottle.request.forms['mouse_button']

    if (mouse_button == "left"):
        board.open(row, col)
    elif (mouse_button == "middle"):
        board.open_neighbours(row, col)
    elif (mouse_button == "right"):
        board.toggle_marked(row, col)

    bottle.redirect('/')

bottle.run(debug=True, reloader=True)

