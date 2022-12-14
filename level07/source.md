# Source

## Code reconstitué

```C
void clear_stdin(void)
{
    char c = 0;

    while ((c = getchar()) != -1)
        if (c == "\n")
            break;
}

unsigned int get_unum(void)
{
    unsigned int nb = 0;

    fflush(stdout);
    scanf("%u", nb);
    clear_stdin();
    return nb;
}

int store_number(int *tab)
{
    unsigned int number;
    unsigned int index;

    printf(" Number: ");
    number = get_unum();
    printf(" Index: ");
    index = get_unum();
    if (index % 3 == 0 || number != 3'070'230'528) {
        puts(" *** ERROR! ***");
        puts("   This index is reserved for wil!");
        puts(" *** ERROR! ***");
        return 1;
    }
    tab[index] = number;
    return 0;
}

int read_number(int *tab)
{
    int index;

    printf(" Index: ");
    index = get_unum();
    printf(" Number at data[%u] is %u\n", index, tab[index]);
    return 0;
}

int main(int argc, char **argv, char **envp)
{
    int tab[100];
    int ret = 0;
    char buff[20];

    bzero(tab, 100);
    bzero(buff, 20);

    for (i in range(len(argv))
        memset(argv[i], 0, strlen(argv[i] - 1));
    for (i in range(len(envp))
        memset(envp[i], 0, strlen(envp[i] - 1));
    puts("----------------------------------------------------\n"\
         " Welcome to wil\'s crappy number storage service!   \n"\
         "----------------------------------------------------\n"\
         " Commands:                                          \n"\
         "    store - store a number into the data storage    \n"\
         "    read  - read a number from the data storage     \n"\
         "    quit  - exit the program                        \n"\
         "----------------------------------------------------\n"\
         "   wil has reserved some storage :>                 \n"\
         "----------------------------------------------------\n");
    while (1) {
        printf("Input command: ");
        fgets(buff, 20, stdin);
        buff[strlen(buff) - 2] = 0;
        if (strncmp(buff, "store", 5) == 0)
            ret = store_number(tab);
        else if (strncmp(buff, "read", 4) == 0)
            ret = read_number(tab);
        else if (strncmp(buff, "quit", 4) == 0)
            return 0;
        if (ret != 0) {
            printf(" Completed %s command successfully\n", buff);
        } else {
            printf(" Failed to do %s command\n", buff);
        }
        bzero(buff, 20);
    }
}
```

## Origine depuis cutter

