# Source

## Code reconstitué

```C
void log_wrapper(FILE *file, char *str1, char *str2)
{
    char buff[272]

    strcpy(buff, str);
    snprintf(&buff[strlen(buff)], 254 - strlen(buff), str2);
    buff[strcspn(buff, "\n")] = 0;
    fprintf(file, "LOG: %s\n", buff);
}


int main(int argc, char **argv)
{
    int fd_log;
    int fd_file;
    int fd_backup;
    char *dest;

    if (argc != 2) {
        printf("Usage: %s filename\n", *argv);
    }

    if ((fd_log = fopen("./backups/.log", w)) == 0) {
        printf("ERROR: Failed to open %s\n", "./backups/.log");
        exit(1);
    }

    log_wrapper(fd_log, "Starting back up: ", argv[1]);

    if ((fd_file = fopen(argv[1], r)) == 0) {
        printf("ERROR: Failed to open %s\n", argv[1]);
        exit(1);
    }

    dest = "./backups/"
    strncat(dest, argv[1], 100 - strlen(dest));

    if ((fd_backup = open(dest, 193, 423)) != -1) {
      printf("ERROR: Failed to open %s%s\n", "./backups/", argv[1]);
      exit(1);
    }

    while ((c = fgetc(fd_file)) != -1) {
        write(fd_backup, &c, 1);

    log_wrapper(fd_log, "Finished back up ", argv[1]);

    fclose(fd_file);
    close(fd_backup);
}

```

## Origine depuis cutter

```C
void log_wrapper(FILE *arg1, char *arg2, char **arg3)
{
    char cVar1;
    int64_t iVar2;
    uint64_t uVar3;
    uint64_t uVar4;
    char **ppcVar5;
    int64_t in_FS_OFFSET;
    uint8_t uVar6;
    va_list args;
    char **size;
    char *src;
    FILE *stream;
    char *va_args;
    int64_t canary;

    uVar6 = 0;
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    stream = arg1;
    strcpy(&va_args, arg2);
    uVar3 = 0xffffffffffffffff;
    ppcVar5 = &va_args;
    do {
        if (uVar3 == 0) break;
        uVar3 = uVar3 - 1;
        cVar1 = *(char *)ppcVar5;
        ppcVar5 = (char **)(ppcVar5 + uVar6 * -2 + 1);
    } while (cVar1 != '\0');
    uVar4 = 0xffffffffffffffff;
    ppcVar5 = &va_args;
    do {
        if (uVar4 == 0) break;
        uVar4 = uVar4 - 1;
        cVar1 = *(char *)ppcVar5;
        ppcVar5 = (char **)(ppcVar5 + uVar6 * -2 + 1);
    } while (cVar1 != '\0');
    snprintf(&stream + ~uVar4 + 7, 0xfe - (~uVar3 - 1), arg3);
    iVar2 = strcspn(&va_args, 0x400d4c);
    *(undefined *)(&va_args + iVar2) = 0;
    fprintf(stream, "LOG: %s\n", &va_args);
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
        __stack_chk_fail();
    }
    return;
}


undefined8 main(int argc, char **argv)
{
    char cVar1;
    int32_t iVar2;
    FILE *arg1;
    int64_t iVar3;
    undefined8 uVar4;
    uint64_t uVar5;
    char *pcVar6;
    int64_t in_FS_OFFSET;
    uint8_t uVar7;
    int64_t var_a8h;
    char **filename;
    uint64_t var_94h;
    FILE *var_88h;
    FILE *stream;
    unsigned long fildes;
    char *ptr;
    undefined2 uStack112;
    char cStack110;
    int64_t canary;

    uVar7 = 0;
    canary = *(int64_t *)(in_FS_OFFSET + 0x28);
    ptr._0_1_ = -1;
    if (argc != 2) {
        printf("Usage: %s filename\n", *argv);
    }
    arg1 = (FILE *)fopen("./backups/.log", 0x400d6b);
    if (arg1 == (FILE *)0x0) {
        printf("ERROR: Failed to open %s\n", "./backups/.log");
        exit(1);
    }
    log_wrapper(arg1, "Starting back up: ", (char **)argv[1]);
    iVar3 = fopen(argv[1], 0x400da9);
    if (iVar3 == 0) {
        printf("ERROR: Failed to open %s\n", argv[1]);
        exit(1);
    }
    stack0xffffffffffffff88 = (char *)0x70756b6361622f2e;
    uStack112 = 0x2f73;
    cStack110 = '\0';
    uVar5 = 0xffffffffffffffff;
    pcVar6 = (char *)(&ptr + 1);
    do {
        if (uVar5 == 0) break;
        uVar5 = uVar5 - 1;
        cVar1 = *pcVar6;
        pcVar6 = pcVar6 + uVar7 * -2 + 1;
    } while (cVar1 != '\0');
    strncat(&ptr + 1, argv[1], 99 - (~uVar5 - 1));
    iVar2 = open(&ptr + 1, 0xc1, 0x1b0);
    if (-1 < iVar2) goto code_r0x00400bee;
    printf("ERROR: Failed to open %s%s\n", "./backups/", argv[1]);
    exit(1);
    do {
        write(iVar2, &ptr, 1);
code_r0x00400bee:
        ptr._0_1_ = fgetc();
    } while ((char)ptr != -1);
    log_wrapper(arg1, "Finished back up ", (char **)argv[1]);
    fclose(iVar3);
    close(iVar2);
    uVar4 = 0;
    if (canary != *(int64_t *)(in_FS_OFFSET + 0x28)) {
        uVar4 = __stack_chk_fail();
    }
    return uVar4;
}
```
