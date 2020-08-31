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
    print("Samo bi rad sel spat: ")
    print(row)
    print(col)
    #board.open(col, row)
    #bottle.redirect('/')

#@bottle.get('/izberi_velikost_in_zahtevnost/')
#def naslednja_stran():
    #velikost = bottle.request.query['velikost']
    #zahtevnost = bottle.request.query['zahtevnost']
    #return bottle.template('izgled_igre', velikost=velikost, zahtevnost=zahtevnost)
#
#@bottle.get('/izberi_velikost_in_zahtevnost/pozdravi/')
#def osnovne_manire():
    #width = int(bottle.request.query['a'])
    #height = int(bottle.request.query['b'])
    #return bottle.template('izgled_igre',width=width, height=height )

#@bottle.get('/izberi_velikost_in_zahtevnost/pozdravi/odpri/')
#def odpri_celico():
    #return "indeks te celice je" + row_idx + col_idx

bottle.run(debug=True, reloader=True)