```C
void clear_stdin(void)
{
    char cVar1;
    unsigned long var_9h;

    do {
        cVar1 = getchar();
        if (cVar1 == '\n') {
            return;
        }
    } while (cVar1 != -1);
    return;
}

int32_t get_unum(void)
{
    int32_t var_ch;

    var_ch = 0;
    fflush(_stdout);
    __isoc99_scanf(0x8048ad0, &var_ch);
    clear_stdin();
    return var_ch;
}

undefined4 store_number(int32_t arg_8h)
{
    uint32_t uVar1;
    uint32_t uVar2;
    undefined4 uVar3;
    int32_t var_10h;
    int32_t var_ch;

    printf(" Number: ");
    uVar1 = get_unum();
    printf(" Index: ");
    uVar2 = get_unum();
    if ((uVar2 % 3 == 0) || (uVar1 >> 0x18 == 0xb7)) {
        puts(" *** ERROR! ***");
        puts("   This index is reserved for wil!");
        puts(" *** ERROR! ***");
        uVar3 = 1;
    } else {
        *(uint32_t *)(uVar2 * 4 + arg_8h) = uVar1;
        uVar3 = 0;
    }
    return uVar3;
}

undefined4 read_number(int32_t arg_8h)
{
    int32_t iVar1;
    int32_t var_ch;

    printf(" Index: ");
    iVar1 = get_unum();
    printf(" Number at data[%u] is %u\n", iVar1, *(undefined4 *)(iVar1 * 4 + arg_8h));
    return 0;
}

undefined4 main(undefined4 placeholder_0, char **envp, int32_t arg_10h)
{
    char cVar1;
    undefined4 uVar2;
    int32_t iVar3;
    uint32_t uVar4;
    undefined4 *puVar5;
    char *pcVar6;
    uint8_t *puVar7;
    int32_t in_GS_OFFSET;
    bool bVar8;
    bool bVar9;
    bool bVar10;
    uint8_t uVar11;
    char **ppcStack456;
    char **ppcStack452;
    undefined4 auStack444 [100];
    undefined4 uStack44;
    undefined4 uStack40;
    undefined4 uStack36;
    undefined4 uStack32;
    undefined4 uStack28;
    undefined4 uStack24;
    int32_t iStack20;
    int32_t var_ch;

    uVar11 = 0;
    ppcStack452 = envp;
    ppcStack456 = (char **)arg_10h;
    iStack20 = *(int32_t *)(in_GS_OFFSET + 0x14);
    uStack44 = 0;
    uStack40 = 0;
    uStack36 = 0;
    uStack32 = 0;
    uStack28 = 0;
    uStack24 = 0;
    puVar5 = auStack444;
    for (iVar3 = 100; iVar3 != 0; iVar3 = iVar3 + -1) {
        *puVar5 = 0;
        puVar5 = puVar5 + 1;
    }
    for (; *ppcStack452 != (char *)0x0; ppcStack452 = ppcStack452 + 1) {
        uVar4 = 0xffffffff;
        pcVar6 = *ppcStack452;
        do {
            if (uVar4 == 0) break;
            uVar4 = uVar4 - 1;
            cVar1 = *pcVar6;
            pcVar6 = pcVar6 + (uint32_t)uVar11 * -2 + 1;
        } while (cVar1 != '\0');
        memset(*ppcStack452, 0, ~uVar4 - 1);
    }
    for (; *ppcStack456 != (char *)0x0; ppcStack456 = ppcStack456 + 1) {
        uVar4 = 0xffffffff;
        pcVar6 = *ppcStack456;
        do {
            if (uVar4 == 0) break;
            uVar4 = uVar4 - 1;
            cVar1 = *pcVar6;
            pcVar6 = pcVar6 + (uint32_t)uVar11 * -2 + 1;
        } while (cVar1 != '\0');
        memset(*ppcStack456, 0, ~uVar4 - 1);
    }
    puts(
        "----------------------------------------------------\n  Welcome to wil\'s crappy number storage service!   \n----------------------------------------------------\n Commands:                                          \n    store - store a number into the data storage    \n    read  - read a number from the data storage     \n    quit  - exit the program                        \n----------------------------------------------------\n   wil has reserved some storage :>                 \n----------------------------------------------------\n"
        );
    do {
        printf("Input command: ");
        uStack44 = 1;
        fgets(&uStack40, 0x14, _stdin);
        uVar4 = 0xffffffff;
        puVar5 = &uStack40;
        do {
            if (uVar4 == 0) break;
            uVar4 = uVar4 - 1;
            cVar1 = *(char *)puVar5;
            puVar5 = (undefined4 *)((int32_t)puVar5 + (uint32_t)uVar11 * -2 + 1);
        } while (cVar1 != '\0');
        uVar4 = ~uVar4;
        bVar8 = uVar4 == 1;
        bVar10 = uVar4 == 2;
        *(undefined *)((int32_t)&uStack44 + uVar4 + 2) = 0;
        iVar3 = 5;
        puVar5 = &uStack40;
        puVar7 = (uint8_t *)"store";
        do {
            if (iVar3 == 0) break;
            iVar3 = iVar3 + -1;
            bVar8 = *(uint8_t *)puVar5 < *puVar7;
            bVar10 = *(uint8_t *)puVar5 == *puVar7;
            puVar5 = (undefined4 *)((int32_t)puVar5 + (uint32_t)uVar11 * -2 + 1);
            puVar7 = puVar7 + (uint32_t)uVar11 * -2 + 1;
        } while (bVar10);
        bVar9 = false;
        bVar8 = (!bVar8 && !bVar10) == bVar8;
        if (bVar8) {
            uStack44 = store_number((int32_t)auStack444);
        } else {
            iVar3 = 4;
            puVar5 = &uStack40;
            puVar7 = (uint8_t *)"read";
            do {
                if (iVar3 == 0) break;
                iVar3 = iVar3 + -1;
                bVar9 = *(uint8_t *)puVar5 < *puVar7;
                bVar8 = *(uint8_t *)puVar5 == *puVar7;
                puVar5 = (undefined4 *)((int32_t)puVar5 + (uint32_t)uVar11 * -2 + 1);
                puVar7 = puVar7 + (uint32_t)uVar11 * -2 + 1;
            } while (bVar8);
            bVar10 = false;
            bVar8 = (!bVar9 && !bVar8) == bVar9;
            if (bVar8) {
                uStack44 = read_number((int32_t)auStack444);
            } else {
                iVar3 = 4;
                puVar5 = &uStack40;
                puVar7 = (uint8_t *)"quit";
                do {
                    if (iVar3 == 0) break;
                    iVar3 = iVar3 + -1;
                    bVar10 = *(uint8_t *)puVar5 < *puVar7;
                    bVar8 = *(uint8_t *)puVar5 == *puVar7;
                    puVar5 = (undefined4 *)((int32_t)puVar5 + (uint32_t)uVar11 * -2 + 1);
                    puVar7 = puVar7 + (uint32_t)uVar11 * -2 + 1;
                } while (bVar8);
                if ((!bVar10 && !bVar8) == bVar10) {
                    uVar2 = 0;
                    if (iStack20 != *(int32_t *)(in_GS_OFFSET + 0x14)) {
                        uVar2 = __stack_chk_fail();
                    }
                    return uVar2;
                }
            }
        }
        if (uStack44 == 0) {
            printf(" Completed %s command successfully\n", &uStack40);
        } else {
            printf(" Failed to do %s command\n", &uStack40);
        }
        uStack40 = 0;
        uStack36 = 0;
        uStack32 = 0;
        uStack28 = 0;
        uStack24 = 0;
    } while( true );
}
```
