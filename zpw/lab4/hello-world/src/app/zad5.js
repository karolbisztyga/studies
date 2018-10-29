/*
  arr1 = ["Mary","Tom","Jack","Jill"]
  arr2 = [1, 2, 3, 4]

  tabliczka() {
    let res = []
    for(let i = 0 ; i<arr1.length ; ++i)
    {
      res.push(i)
    }
    return res;
  }

  arr = tabliczka()
*/
var names = new Array("Mary", "Tom", "Jack", "Jill");
for (var i = 0; i < names.length; i++) {
    console.log(names[i]);
}
