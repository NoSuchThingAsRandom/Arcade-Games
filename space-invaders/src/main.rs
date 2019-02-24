extern crate bitvec;
extern crate piston;
extern crate piston_window;

<<<<<<< HEAD
use bitvec::*;
use piston::event_loop::{EventLoop, EventSettings, Events};
use piston_window::*;
use std::time::{Duration, Instant};

struct Dimensions {
    pub width: u32,
    pub height: u32,
}

struct Player {
    pub position: [f64; 4],
    pub bullet: Shot,
    pub colour: [f32; 4],
    pub velocity: f64,
    pub duration: Instant,
}
impl Player {
    fn new(dims: &Dimensions) -> Self {
        Player {
            position: [
                dims.width as f64 / 2.0,
                dims.height as f64 * 0.95,
                dims.width as f64 * 0.1,
                dims.height as f64 * 0.1,
            ],
            bullet: Shot {
                exist: false,
                position: [0.0, 0.0, 0.0, 0.0],
            },
            colour: [0.0, 1.0, 1.0, 1.0],
            velocity: 0.0,
            duration: Instant::now(),
        }
    }
    fn move_player(&mut self, amount: f64) {
        self.velocity = amount;
        self.duration = Instant::now();
    }
    fn fire(&mut self, dims: &Dimensions) {
        if !self.bullet.exist {
            self.bullet = Shot {
                exist: true,
                position: [
                    self.position[0],
                    self.position[1],
                    dims.width as f64 * 0.01,
                    dims.height as f64 * 0.05,
                ],
            }
        }
    }
}
#[derive(Copy, Clone)]
struct Shot {
    pub exist: bool,
    pub position: [f64; 4], //X,Y, Width, Height
}
impl Shot {
    fn update(&mut self, velocity: f64) {
        self.position[1] += velocity;
    }
=======

use bitvec::*;
use piston_window::*;
use piston::event_loop::{Events, EventLoop, EventSettings};

struct Dimensions{pub width:u32,pub height:u32}


struct Player{
    pub position:[f64;4],
    pub bullet:Option<Shot>,
    pub colour: [f32;4]
}
impl Player{
    fn new(dims:&Dimensions) -> Self{
        Player{
            position:[dims.width as f64/2.0,dims.height as f64*0.95,dims.width as f64*0.1,dims.height as f64*0.1],
            bullet:None,
            colour:[0.0,1.0,1.0,1.0]
        }
    }
    fn move_player(&mut self,amount:f64){
        self.position[0]+=amount;
    }
}

struct Shot{
    exist: bool,
    position:[f64;4]//X,Y, Width, Height
>>>>>>> origin/master
}

struct Row {
    pub alive: BitVec,
    pub position: f64,
    pub velocity: f64,
    pub height: f64,
<<<<<<< HEAD
    pub colour: [f32; 4],
}
impl Row {
    fn new(length: usize, height: f64, colour: [f32; 4]) -> Self {
        Row {
            position: height * 0.025,
=======
    pub colour: [f32;4]
}
impl Row{
    fn new(length:usize,height:f64, colour:[f32;4]) -> Self{
        Row{
            position: 0.0,
>>>>>>> origin/master
            velocity: 20.0,
            alive: bitvec![1;length],
            height,
            colour,
        }
    }
<<<<<<< HEAD
    fn dead(&mut self, index: usize) {
        self.alive.set(index, false)
    }
}

fn main() {
    let dimensions = Dimensions {
        width: 640,
        height: 480,
    };
    let mut first = Row::new(10, dimensions.height as f64 * 0.05, [1.0, 0.0, 0.0, 1.0]);
    let mut cannon = Player::new(&dimensions);
    let mut window: PistonWindow =
        WindowSettings::new("Space Invaders", [dimensions.width, dimensions.height])
            .exit_on_esc(true)
            .vsync(true)
            .build()
            .unwrap();
=======
}



fn main() {
    let dimensions=Dimensions{width:640,height:480};
    let mut first=Row::new(10,dimensions.height as f64 *0.05,[1.0,0.0,0.0,1.0]);
    let mut cannon=Player::new(&dimensions);
    let mut window: PistonWindow=WindowSettings::new(
        "Space Invaders",
        [dimensions.width,dimensions.height])
        .exit_on_esc(true)
        .vsync(true)
        .build()
        .unwrap();
>>>>>>> origin/master

    let mut events = Events::new(EventSettings::new());
    events.set_ups(60);
    events.set_max_fps(60);

<<<<<<< HEAD
    while let Some(e) = events.next(&mut window) {
        if let Some(_args) = e.render_args() {
            let mut count = 0.0;
            window.draw_2d(&e, |c, g| {
                clear([0.0; 4], g);
                rectangle(cannon.colour, cannon.position, c.transform, g);
                if cannon.bullet.exist {
                    rectangle(
                        [255.0, 255.0, 0.0, 255.0],
                        cannon.bullet.position,
                        c.transform,
                        g,
                    )
                }

                for i in first.alive.iter() {
                    if i {
                        //println!("{}",(first.position+count*dimensions.width as f64 *0.1+count*dimensions.width as f64 *0.01));
                        rectangle(
                            first.colour,
                            [
                                first.position + count * dimensions.width as f64 * 0.1,
                                first.height,
                                dimensions.width as f64 * 0.05,
                                dimensions.height as f64 * 0.05,
                            ],
                            c.transform,
                            g,
                        );
                        count += 1.0;
                    }
                }
            });
        }
        if let Some(args) = e.update_args() {
            //Moves first row of enemies
            first.position += first.velocity * args.dt;
            if first.position > dimensions.width as f64 * 0.04 {
                first.velocity = -(first.velocity.abs());
            }
            if first.position < dimensions.width as f64 * 0.02 {
                first.velocity = first.velocity.abs();
            }
            //Moves cannon
            if cannon.duration.elapsed() < Duration::from_millis(50) {
                cannon.position[0] += cannon.velocity;
            }
            //Moves Bullet
            if cannon.bullet.exist {
                cannon.bullet.position[1] += (dimensions.height as f64 * -0.5 * args.dt);
                if cannon.bullet.position[1] <= 0.0 {
                    cannon.bullet.exist = false;
                }
                //Collision detection
                for index in 0..first.alive.len() {
                    //for (index,item) in first.alive.iter().enumerate(){
                    if first.alive.get(index) {
                        if first.position + index as f64 * dimensions.width as f64 * 0.1
                            < cannon.bullet.position[0]
                            && cannon.bullet.position[0]
                                < first.position
                                    + index as f64 * dimensions.width as f64
                                    + dimensions.height as f64 * 0.05
                            && (dimensions.height as f64 * 0.05 + (first.height as f64))
                                < cannon.bullet.position[1]
                            && cannon.bullet.position[1] > first.height
                        {
                            first.dead(index);
                            println!("Delete2")
                        }
                    }
                }
            }
        }
        if let Some(button) = e.press_args() {
            match button {
                Button::Keyboard(key) => match key {
                    Key::Left => cannon.move_player(dimensions.width as f64 * -0.01),
                    Key::Right => cannon.move_player(dimensions.width as f64 * 0.01),
                    Key::Space => cannon.fire(&dimensions),
                    _ => {}
                },
                _ => {}
            }
        }
    }
=======


    while let Some(e) =events.next(&mut window){
        if let Some(args) = e.render_args() {
            let mut count=1.0;
            window.draw_2d(&e, |c,g|{
                clear([0.0;4],g);
                rectangle(cannon.colour,cannon.position,c.transform,g);
                for i in first.alive.iter(){
                    if i{
                        //println!("{}",(first.position+count*dimensions.width as f64 *0.1+count*dimensions.width as f64 *0.01));
                        rectangle(first.colour,
                        [first.position+count*dimensions.width as f64 *0.1,
                        first.height,
                        dimensions.width as f64 *0.05,
                        dimensions.height as f64 *0.05],
                        c.transform,g);
                        count+=1.0;
                    }
                }     
            });
        }
        if let Some(args)= e.update_args(){
            first.position+=first.velocity*args.dt;
            if first.position>dimensions.width as f64*0.01{
                first.velocity=-first.velocity;
            }
            if first.position<=dimensions.width as f64*-0.05{
                first.velocity=-first.velocity
            }
        }
        if let Some(button)=e.press_args(){
            match button{
                Button::Keyboard(key) => {
                    match key{
                        Key::Left => {cannon.move_player(dimensions.width as f64*-0.01)}
                        Key::Right => {cannon.move_player(dimensions.width as f64*0.01)}
                        _ => {}
                    }
                }
                _ => {}
            }
        }
}
>>>>>>> origin/master
}
