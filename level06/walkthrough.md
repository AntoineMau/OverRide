# Level06

```shell
$ ./level06
***********************************
*             level06             *
***********************************
-> Enter Login: Hello
***********************************
***** NEW ACCOUNT DETECTED ********
***********************************
-> Enter Serial: World
```

Apres avoir reformer l'assembleur en C nous pouvons voir qu'il compare notre input `login` et notre input `serial`. Il compare notre `login` une fois crypte et notre `serial`.

On va faire un fichier python qui reproduit le comportement de cryptage du `level06`

- [Level06.py](Ressources/level06.py)

```shell
$ python level06.py "qwerty"
6232813

$ ./level06
***********************************
*             level06             *
***********************************
-> Enter Login: qwerty
***********************************
***** NEW ACCOUNT DETECTED ********
***********************************
-> Enter Serial: 6232813
Authenticated!

$ cat /home/users/level07/.pass
GbcPDRgsFK77LNnnuh7QyFYA2942Gp8yKj9KrWD8
```
