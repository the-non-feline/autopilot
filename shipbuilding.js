function Part(part_name, mass, hp, cost, area) {
  this.part_name = part_name; 
  this.mass = mass; 
  this.hp = hp; 
  this.cost = cost; 
  this.area = area; 
  this.XYPos = [null, null]; 
  function this.getPartText() {
    var raw_code = '{"pos":[' + String(this.XYPos[0]) + ',' + String(this.XYPos[1]) + '],"type":"' + this.part_name + '","dir":0}'; 
    console.log(raw_code); 
    return raw_code; 
  } 
  function this.getCoordsOccupied() {
    var coords_occupied = []; 
    var xy_center = this.getXYPos(); 
    for(var x = 0; x < this.area[0]; x++) {
      for(var y = 0; y < this.area[1]; y++) {
        var scaledX = xy_center[0] + x * 20 - this.area[0] * 10 + 10; 
        var scaledY = xy_center[1] + y * 20 - this.area[1] * 10 + 10; 
        coords_occupied.append([scaledX, scaledY]) 
      } 
    } 
    return coords_occupied; 
  } 
