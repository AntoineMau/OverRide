# Level03

On observe que l'exécutable lit un input sur l'entrée standard

```shell
$ ./level03
***********************************
*            level03            **
***********************************
Password:123456789

Invalid Password
```

En reconstituant le code (_résultat sauvegardé dans [source.md](source.md)_).
On cherche a trouver le nombre pour finaliser cette equation

```C
"Q" ^ number = "C"
"}" ^ number = "o"
...
```

On obtient <code>"Q}|u`sfg~sf{}|a3" ^ "Congratulations!" = 12121212121212121212121212121212<sub>16</sub></code>

On comprend que le paramètre de la fonction `decrypt()` doit prendre etre `0x12`. Nous devons, donc résoudre cette équation

```Python
0x1337d00d - input = 0x12
input = 0x1337d00d - 0x12
input = 0x1337cffb <=> 322424827
```

Plus qu'a essayer

```shell
$ ./level03
***********************************
*            level03            **
***********************************
Password:322424827
$ cat /home/users/level04/.pass
kgv3tkEb9h2mLkRsPkXRfc2mHbjMxQzvb2FrgKkf
```

lien: https://xor.pw/
