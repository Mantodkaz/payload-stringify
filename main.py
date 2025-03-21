def convert_to_c_string(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = 'const char* StringPayload =\n'
    for line in lines:
        escaped = (
            line.replace('\\', '\\\\')     
                .replace('"', '\\"')       
                .rstrip('\n').rstrip('\r')
        )
        result += f'"{escaped}\\r\\n"\n'
    result += ';'
    return result

if __name__ == '__main__':
    input_file = 'backdoor.aspx' # change this (optional)
    output = convert_to_c_string(input_file)

    with open('payload_c_literal.txt', 'w', encoding='utf-8') as f:
        f.write(output)

    print('[+] Conversion complete. Output saved to payload_c_literal.txt')
