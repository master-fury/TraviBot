function human(){
    let text = document.getElementById("custom_input").value;
    let data = {"type":"human","data":text};
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/reply',
        data : JSON.stringify(data),
        success: function(response) {
            let div = document.createElement('div');
            div.innerHTML = response.trim();
            document.getElementById("reply").appendChild(div.firstChild); 
            robot(text); 
        },
        error: function(xhr) {
             //Do Something to handle error 
        }
    });
            
};
    
function robot(text){
    let data = {"type":"robot","data":text};
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/reply',
        data : JSON.stringify(data),
        success: function(response) {
            let div = document.createElement('div');
            div.innerHTML = response.trim();
            document.getElementById("reply").appendChild(div.firstChild);       
        },
        error: function(xhr) {
            //Do Something to handle error 
          }
    });
        
};
    
function inital_robot(){
    let data = {"type":"robot","data":"HEY! How may I help You?"};
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/reply',
        data : JSON.stringify(data),
        success: function(response) {
            let div = document.createElement('div');
            div.innerHTML = response.trim();
            document.getElementById("reply").appendChild(div.firstChild);    
            },
        error: function(xhr) {
            //Do Something to handle error 
            }
        });
            
};
