NAVODILA ZA ZAGON PROGRAMA

Pred zagonom igre mora uporabnik:
1. Namestiti programski jezik Python 3.7
2. Namestiti Visual Studio Code.
3. Namestiti Git ali TortoiseGit.

Za zagon igre mora uporabnik:
1. Narediti kopijo Git repozitorija s specifikacijo https://github.com/samofuc/Minesweeper.git
2. V Visual Studio Code odpreti mapo Minesweeper, v katerem je kopija Git repozitorija.
3. V Visual Studio Code terminalu zagnati main.py python datoteko.
4. S spletnim brskalnikom odpreti naslov http://127.0.0.1:8080/".

Podprti spletni brskalniki:
1. Microsoft Edge
2. Google Chrome

NAVODILA ZA UPORABO

Minolovec je računalniška igra, pri kateri mora igralec označiti vsa polja z mino in odpreti vsa ostala polja. Mreža je pravokotne oblike in vsebuje polja, ki so na začetku zaprta.

Z levim gumbom miške na polje se zaprto polje odpre. Polje je lahko prazno, ima mino ali pa prikaže število vseh min na sosednjih poljih. Če uporabnik odpre polje z mino, se igra konča neuspešno. Če igralec odpre polje, ki nima mine, se igra nadaljuje. Če je polje prazno, se odprejo tudi sosednja polja.

Z desnim gumbom miške igralec označi zaprto polje. Pri tem seveda lahko označi katerokoli polje, tudi tako brez mine.¸

S sredinjskim gumbom miške na odprto polje igralec odpre vsa zaprta sosednja polja, če je označil ustrezno število min na sosednjih poljih. Če so mine označene napačno, se igra konča neuspešno.

Igra se konča uspešno, če igralec pravilno označi vsa polja z mina ter odpre vsa preostala polja.

S pritiskom na gumb (smiley face) igralec začne novo igro z istimi nastavitvami.

S pritiskom na gumb Game si igralec izbere težavnost igre. Izbere lahko med tremi težavnosti ali pa si sam izbere velikost mreže in število min.

V levem zgornjem kotu se izpisuje število še neoznačenih polj.

NADALNJI RAZVOJ

V prihodnosti bi igro lahko dopolnili:
1. Merjenje časa igre
2. Vodenje seznama najboljših igralcev
3. Označevanje polj z vprašajem

ZASLUGE

1. Del stilov in slike v igri sem si sposodil iz spletne igre http://minesweeperonline.com/
2. Implementacijo modalnega dialoga sem si sposodil na spletni strani https://www.w3schools.com/howto/howto_css_modals.asp
