#!/usr/bin/swipl

% Questo file Prolog implementa un'interfaccia interattiva per visualizzare informazioni da GitHub
% tramite una simulazione del comportamento richiesto, poiché Prolog non gestisce direttamente
% le richieste HTTP senza estensioni specifiche. Le informazioni sono simulate per dimostrare
% l'interfaccia interattiva richiesta.

:- initialization(main).

% Predicati per le informazioni simulate (in una vera implementazione questi verrebbero da una chiamata API)
nome('Mario Rossi').
bio('Sono uno sviluppatore appassionato di logica e programmazione funzionale.').
repo_pubblici(15).
follower(128).
following(50).

% Mostra il menu principale
mostra_menu :-
    write('=================================================='), nl,
    write('Seleziona un\'opzione:'), nl,
    write('1. Nome'), nl,
    write('2. Bio'), nl,
    write('3. Numero di repository pubblici'), nl,
    write('4. Numero di follower'), nl,
    write('5. Numero di following'), nl,
    write('6. Tutte le informazioni'), nl,
    write('7. Esci'), nl,
    write('Inserisci il numero dell\'opzione: ').

% Gestione delle scelte
esegui_scelta(1) :-
    nome(Nome),
    format('~nNome: ~w~n', [Nome]).
esegui_scelta(2) :-
    bio(Bio),
    format('~nBio: ~w~n', [Bio]).
esegui_scelta(3) :-
    repo_pubblici(Repos),
    format('~nNumero di repository pubblici: ~w~n', [Repos]).
esegui_scelta(4) :-
    follower(Followers),
    format('~nNumero di follower: ~w~n', [Followers]).
esegui_scelta(5) :-
    following(Following),
    format('~nNumero di following: ~w~n', [Following]).
esegui_scelta(6) :-
    nome(Nome),
    bio(Bio),
    repo_pubblici(Repos),
    follower(Followers),
    following(Following),
    write('Tutte le informazioni:'), nl,
    format('Nome: ~w~n', [Nome]),
    format('Bio: ~w~n', [Bio]),
    format('Repository pubblici: ~w~n', [Repos]),
    format('Follower: ~w~n', [Followers]),
    format('Following: ~w~n', [Following]).
esegui_scelta(7) :-
    write('Grazie per aver usato l\'applicazione. Arrivederci!'), nl,
    halt.
esegui_scelta(_) :-
    write('Opzione non valida. Riprova.'), nl.

% Legge l'input dell'utente
leggi_input(Scelta) :-
    read(Scelta).

% Loop principale
loop :-
    mostra_menu,
    leggi_input(Scelta),
    esegui_scelta(Scelta),
    write('Premi Invio per continuare...'), nl,
    get_char(_),
    loop.

% Punto di ingresso principale
main :-
    write('Benvenuto nell\'applicazione informativa GitHub!'),
    nl,
    write('ATTENZIONE: Questo programma simula le informazioni di GitHub.'),
    nl,
    write('In una vera implementazione, questo codice farebbe una chiamata API.'),
    nl,
    loop.