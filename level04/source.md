# Source

## Code reconstitué

```C
int main(void) {
    int status = 0;
    char input[32];
    pid_t child = fork();

    if (child == 0) {
        prctl(1, 1);
        ptrace(0, 0, 0, 0);
        puts("Give me some shellcode, k");
        gets(input);
    } else {
        while (1) {
            wait(&status);
            if (status & 127) {
                puts("child is exiting...");
                return 0;
            }
            if (ptrace(3, child, 44, 0) == 11)
                break;
        }
        puts("no exec() for you");
        kill(child, SIGKILL);
    }
    return 0;
}
```

## Origine depuis cutter

```C
undefined4 main(void)
{
    int32_t iVar1;
    undefined4 *puVar2;
    uint8_t uVar3;
    uint32_t uStack164;
    undefined4 auStack160 [32];
    uint32_t uStack32;
    uint32_t uStack28;
    int32_t iStack24;
    int32_t iStack20;
    int32_t var_8h;

    uVar3 = 0;
    iStack20 = fork();
    puVar2 = auStack160;
    for (iVar1 = 0x20; iVar1 != 0; iVar1 = iVar1 + -1) {
        *puVar2 = 0;
        puVar2 = puVar2 + (uint32_t)uVar3 * -2 + 1;
    }
    iStack24 = 0;
    uStack164 = 0;
    if (iStack20 == 0) {
        prctl(1, 1);
        ptrace(0, 0, 0, 0);
        puts("Give me some shellcode, k");
        gets(auStack160);
    } else {
        do {
            wait(&uStack164);
            uStack32 = uStack164;
            if (((uStack164 & 0x7f) == 0) || (uStack28 = uStack164, '\0' < (char)(((uint8_t)uStack164 & 0x7f) + 1) >> 1)
               ) {
                puts("child is exiting...");
                return 0;
            }
            iStack24 = ptrace(3, iStack20, 0x2c, 0);
        } while (iStack24 != 0xb);
        puts("no exec() for you");
        kill(iStack20, 9);
    }
    return 0;
}
```
