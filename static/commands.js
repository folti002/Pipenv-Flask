function addName(){
  let name = document.getElementById("name").value;
  if(name){
    console.log(name);
    document.getElementById("nameList").innerHTML += "<li> " + name + "</li>";
  } else {
    console.log("Empty name was not added");
  }
}