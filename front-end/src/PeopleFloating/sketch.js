export default function sketch (p) {
    let rotation = 0;
    let textBRuh;
    let data;


  

    p.preload = function() {
        const API_URL = 'http://127.0.0.1:8000/disasters/list/';
        data = p.loadJSON(API_URL)
    }

    p.setup = function () {
      p.createCanvas(600, 700, p.WEBGL);
        
      //camera
    //   var cam = p.createCamera();
    //   cam.move(0, 5, 0)

      textBRuh = p.createGraphics(1500, 200)
    //   textBRuh.fill(0,255,0)
        
        console.log(data.[0].country)
      textBRuh.textSize(44)
      textBRuh.text(data.[0].country + ' ' + data.[0].year + ' ' +data.[0].people_died + ' '+data.[0].disaster_type, 100, 100)
    };
  
  
    p.draw = function () {
      p.background(100);
      p.ambientLight(100);

      p.directionalLight(255, 255, 255, 0, 0, 1)

      p.orbitControl(1, 1, 0.1);
      p.push()
      p.rotateY(-rotation);
      p.texture(textBRuh)
      
        p.noStroke();
   
      p.cylinder(60, 50);
      p.pop()


      p.push()
      p.stroke(255);
      p.rotateY(rotation);
      p.box(50, 200, 50);
      p.pop()
        
      
        rotation+=0.02
     
    };
  };