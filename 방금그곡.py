arr = ['C#', 'D#', 'F#', 'G#', 'A#']
arr2 = ['c','d','f','g','a']
arr3 = list(zip(arr, arr2))

def pre_data(temp):
    global arr3
    for i, v in arr3:
        temp = temp.replace(i, v)
    return temp


def solution(m, musicinfos):  
    
    musicinfos_len = 0
    count = 999999999999
    result = []
    
    m = pre_data(m)
    m_len = len(m)
    
    for i in musicinfos:
        answer = ''
        start, end, title, info = i.split(',')
        start = start.split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = end.split(':')
        end = int(end[0]) * 60 + int(end[1])
        info = pre_data(info)
        musicinfos_len = end - start
        info_len = len(info)

        for i in range(musicinfos_len):
            answer += list(info)[i % info_len]

        #answer = pre_data(answer)
        try:
            temp = answer.index(m)
            temp = answer[temp:temp + m_len]
            result.append((musicinfos_len, count, title))

        except:
            pass
        count -= 1

    if len(result) == 0 :
        return "(None)"
    else:
        result = sorted(result, reverse=True)
        return result[0][2]