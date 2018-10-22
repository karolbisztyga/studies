document.addEventListener('DOMContentLoaded', function () {

	// zad1
	console.log('ZAD 1');

	const tab1 = [1, 7, 12, 46, 85];
	const tab2 = [10, 26, 75, 34];

	// merge
	const tab3 = [...tab1, ...tab2];

	console.log(tab3);

	// sort
	tab3.sort(function(a,b){
		return a-b;
	})

	console.log(tab3)

	// max and min
	let tab3max = Math.max(...tab3)
	let tab3min = Math.min(...tab3)

	console.log(tab3max);
	console.log(tab3min);

	// zad2
	console.log('ZAD 2');

	function printUpper(...args) {
		let result = ''
		for(i in args) {
			let arg = args[i];
			arg = arg.toUpperCase()
			result += arg + ' + '
		}
		result = result.substring(0,result.length-3)
		return result;
	}

	let up1 = printUpper("polska", "norwegia", "australia", "kanada");
	console.log(up1);

	// zad3
	console.log('ZAD 3');

	let counter = 0;
	let blueEnabled = true;
	let redEnabled = true;
	let yellowEnabled = true;
	let propagation = true;

	function checkCounter() {
		if (counter > 30)
			redEnabled = false;
		if(counter > 50)
			yellowEnabled = false;
	}

	let zad3blue = document.getElementById("zad3-blue");
	zad3blue.addEventListener('click', function(e) {
		checkCounter();
		if (blueEnabled) {
			++counter;
			console.log('blue ' + counter);
		}
	});

	let zad3red = document.getElementById("zad3-red");
	zad3red.addEventListener('click', function(e) {
		checkCounter();
		if (redEnabled) {
			++counter;
			console.log('red ' + counter);
		}
		if (!propagation) {
			if (!e) var e = window.event;
		    e.cancelBubble = true;
		    if (e.stopPropagation) e.stopPropagation();
		}
	});

	let zad3yellow = document.getElementById("zad3-yellow");
	zad3yellow.addEventListener('click', function(e) {
		checkCounter();
		if (yellowEnabled) {
			++counter;
			console.log('yellow ' + counter);
		}
		if (!propagation) {
			if (!e) var e = window.event;
		    e.cancelBubble = true;
		    if (e.stopPropagation) e.stopPropagation();
		}
	});

	let zad3propagation = document.getElementById("zad3-propagation");
	zad3propagation.addEventListener('click', function(e) {
		propagation = !propagation;
	});

	let zad3select = document.getElementById("zad3-select");

	let zad3add = document.getElementById("zad3-add");
	zad3add.addEventListener('click', function(e) {
		switch(zad3select.value) {
			case "blue":
				blueEnabled = true;
				break;
			case "red":
				redEnabled = true;
				break;
			case "yellow":
				yellowEnabled = true;
		}
	});

	let zad3remove = document.getElementById("zad3-remove");
	zad3remove.addEventListener('click', function(e) {
		switch(zad3select.value) {
			case "blue":
				blueEnabled = false;
				break;
			case "red":
				redEnabled = false;
				break;
			case "yellow":
				yellowEnabled = false;
		}
	});

	// zad4
	console.log('ZAD 4');

	const zad4tab = [1,2,3,4,5];
	let [a,b,,c] = zad4tab
	console.log(a + ',' + b + ',' + c);

	const obj = {
		name : "Marcin",
		surname : "Kowalski",
		age : 20
	}
	let {name, surname, age} = obj;
	console.log(name + ',' + surname + ',' + age);

	const user = {
		name: 'Grzegorz',
		type: 'node',
		info: 'something',
		id: 21,
		relatives: {
			wife: {
				name: 'Magdalena',
				id: 22
			}
		}
	};
	let test= {relatives: {wife: {}}};
	({
		info: test.info,
		id: test.id,
		relatives: {
			wife: {
				name: test.relatives.wife.name
			}
		}
	} = user);
	console.log(user);
	console.log(test);

	// zad5
	console.log('ZAD 5');

	class Brick {
		constructor(x,y,graphics,width,height,type,live) {
			this.x = x;
			this.y = y;
			this.graphics = graphics;
			this.width = width;
			this.height = height;
			this.type = type;
			this.live = live;
		}

		print() {
			console.log(this.x + ',' + this.y + ',' + this.graphics + ',' + this.width + ',' + this.height + ',' + this.type + ',' + this.live);
		}

		init() {
			console.log('Dodano plansze');
		}		
	}

	class BrickRed extends Brick {
		constructor(x,y,width,height,type) {
			super(x,y,'red.png',width,height,type,15);
		}
	}


	class BrickBlue extends Brick {
		constructor(x,y,width,height,type) {
			super(x,y,'blue.png',width,height,type,10);
		}
	}


	class BrickGreen extends Brick {
		constructor(x,y,width,height,type) {
			super(x,y,'green.png',width,height,type,20);
		}
	}

	class BrickAnim extends Brick {
		constructor(x,y,graphics,width,height,type,live,speed) {
			super(x,y,graphics,width,height,type,live);
			this.speed = speed;
		}
		moveHorizontal() {
			console.log("Poruszam sie poziomo z szybkoscia " + this.speed);
		}
	}

	let brick = new Brick(0,0,'test.jpg',100,100,null,12);
	brick.init();
	brick.print();
	let brickb = new BrickBlue(34,56,23,45,null);
	brickb.init();
	brickb.print();
	let brickg = new BrickGreen(223,12,45,234,null);
	brickg.init();
	brickg.print();
	let brickr = new BrickRed(54,3,23,32,null);
	brickr.init();
	brickr.print();
	let bricka = new BrickAnim(54,3,'asd.png',23,32,null,23,33);
	bricka.init();
	bricka.print();
	bricka.moveHorizontal();

	// zad6
	console.log('ZAD 6');

	function *gen() {
		var x = 20;
		while (x>0) {
			yield x--;
		}
	}

	let genobj = gen();
	for(var i=0;i<20;++i) {
		console.log(genobj.next().value);
	}

	// zad7
	console.log('ZAD 7');

	const user7 = [
		{ imie:"Ola", sex: 'F', value: 5000},
		{ imie:"Kasia", sex: 'F',value: 650},
		{ imie:"Jurek", sex: 'M',value: 10},
		{ imie:"Ola", sex: 'F', value: 1200},
		{ imie:"Robert", sex: 'M', value: 77},
		{ imie:"Wacek", sex: 'M', value: 77},
		{ imie:"Ula", sex: 'F', value: 77},
		{ imie:"Ola", sex: 'F', value: 77},
	]

	console.log(user7);
	let user7f = user7.filter(function(obj) { return obj.sex == 'F' });
	console.log(user7f);
	let sum7 = user7f.reduce(function(previousValue, currentValue, index, array) {
		return previousValue + currentValue.value;
	}, 0);
	console.log(sum7);

});