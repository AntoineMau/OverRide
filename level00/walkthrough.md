# Level0

On observe que l'exécutable lit un input sur l'entrée standard

```shell
$ ./level00
***********************************
*            -Level00 -           *
***********************************
Password:Hello World

Invalid Password!
```

On regarde l'assembleur et on remarque qu'il compare notre input a
<code>0x149c<sub>16</sub> <=> 5276<sub>10</sub></code> et s'ils sont ésgaux il lance
`system("/bin/sh")`

```shell
$ ./level00
***********************************
*            -Level00 -           *
***********************************
Password:5276

Authenticated!
$ cat /home/users/level01/.pass
uSq2ehEGT6c9S24zbshexZQBXUGrncxn5sD5QfGL
```
