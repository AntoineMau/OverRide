# Source

## Code reconstitué

```C
int main(int argc, char **argv)
{
    char *passwd;
    char *flag;
    char *name;
    int nb_read_c;
    FILE *file;

    file = fopen("/home/users/level03/.pass", 0x400bb0);
    if (!file) {
        fwrite("ERROR: failed to open password file\n", 1, 36, _stderr);
        exit(1);
    }
    nb_read_c = fread(&flag, 1, 41, file);
    flag.end(0);
    if (nb_read_c != 41) {
        fwrite("ERROR: failed to read password file\n", 1, 36, _stderr);
        exit(1);
    }
    fclose(file);
    puts("===== [ Secure Access System v1.0 ] =====");
    puts("/***************************************\\");
    puts("| You must login to access this system. |");
    puts("\\**************************************/");
    printf("--[ Username: ");
    fgets(&name, 100, _stdin);
    name.end(0);
    printf("--[ Password: ");
    fgets(&passwd, 100, _stdin);
    passwd.end(0);
    puts("*****************************************");
    if (strncmp(&flag, &passwd, 41) != 0) {
        printf(&name);
        puts(" does not have access!");
        exit(1);
    }
    printf("Greetings, %s!\n", &name);
    system("/bin/sh");
    return 0;
}
```

## Origine depuis cutter

```C
undefined8 main(int argc, char **argv)
{
    int32_t iVar1;
    undefined8 uVar2;
    int64_t iVar3;
    char **ppcVar4;
    char **var_120h;
    int var_114h;
    char *filename;
    char *ptr;
    char *format;
    int32_t var_ch;
    FILE *file;

    ppcVar4 = &format;
    for (iVar3 = 0xc; iVar3 != 0; iVar3 = iVar3 + -1) {
        *ppcVar4 = (char *)0x0;
        ppcVar4 = ppcVar4 + 1;
    }
    *(undefined4 *)ppcVar4 = 0;
    ppcVar4 = &ptr;
    for (iVar3 = 5; iVar3 != 0; iVar3 = iVar3 + -1) {
        *ppcVar4 = (char *)0x0;
        ppcVar4 = ppcVar4 + 1;
    }
    ppcVar4 = 0;
    ppcVar4 = &filename;
    for (iVar3 = 0xc; iVar3 != 0; iVar3 = iVar3 + -1) {
        *ppcVar4 = (char *)0x0;
        ppcVar4 = ppcVar4 + 1;
    }
    *(undefined4 *)ppcVar4 = 0;
    file = (FILE *)0x0;
    var_ch = 0;
    file = (FILE *)fopen("/home/users/level03/.pass", 0x400bb0);
    if (file == (FILE *)0x0) {
        fwrite("ERROR: failed to open password file\n", 1, 36, _stderr);
        exit(1);
    }
    var_ch = fread(&ptr, 1, 0x29, file);
    iVar3 = strcspn(&ptr, 0x400bf5);
    (&ptr + iVar3) = 0;
    if (var_ch != 0x29) {
        fwrite("ERROR: failed to read password file\n", 1, 36, _stderr);
        fwrite("ERROR: failed to read password file\n", 1, 36, _stderr);
        exit(1);
    }
    fclose(file);
    puts("===== [ Secure Access System v1.0 ] =====");
    puts(0x400c50);
    puts("| You must login to access this system. |");
    puts(0x400cb0);
    printf("--[ Username: ");
    fgets(&format, 100, _stdin);
    iVar3 = strcspn(&format, 0x400bf5);
    (&format + iVar3) = 0;
    printf("--[ Password: ");
    fgets(&filename, 100, _stdin);
    iVar3 = strcspn(&filename, 0x400bf5);
    (&filename + iVar3) = 0;
    puts("*****************************************");
    iVar1 = strncmp(&ptr, &filename, 0x29);
    if (iVar1 != 0) {
        printf(&format);
        puts(" does not have access!");
        exit(1);
        uVar2 = .init();
        return uVar2;
    }
    printf("Greetings, %s!\n", &format);
    system("/bin/sh");
    return 0;
}
```
