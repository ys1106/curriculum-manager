window.onload = function() {
    document.getElementById("add_button").addEventListener('click', add);
    document.getElementById('exit').addEventListener('click', exit);
}


function add() {
  let addTable = document.getElementById('addTable');
  addTable.setAttribute('id','addTableDisplay');

}


function exit() {
  let displayTable = document.getElementById('addTableDisplay');
  console.log(displayTable);
  displayTable.setAttribute('id', 'addTable');
}
