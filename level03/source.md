# Source

## Code reconstitué

```C
void decrypt(int number)
{
    char str[17] = "Q}|u`sfg~sf{}|a3";

    for i in range(len(str))
      str[i] = str[i] ^ number;
    if (strncmp(str, "Congratulations!", 17) == 0)
        system("/bin/sh");
    else
        puts("\nInvalid Password");
}

void test(int input, int number)
{
    number -= input;
    switch(number) {
    default:
        decrypt(rand());
        break;
    case 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21:
        decrypt(number);
}

int main(void)
{
    int input;

    srand(time(0));
    puts("***********************************");
    puts("*\t\tlevel03\t\t**");
    puts("***********************************");
    printf("Password:");
    scanf(input);
    test(input, 0x1337d00d);
    return 0;
}
```

## Origine depuis cutter

```C
void decrypt(int32_t arg_8h)
{
    char cVar1;
    uint32_t uVar2;
    int32_t iVar3;
    int32_t *piVar4;
    uint8_t *puVar5;
    int32_t in_GS_OFFSET;
    bool bVar6;
    bool bVar7;
    int32_t var_2ch;
    int32_t var_28h;
    unsigned long var_24h;
    int32_t var_1dh;
    int32_t var_19h;
    int32_t var_15h;
    int32_t var_11h;
    undefined var_dh;
    int32_t canary;

    canary = *(int32_t *)(in_GS_OFFSET + 0x14);
    var_1dh = 0x757c7d51;
    var_19h = 0x67667360;
    var_15h = 0x7b66737e;
    var_11h = 0x33617c7d;
    var_dh = 0;
    uVar2 = 0xffffffff;
    piVar4 = &var_1dh;
    do {
        if (uVar2 == 0) break;
        uVar2 = uVar2 - 1;
        cVar1 = *(char *)piVar4;
        piVar4 = (int32_t *)((int32_t)piVar4 + 1);
    } while (cVar1 != '\0');
    var_28h = 0;
    while( true ) {
        bVar6 = (uint32_t)var_28h < ~uVar2 - 1;
        bVar7 = var_28h == ~uVar2 - 1;
        if (!bVar6) break;
        *(uint8_t *)((int32_t)&var_1dh + var_28h) = (uint8_t)arg_8h ^ *(uint8_t *)((int32_t)&var_1dh + var_28h);
        var_28h = var_28h + 1;
    }
    iVar3 = 0x11;
    piVar4 = &var_1dh;
    puVar5 = (uint8_t *)"Congratulations!";
    do {
        if (iVar3 == 0) break;
        iVar3 = iVar3 + -1;
        bVar6 = *(uint8_t *)piVar4 < *puVar5;
        bVar7 = *(uint8_t *)piVar4 == *puVar5;
        piVar4 = (int32_t *)((int32_t)piVar4 + 1);
        puVar5 = puVar5 + 1;
    } while (bVar7);
    if ((!bVar6 && !bVar7) == bVar6) {
        system();
    } else {
        puts();
    }
    if (canary != *(int32_t *)(in_GS_OFFSET + 0x14)) {
        __stack_chk_fail();
    }
    return;
}

void test(int32_t arg_8h, int32_t arg_ch)
{
    int32_t arg_8h_00;
    unsigned long var_ch;

    arg_ch = arg_ch - arg_8h;
    switch(arg_ch) {
    default:
        arg_8h_00 = rand();
        decrypt(arg_8h_00);
        break;
    case 1:
        decrypt(arg_ch);
        break;
    case 2:
        decrypt(arg_ch);
        break;
    case 3:
        decrypt(arg_ch);
        break;
    case 4:
        decrypt(arg_ch);
        break;
    case 5:
        decrypt(arg_ch);
        break;
    case 6:
        decrypt(arg_ch);
        break;
    case 7:
        decrypt(arg_ch);
        break;
    case 8:
        decrypt(arg_ch);
        break;
    case 9:
        decrypt(arg_ch);
        break;
    case 0x10:
        decrypt(arg_ch);
        break;
    case 0x11:
        decrypt(arg_ch);
        break;
    case 0x12:
        decrypt(arg_ch);
        break;
    case 0x13:
        decrypt(arg_ch);
        break;
    case 0x14:
        decrypt(arg_ch);
        break;
    case 0x15:
        decrypt(arg_ch);
    }
    return;
}

undefined4 main(void)
{
    int32_t iStack20;

    time();
    srand();
    puts();
    puts();
    puts();
    printf();
    __isoc99_scanf();
    test(iStack20, 0x1337d00d);
    return 0;
}
```
