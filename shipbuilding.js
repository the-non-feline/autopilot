function Part(name, mass, hp, cost, size) {
  this.name = name; 
  this.mass = mass; 
  this.hp = hp; 
  this.cost = cost; 
  this.size = size; 
  this.XYPos = [null, null]; 
  function this.getPartText() {
    var raw_code = '{"pos":[' + String(this.XYPos[0]) + ',' + String(this.XYPos[1]) + '],"type":"' + this.name + '","dir":0}'; 
    console.log(raw_code); 
    return raw_code; 
  } 
  /*function this.getCoordsOccupied() {
    var coords_occupied = [null, null]; 
    var xy_coords = this.getXYPos(); 
  */ 
} 
