import bottle
import Board

board = Board.Board(5,5,9)

@bottle.get('/')
def osnovna_stran():
    return bottle.template('home.html', board=board)

@bottle.post('/open/')
def open_cell():
    col = bottle.request.forms['selected_col']
    row = bottle.request.forms['selected_row']
    mouse_button = bottle.request.forms['mouse_button']

    if (mouse_button == "left"):
        print(row)
        print(col)
        print(mouse_button)
        #board.open(col, row)
    elif (mouse_button == "right"):
        print(row)
        print(col)
        print(mouse_button)
        board.toggle_marked(int(row), int(col))

    bottle.redirect('/')

bottle.run(debug=True, reloader=True)