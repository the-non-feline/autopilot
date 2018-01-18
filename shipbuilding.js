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
  function this.getCoordsOccupied() {
    var coords_occupied = []; 
    var xy_center = this.getXYPos(); 
    for(var x = 0; x < this.size[0]; x++) {
      for(var y = 0; y < this.size[1]; y++) {
        var scaledX = xy_center[0] + x * 20 - this.size[0] * 10 + 10; 
        var scaledY = xy_center[1] + y * 20 - this.size[1] * 10 + 10; 
        coords_occupied.append([scaledX, scaledY]) 
      } 
    } 
    return coords_occupied; 
  } 
