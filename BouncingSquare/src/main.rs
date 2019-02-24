extern crate piston;
extern crate piston_window;
use piston_window::*;
use piston::event_loop::{Events, EventLoop, EventSettings};
pub struct Rectangle{
    pub colour: [f32; 4],
    pub position: [f64; 4],
    velocity:[f64; 2],
}
impl Rectangle{
    fn new() -> Self{
        Rectangle {
            colour: [1.0,0.5,0.0,1.0],
            position:[100.0,100.0,50.0,50.0],//Top Left X, Top Left Y, Width, Height 
            velocity:[5.0,5.0],
        }
    }
    fn update_velocity(&mut self,factor:f64){
        self.velocity[0]*=factor;
        self.velocity[1]*=factor;
    }
    fn update_colour(dt:f32,colour: f32)->f32 {
        if colour <= 0.0 {
            1.0
        } else {
            colour - 0.01 * dt * 120.0
        }
    }
    fn update(&mut self,args:&UpdateArgs,size:(f64,f64)){
        
        //Colour Update
        self.colour[0] = Self::update_colour(args.dt as f32, self.colour[0]);
        self.colour[1] = Self::update_colour(args.dt as f32, self.colour[1]);
        self.colour[2] = Self::update_colour(args.dt as f32, self.colour[2]);
        //X Update
        if self.position[0]<0.0 {
            self.velocity[0]=-self.velocity[0];          
        }
        if self.position[0]+self.position[2]>=size.0{
            self.velocity[0]=-self.velocity[0];  
        }
        self.position[0]+=self.velocity[0]*args.dt*120.0;

        //Y Update
        if self.position[1]<0.0 || self.position[1]+self.position[3]>=size.1{
            self.velocity[1]=-self.velocity[1];                   
        }
        self.position[1]+=self.velocity[1]*args.dt*120.0;
        
    }
}


fn main(){
    let mut rect=Rectangle::new();
    let mut window: PistonWindow=WindowSettings::new(
        "Bouncing-Square",
        [640,480])
        .exit_on_esc(true)
        .vsync(true)
        .build()
        .unwrap();


    let mut window_size: (f64, f64)=(0.0,0.0);
    let mut events = Events::new(EventSettings::new());
    events.set_ups(60);
    events.set_max_fps(60);
    while let Some(e) =events.next(&mut window){
        if let Some(args) = e.render_args() {
            window.draw_2d(&e, |c,g|{
                clear([1.0;4],g);
                rectangle(rect.colour, rect.position,c.transform, g);
            });
            window_size=(args.draw_width as f64,args.draw_height as f64);
        }
        if let Some(args)= e.update_args(){
            rect.update(&args,window_size);
        }
        if let Some(button)=e.press_args(){
            match button{
                Button::Keyboard(key) => {
                    match key{
                        Key::W =>{
                            rect.update_velocity(2.0);
                        }
                        Key::Up=>{
                            rect.update_velocity(2.0);
                        }
                        Key::S =>{
                            rect.update_velocity(0.5);
                        }
                        Key::Down =>{
                            rect.update_velocity(0.5);
                        }
                        Key::F5 =>{
                            rect.position[0]=10.0;
                            rect.position[1]=10.0;
                        }
                        _ => {}
                    }
                }
                _ => {}
            }
        }
    }
    
}