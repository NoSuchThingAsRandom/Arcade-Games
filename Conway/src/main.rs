extern crate piston;
extern crate piston_window;
use piston::event_loop::{EventLoop, EventSettings, Events};
use piston_window::*;


const DIMENSIONS: usize = 2;
const MAX_SIZE: usize = 100;
const GREEN:[f32;4]=[0.0, 0.0, 1.0, 1.0];
fn main() {
    println!("Hello World");
    let mut started=false;
    let mut cursor = [0.0, 0.0];
    let mut grid = [[false; MAX_SIZE]; MAX_SIZE];
    //TODO Create starting

    //Create window
    let mut window: PistonWindow=WindowSettings::new(
        "Game Of Life",
        [(MAX_SIZE*10) as u32,(MAX_SIZE*10) as u32])
        .exit_on_esc(true)
        .vsync(true)
        .build()
        .unwrap();
    let mut events = Events::new(EventSettings::new());
    events.set_ups(2);
    events.set_max_fps(10);

    while let Some(e) = events.next(&mut window) {
        if let Some(_args) = e.render_args() {
            window.draw_2d(&e, |c, g| {
                //Clear Screen
                clear([0.0; 4], g);

                //Draw Live Blobs
                for x in 0..MAX_SIZE{
                    for y in 0..MAX_SIZE{
                        if grid[x][y]{
                            rectangle(GREEN, [x as f64*10.0, y as f64*10.0, 10.0, 10.0], c.transform, g);
                        }
                    }
                }
                
            });
        }

        if let Some(args) = e.update_args() {
            if started{
                //Update grid
                let moves: [isize; 3] = [-1, 0, 1];
                let mut new_grid = [[false; MAX_SIZE]; MAX_SIZE];
                for x in 0..MAX_SIZE-1 {
                    for y in 0..MAX_SIZE-1 {
                        //Counts number of alive neighbours
                        let mut alive = 0;
                        for x_move in &moves {
                            for y_move in &moves {
                                if (x as isize + x_move) < 0 && (y as isize + y_move) < 0 {
                                    if grid[(MAX_SIZE as isize - (x as isize + x_move)) as usize-2]
                                        [(MAX_SIZE as isize - (y as isize + y_move)) as usize-2]{alive+=1};
                                } else if (x as isize + x_move) < 0 {
                                    if grid[(MAX_SIZE as isize - (x as isize + x_move)) as usize-2]
                                        [(y as isize + y_move) as usize]{alive+=1};
                                } else if (y as isize + y_move) < 0 {
                                    if grid[(x as isize + x_move) as usize]
                                        [(MAX_SIZE as isize - (y as isize + y_move)) as usize-2]{alive+=1};
                                } else {
                                    if grid[(x as isize + x_move) as usize][(y as isize + y_move) as usize]{alive+=1};
                                }
                            }
                        }
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
            }
        }
        e.mouse_cursor(|x, y| {
            cursor = [x, y];
        });

        if let Some(button) = e.press_args() {
            match button {
                Button::Keyboard(key) => match key {
                    Key::Left => {},
                    Key::Right =>{},
                    Key::Space =>{println!("Started");started=!started},
                    _ => {}
                },
                _ => {}
            }
        }

        if let Some(button) = e.release_args() {
            match button{
                Button::Mouse(button) =>{if !started{grid[(cursor[0]/10.0) as usize][(cursor[1]/10.0) as usize]=true}},
                _ => {}
                
            }
        }
    }
}
