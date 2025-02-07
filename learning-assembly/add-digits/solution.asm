section .data:
	number_str db '38', 0

global _start


_start:
		; check if number is less than one digit if it is then jump to print
    ; Initialize counter
    mov ecx, 0  ; ECX will hold the length
    mov esi, number_str  ; ESI points to the start of the string

find_length:
    cmp byte [esi], 0  ; Check if we've reached the null terminator
    je check_length  ; Jump to done if null terminator is found
    inc ecx  ; Increment counter (length)
    inc esi  ; Move to the next character
    jmp find_length  ; Repeat the loop

check_length:
    ; Compare A and B (AL - BL)
    cmp ecx, 2  ; Compare ECX (A) with 2 (B)
    ; Jump if A is less than B (JG: Jump if Greater)
		jb done   ; Jump if ecx is less than 2 (unsigned comparison)
		jae addnums ; Jump if ecx is greather than or equal to 2 (unsigned comparison)

convert_loop:
    ; Load next byte (character) from the string
    movzx edx, byte [esi] ; Load the next character into edx (zero-extend byte to word)

    ; Check if we've reached the null terminator (end of string)
    cmp dl, 0             ; Compare the character to 0 (null terminator)
    je done               ; If it is the null terminator, we're done

    ; Convert ASCII character to integer ('0' -> 0, '1' -> 1, ..., '9' -> 9)
    sub dl, '0'           ; Subtract ASCII value of '0' (0x30) to get the digit (e.g., '1' becomes 1)

    ; Multiply the result by 10 (shift left by 1 decimal place)
    imul eax, eax, 10     ; eax = eax * 10

    ; Add the digit to the result
    add eax, edx          ; eax = eax + digit

    ; Move to the next character
    inc esi               ; Increment pointer to the next character in the string

    ; Repeat the loop
    jmp convert_loop

addnums:


done:
    ; ECX now contains the length of the string
    ; You can use ECX in further code
    ; Exit program
    mov eax, 1  ; Syscall number for exit
    xor ebx, ebx  ; Return code 0
    int 0x80  ; Call kernel to exit
