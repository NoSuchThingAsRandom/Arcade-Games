const MAX_SIZE: usize = 10;
fn main() {
    let mut grid = [[false; MAX_SIZE]; MAX_SIZE];
	//Add cells
	grid[2][3]=true;
	grid[2][4]=true;
	grid[2][2]=true;

	for pass in 0..10{
		println!("\nPass: {}",pass);
		//Update grid
		let moves: [isize; 3] = [-1, 0, 1];
		let mut new_grid = [[false; MAX_SIZE]; MAX_SIZE];
		for x in 0..MAX_SIZE {
			for y in 0..MAX_SIZE {
				//Counts number of alive neighbours
				let mut alive = 0;
				for x_move in &moves {
					for y_move in &moves {
						let new_x=
							if (x as isize + x_move) < 0{
								MAX_SIZE-1
							}else if (x as isize + x_move) ==MAX_SIZE as isize{
								0
							}else{
								(x as isize+x_move) as usize
							};
						let new_y=
							if (y as isize + y_move) < 0{
								MAX_SIZE-1
							}else if (y as isize + y_move) ==MAX_SIZE as isize{
								0
							}else{
								(y as isize+y_move)as usize
						};
						if x==new_x && y==new_y{
							continue;
						}
						if grid[new_x][new_y]{
							alive+=1;
						}

					}
				}
				/*
				For Debuging
				if alive>0{
					println!("x is: {} y is: {} alive: {}",x,y,alive);
				}*/
				new_grid[x][y] = if grid[x][y] == true {
					match alive {
						2 | 3 => true,
						_ => false,
					}
				} else {
					if alive == 3 {
						true
					} else {
						false
					}
				}
			}
		}
		grid=new_grid;
		
		//Output Grid
		print!(" ");
		for x in 0..MAX_SIZE{
			print!("{}",x);
		}
		print!("\n");
		for x in 0..MAX_SIZE{
			print!("{}",x);
			for y in 0..MAX_SIZE{
				if grid[x][y]{
					print!("I");
				}else{
					print!(" ");
				}
			}
			print!("\n");
		}
	}        
}
