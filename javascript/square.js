function solution(v) {
    const answer = []
    const garo = []
    const saero = []
    
    for(var value of v) {
        const temp_garo = value[0]
        const temp_saero = value[1]
        garo.push(temp_garo)
        saero.push(temp_saero)
    }
    //console.log(garo, saero)
    let count = garo.filter(element => 1 === element).length
    //console.log(count)
    
    for(var garo_val of garo) {
        let count = garo.filter(element => garo_val === element).length
        if(count != 2) answer.push(garo_val)
    }
    
    for(var saero_val of saero) {
        let count = saero.filter(element => saero_val === element).length
        if(count != 2) answer.push(saero_val)
    }
    
    return answer
}

//https://programmers.co.kr/tryouts/3929/challenges?original_test_id=26818&original_token=daf8a795cfebe1144c822dd62cb4b13d 나머지 한점 구하기?
