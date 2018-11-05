//let arr1 = ["Ala", "ma", "kota"]
//let arr2 = [1, 2, 3, 4]

export function tabliczka(arr1, arr2) {
    let res = []
    for(let i = 0 ; i<Math.min(arr1.length,arr2.length) ; ++i)
    {
        res.push(arr1[i] + arr2[i]);
    }
    return res;
}

export function tabliczka2(arr1, arr2) {
    let res = []
    let len = Math.min(arr1.length,arr2.length)
    let counter = 0
    for(let i of arr1) {
        res.push(i);
        ++counter
        if (counter >= len) break;
    }
    counter = 0
    for(let i of arr2) {
        res[counter] += i
        counter++
        if (counter >= len) break;
    }
    return res;
}
/*
let arr = tabliczka2(arr1, arr2)
for(let item of arr) {
    console.log(item);
}
*/