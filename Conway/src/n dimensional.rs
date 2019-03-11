const MAX_SIZE: usize = 5;
const dimensions:usize=3;
/*
#[derive(Debug)]
struct myGeneric<T>{
	value:T,
}
impl myGeneric{
	fn out(&self){
		println{"{:?}",self.value};
	}
}
*/

fn main(){
	let mut grid=vec![false;MAX_SIZE];
    //let mut grid=[&temp;MAX_SIZE];
	for _d in 1..dimensions{
		//let grid=vec![&grid.copy();MAX_SIZE];
		let mut new=Vec::new();
		for x in 0..MAX_SIZE{
		    new.push(grid.clone());
		    
		}
		println!("D: {}",_d);
	}
	//print_grid(dimensions,&grid);
	println!("{:?}",grid);
	for x in 0..MAX_SIZE{
	 	for y in 0..MAX_SIZE{
	    	for z in 0..MAX_SIZE{
	            print!(" {}",grid[x][y][z]);
	    
	        }
	        print!("\n");
	    
	    }
	    println!("3Rd dimension {}",x);
	    
	}
}
/*
fn print_grid(dimensions:usize,grid:&[myGeneric]){
	if dimensions==1{
		for x in 0..MAX_SIZE{
			grid[x].output();
			//println!("{:?}",grid[x]);
			//print!("{:?}",grid[x]);
		}
	}else{
		println!("Printing dimensions {}",dimensions);
		for x in 0..MAX_SIZE{
			print_grid(dimensions-1,&grid[x] as &[myGeneric]);
		}
	}
	
}*/
