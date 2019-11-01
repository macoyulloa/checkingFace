
function sendData(){
    var dataArray = $("form").serializeArray();
    var data = {}

    dataArray.map(function fun (obj) {
        data[obj.name] = obj.value;
    })

    $.ajax({    
        headers: {'Content-Type':'application/json'}, method: "POST",
        url: "https://api-jwt-v3.herokuapp.com/api/users",
        data: JSON.stringify({ user: data})
       })
}