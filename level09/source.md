# Source

## Code reconstitué

```C
struct s_struct
{
    char msg[128];
    char username[40];
    unsigned int i;
}

void secret_backdoor(void)
{
    char string[128];

    fgets(string, 128, stdin);
    system(string);
}

void set_msg(_struc *s)
{
    char message[128];

    bzero(message, 128);
    puts(">: Msg @Unix-Dude");
    printf(">>: ");
    fgets(message, 1024, stdin);
    strncpy(s->msg, message, s->i);
}

void set_username(s_struc *s)
{
    char username[128];

    bzero(username, 16)
    puts(">: Enter your username");
    printf(">>: ");
    fgets(username, 128, stdin);
    strncpy(s->username, username, 41)
    printf(">: Welcome, %s", s->username);
}

void handle_msg(void)
{
    s_struct *s;

    bzero(s->username, 40)
    s->i = 140;
    set_username(s);
    set_msg(s->msg);
    puts(">: Msg sent!");
}

int main(void)
{
    puts("--------------------------------------------\n"\
         "|   ~Welcome to l33t-m$n ~    v1337        |\n"\
         "--------------------------------------------\n");
    handle_msg();
    return 0;
}
```

## Origine depuis cutter

```C
void secret_backdoor(void)
{
    char *string;

    fgets(&string, 0x80, *_stdin);
    system(&string);
    return;
}

void set_msg(char *arg1)
{
    int64_t iVar1;
    char **ppcVar2;
    char *dest;
    char *src;

    ppcVar2 = &src;
    for (iVar1 = 0x80; iVar1 != 0; iVar1 = iVar1 + -1) {
        *ppcVar2 = (char *)0x0;
        ppcVar2 = ppcVar2 + 1;
    }
    puts(0xbcd);
    printf(0xbdf);
    fgets(&src, 0x400, *_stdin);
    strncpy(arg1, &src, (int64_t)*(int32_t *)(arg1 + 0xb4));
    return;
}

void set_username(int64_t arg1)
{
    int64_t iVar1;
    char **ppcVar2;
    int64_t var_98h;
    char *s;
    int64_t var_4h;

    ppcVar2 = &s;
    for (iVar1 = 0x10; iVar1 != 0; iVar1 = iVar1 + -1) {
        *ppcVar2 = (char *)0x0;
        ppcVar2 = ppcVar2 + 1;
    }
    puts(0xbe4);
    printf(0xbdf);
    fgets(&s, 0x80, *_stdin);
    for (var_4h._0_4_ = 0; ((int32_t)var_4h < 0x29 && (*(char *)((int64_t)&s + (int64_t)(int32_t)var_4h) != '\0'));
        var_4h._0_4_ = (int32_t)var_4h + 1) {
        *(undefined *)(arg1 + 0x8c + (int64_t)(int32_t)var_4h) = *(undefined *)((int64_t)&s + (int64_t)(int32_t)var_4h);
    }
    printf(0xbfb, arg1 + 0x8c);
    return;
}

void handle_msg(void)
{
    int64_t var_c0h;
    undefined8 uStack60;
    undefined8 uStack52;
    undefined8 uStack44;
    undefined8 uStack36;
    undefined8 uStack28;
    int64_t var_ch;

    uStack60 = 0;
    uStack52 = 0;
    uStack44 = 0;
    uStack36 = 0;
    uStack28 = 0;
    var_ch._0_4_ = 0x8c;
    set_username((int64_t)&var_c0h);
    set_msg((char *)&var_c0h);
    puts(0xbc0);
    return;
}

undefined8 main(void)
{
    puts(0xc10);
    handle_msg();
    return 0;
}
```
