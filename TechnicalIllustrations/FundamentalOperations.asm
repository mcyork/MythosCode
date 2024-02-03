section .data
    msg db 'At the core, life is about processing experiences.', 0

section .text
    global _start

_start:
    mov rax, 1                  ; syscall for write
    mov rdi, 1                  ; file descriptor 1 is stdout
    mov rsi, msg                ; message to write
    mov rdx, 46                 ; number of bytes
    syscall                     ; invoke operating system to output the message

    mov rax, 60                 ; syscall for exit
    xor rdi, rdi                ; status 0
    syscall                     ; invoke operating system to exit
