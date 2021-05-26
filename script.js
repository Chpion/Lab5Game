const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const ground = new Image();
ground.src = "images/field.png";
const fir = new Image();
fir.src = "images/fir.png"
const pinetree = new Image();
pinetree.src = "images/pinetree.png"
const birchtree = new Image();
birchtree.src = "images/birchtree.png"
let x;
let y;
let box = 125;
let tree;
let field = [];
let month = 5;
let year = 1;
let time = 0;
let k = 0, count = 0;
let rand;
let firK = 0, pineK = 0, birchK = 0;


function end(){
	let q = 0;
	for (let i = 0; i < 15; i++){
		if (field[i] == 0){
			q++;
		}
		else if (field[i]==1){
			firK++;
		}
		else if (field[i]==2){
			pineK++;
		}
		else{
			birchK++;
		}
	}
	if (q == 0){
		alert("Вы победили!Выращено: " + firK + " Елей " + pineK + " Сосен " + birchK + " Берез!");
	}
	else{
		alert("Вы проиграли!Выращено: " + (16-q) + " деревьев из 16");
	}
}

function deleted(){
	if (month == 12){
		let q = 0;
		for (let i = 0; i < 15; i++){
			if (field[i] != 0){
				q++;
			}
		}
		count = Math.floor( q / 100 * 40);
		if (count <= 1){
			count = 1;
			let i = 15;
			while (count > 0){
				if (field[i] == 1 ||field[i] == 2 || field[i] == 3 ){
					if (field[i] == 1){						
						field[i] = 0;
						count--;
					}
					else if(field[i] == 2){
						field[i] = 0;
						count--;
					}
					else {
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
		else if (count > 1){
			let i = 15;
			while (count > 0){
				if (field[i] == 1 ||field[i] == 2 || field[i] == 3 ){
					if (field[i] == 1){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 2){
						field[i] = 0;
						count--;
					}
					else {
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
	}
	if (month >= 3 && month <= 5){
		let q = 0;
		for (let i = 0; i < 15; i++){
			if (field[i] == 1 || field[i] == 2){
				q++;
			}
		}
		count = Math.floor(q / 100 * 40);
		let j = 0;
		if (count <= 1){
			count = 1;
			let i = 15;
			while (count > 0){
				if (field[i] == 1 ||field[i] == 2){
					if (field[i] == 1){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 2){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
		else if (count > 1){
			let i = 15;
			while (count > 0){
				if (field[i] == 1 ||field[i] == 2){
					console.log(field[i]);
					if (field[i] == 1){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 2){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
	}
	if (month >= 6 && month <=8){
		let q = 0;
		for (let i = 0; i < 15; i++){
			if (field[i] == 1 || field[i] == 3){
				q++;
			}
		}
		count = Math.floor(q / 100 * 40);
		if (count < 1){
			count = 1;
			let i = 15;
			while (count >= 0){
				if (field[i] == 1 ||field[i] == 3){
					if (field[i] == 1){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 3){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
		else if (count > 1){
			let i = 15;
			while (count > 0){
				if (field[i] == 1 ||field[i] == 3){
					if (field[i] == 1){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 3){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
	}
	if (month >= 9 && month <=11){
		let q = 0;
		for (let i = 0; i < 15; i++){
			if (field[i] == 3 || field[i] == 2){
				q++;
			}
		}
		count = Math.floor(q / 100 * 40);
		if (count <= 1){
			count = 1;
			let i = 15;
			while (count > 0){
				if (field[i] == 2 ||field[i] == 3){
					if (field[i] == 2){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 3){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
		else if (count > 1){
			let i = 15;
			while (count > 0){
				if (field[i] == 2 ||field[i] == 3){
					if (field[i] == 2){
						field[i] = 0;
						count--;
					}
					else if(field[i] == 3){
						field[i] = 0;
						count--;
					}
					
				}
				i--;
			}
		}
	}
}

function timer(){
	time++;
	if (time > 4)
	{
		time = 1;
		if (month == 12)
		{
			month = 3;
			year++;
			deleted();
			draw();
		}
		else if (month == 5 && year == 3)
		{
			end();
		}
		else{
			month++;
			deleted();
			draw();
		}
	}
	let q = 0;
	for (let i = 0; i < 15; i++){
		if (field[i] == 0){
			q++;
		}
	}
	document.getElementById("time").innerHTML ="До смены месяца осталось:"+(4-time);
	document.getElementById("data").innerHTML ="Дата:"+ month + "." + year;
}

function direction(event){
    if(event.keyCode == 49){
        tree = 1;
    }
    else if(event.keyCode==50){
        tree = 2;
    }
    else if(event.keyCode==51){
        tree = 3;
    }
	mouse();
}

function mouse()
{
	$( document ).ready(function(){
		$( document ).click(function( event ){
			x = Math.floor((event.pageX + 62.5) / 125 - 6);
			y = Math.floor((event.pageY)/ 125);
		});
	});
	draw();
}

function draw(){
	ctx.drawImage(ground, 0, 0)
	if (field[y*4+x] == 0)
	{
		field[y*4+x] = tree;
		for (let i = 0; i < 16; i++){
			if (field[i] == 1){
				ctx.drawImage(fir, (i%4*125+5), (Math.floor(i/4)*125+5))
			}
			else if (field[i] == 2){
				ctx.drawImage(pinetree, (i%4*125+5),(Math.floor(i/4)*125+5))	
			}
			else if (field[i] == 3){
				ctx.drawImage(birchtree, (i%4*125+5), (Math.floor(i/4)*125+5))
			}		
		}
	}
	else if (field[y*4+x] == 1){
		field[y*4+x] = tree;
		for (let i = 0; i < 16; i++){
			if (field[i] == 1){
				ctx.drawImage(fir, (i%4*125+5), (Math.floor(i/4)*125+5))
			}
			else if (field[i] == 2){
				ctx.drawImage(pinetree, (i%4*125+5),(Math.floor(i/4)*125+5))				
			}
			else if (field[i] == 3){
				ctx.drawImage(birchtree, (i%4*125+5), (Math.floor(i/4)*125+5))				
			}		
		}
	}
	else if (field[y*4+x] == 2){
		field[y*4+x] = tree;
		for (let i = 0; i < 16; i++){
			if (field[i] == 1){
				ctx.drawImage(fir, (i%4*125+5), (Math.floor(i/4)*125+5))				
			}
			else if (field[i] == 2){
				ctx.drawImage(pinetree, (i%4*125+5),(Math.floor(i/4)*125+5))
			}
			else if (field[i] == 3){
				ctx.drawImage(birchtree, (i%4*125+5), (Math.floor(i/4)*125+5))				
			}		
		}
	}
	else{
		field[y*4+x] = tree;
		for (let i = 0; i < 16; i++){
			if (field[i] == 1){
				ctx.drawImage(fir, (i%4*125+5), (Math.floor(i/4)*125+5))				
			}
			else if (field[i] == 2){
				ctx.drawImage(pinetree, (i%4*125+5),(Math.floor(i/4)*125+5))				
			}
			else if (field[i] == 3){
				ctx.drawImage(birchtree, (i%4*125+5), (Math.floor(i/4)*125+5))
			}		
		}
	}
	
}
document.addEventListener("keydown", direction);
let game = setInterval(timer, 1000);