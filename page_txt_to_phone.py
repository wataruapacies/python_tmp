def phone_number_new(string):
    number_10 = ['0','1','2','3','4','5','6','7','8','9']
    exist = 0
    count = 0
    count_hyphen = 0
    phone_number_count = 12
    answer = ['','']
    for i in range(len(string)):
        if i < 15:
            continue
        elif string[i] in number_10 and string[i-1] in number_10 and string[i-2] in number_10 and string[i-3] == '-' and string[i-4] in number_10 and string[i-5] in number_10 and string[i-6] in number_10 and string[i-7] == '-' and string[i-8] == '0' and string[i-9] == '2' and string[i-10] == '1' and string[i-11] == '0':
            digits = 11
            answer[1] = string[i-digits]
            for k in range(digits):
                answer[1] = answer[1] + string[i-(digits-1-k)]
            #print('free dial')
            #print(answer[1])
        elif string[i] in number_10 and string[i-1] in number_10 and string[i-2] in number_10 and string[i-3] in number_10:#末尾****
            if string[i-4] == '-':#末尾-****
                if string[i-5] in number_10 and string[i-6] in number_10:#末尾**-****
                    if string[i-7] in number_10 and string[i-8] in number_10:#末尾****-****
                        if string[i-9] == '-':#末尾-****-****
                            if string[i-10] in number_10 and string[i-11] =='0':#0*-****-****
                                digits = 11
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('00'):
                                    answer[0] = ''
                                else:
                                    break
                            elif string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0':#0**-****-****
                                digits = 12
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('000'):
                                    answer[0] = ''
                                else:
                                    break
                        elif string[i-9] ==')':#末尾)****-****
                            if string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0*)****-****
                                digits = 12
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('(00)'):
                                    answer[0] = ''
                                else:
                                    break
                            elif string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0' and string[i-13] == '(':#(0**)****-****
                                digits = 13
                                answer[0] = string[i-digits]
                                for k in range(digits):
                                    answer[0] = answer[0] + string[i-(digits-1-k)]
                                if answer[0].startswith('(000)'):
                                    answer[0] = ''
                                else:
                                    break
                    elif string[i-7] in number_10:#末尾***-****
                        if string[i-8] == '-' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0**-***-****
                            digits = 11
                            answer[0] = string[i-digits]
                            for k in range(digits):
                                answer[0] = answer[0] + string[i-(digits-1-k)]
                            if answer[0].startswith('000'):
                                answer[0] = ''
                            else:
                                break
                        elif string[i-8] == ')' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0**)***-****
                            digits = 12
                            answer[0] = string[i-digits]
                            for k in range(digits):
                                answer[0] = answer[0] + string[i-(digits-1-k)]
                            if answer[0].startswith('(000)'):
                                answer[0] = ''
                            else:
                                break
                    elif string[i-7] == '-' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] =='0':#0***-**-****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('0120'):
                            answer[1] = answer[0]
                            answer[0] = ''
                            #print('free dial')
                            #print(answer[1])
                        if answer[0].startswith('0000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] == '(' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] =='0' and string[i-12] == ')':#(0***)**-****
                        digits = 12
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('(0120)'):
                            answer[1] = answer[0]
                            answer[0] = ''
                            #print('free dial')
                            #print(answer[1])
                        if answer[0].startswith('(0000)'):
                            answer[0] = ''
                        else:
                            break
            elif string[i-4] == ')':#末尾)****
                if string[i-5] in number_10 and string[i-6] in number_10:#末尾**)****
                    if string[i-7] =='(' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0***(**)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('0120'):
                            answer.append(answer[0])
                            answer[0] = ''
                            #print('free dial')
                            #print(answer[1])
                        if answer[0].startswith('0000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] =='(' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0':#0**(***)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('000'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] =='(' and string[i-10] in number_10 and string[i-11] == '0':#0*(****)****
                        digits = 11
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('00'):
                            answer[0] = ''
                        else:
                            break
                    elif string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] =='(' and string[i-10] in number_10 and string[i-11] in number_10 and string[i-12] == '0':#0**(****)****
                        digits = 12
                        answer[0] = string[i-digits]
                        for k in range(digits):
                            answer[0] = answer[0] + string[i-(digits-1-k)]
                        if answer[0].startswith('000'):
                            answer[0] = ''
                        else:
                            break
            elif string[i-4] in number_10 and string[i-5] in number_10:#末尾******
                if string[i-6] == ')' and string[i-7] in number_10 and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0***)******
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(0120)'):
                        answer[1] = answer[0]
                        #print('free dial')
                        #print(answer[1])
                        answer[0] = ''
                    if answer[0].startswith('(0000)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] == ')' and string[i-8] in number_10 and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0**)*******
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(000)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] in number_10 and string[i-8] == ')' and string[i-9] in number_10 and string[i-10] == '0' and string[i-11] == '(':#(0*)********
                    digits = 11
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(00)'):
                        answer[0] = ''
                    else:
                        break
                elif string[i-6] in number_10 and string[i-7] in number_10 and string[i-8] == ')' and string[i-9] in number_10 and string[i-10] in number_10 and string[i-11] == '0' and string[i-12] == '(':#(0**)********
                    digits = 12
                    answer[0] = string[i-digits]
                    for k in range(digits):
                        answer[0] = answer[0] + string[i-(digits-1-k)]
                    if answer[0].startswith('(000)'):
                        answer[0] = ''
                    else:
                        break
    return answer